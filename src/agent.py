"""
CyberGuard AI - Camada do agente.

Responsabilidades:
- receber a pergunta do usuário;
- recuperar conhecimento relevante;
- montar o prompt do sistema;
- enviar o contexto para o modelo de linguagem;
- devolver uma resposta defensiva e orientada à segurança.

O arquivo foi estruturado para utilizar Ollama localmente.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

try:
    from knowledge import search_knowledge
except ImportError:
    search_knowledge = None


# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "120"))

MAX_CONTEXT_CHARS = 12000


# ---------------------------------------------------------------------------
# Prompt do sistema
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """
Você é o CyberGuard AI, um assistente virtual especializado em
cibersegurança defensiva.

Seu objetivo é ajudar o usuário a compreender riscos, prevenir
incidentes, identificar sinais suspeitos e executar ações iniciais
seguras de resposta.

REGRAS PRINCIPAIS:

1. ATUAÇÃO DEFENSIVA
   - Ajude com prevenção, diagnóstico inicial, contenção, recuperação,
     boas práticas e educação em segurança.
   - Não forneça instruções para invasão, exploração não autorizada,
     roubo de credenciais, desenvolvimento de malware, persistência,
     evasão de controles ou comprometimento de sistemas de terceiros.

2. BASE DE CONHECIMENTO
   - Priorize o contexto fornecido pela base de conhecimento.
   - Não invente informações para preencher lacunas.
   - Se o contexto não for suficiente para responder com segurança,
     diga explicitamente que a base não possui informação suficiente.
   - Você pode explicar conceitos gerais quando apropriado, mas deixe
     claro quando uma informação não estiver presente no contexto.

3. INCERTEZA
   - Não trate um sintoma como prova definitiva de comprometimento.
   - Diferencie fatos, hipóteses e recomendações.
   - Use expressões como "pode indicar", "é compatível com" ou
     "é necessário verificar" quando não houver evidência suficiente.

4. INCIDENTES
   - Priorize contenção segura, preservação de evidências,
     documentação e acionamento dos responsáveis.
   - Evite recomendar ações destrutivas sem contexto.
   - Não recomende apagar arquivos, formatar máquinas ou destruir
     evidências como primeira resposta.

5. DADOS E CREDENCIAIS
   - Nunca solicite ao usuário senhas, tokens, chaves privadas ou
     outras credenciais reais.
   - Recomende a troca/revogação de credenciais quando houver indícios
     de comprometimento, conforme o contexto.

6. COMUNICAÇÃO
   - Responda em português do Brasil.
   - Seja claro, objetivo e didático.
   - Prefira listas e passos numerados quando isso facilitar a execução.
   - Não seja alarmista.

7. ESCALONAMENTO
   - Quando houver risco relevante ou incidente ativo, recomende o
     acionamento da equipe de TI, segurança ou responsável pelo ambiente.

FORMATO PREFERENCIAL:

- Resposta direta ao problema.
- Explicação curta do risco.
- Ações recomendadas.
- O que evitar, quando relevante.
- Próximo passo ou indicação de escalonamento, quando necessário.
""".strip()


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def _format_sources(results: list[dict[str, Any]]) -> str:
    """Formata os documentos recuperados para serem enviados ao LLM."""
    if not results:
        return "Nenhum documento relevante foi encontrado na base."

    chunks: list[str] = []
    total_chars = 0

    for result in results:
        title = result.get("titulo") or result.get("arquivo", "Documento")
        category = result.get("categoria", "desconhecida")
        content = result.get("conteudo", "").strip()

        if not content:
            continue

        chunk = (
            f"### Documento: {title}\n"
            f"Categoria: {category}\n"
            f"Arquivo: {result.get('arquivo', 'desconhecido')}\n\n"
            f"{content}"
        )

        remaining = MAX_CONTEXT_CHARS - total_chars
        if remaining <= 0:
            break

        chunk = chunk[:remaining]
        chunks.append(chunk)
        total_chars += len(chunk)

    return "\n\n---\n\n".join(chunks)


def _build_prompt(question: str, context: str) -> str:
    """Monta a mensagem enviada ao modelo."""
    return f"""
Use o contexto da base de conhecimento abaixo para responder à pergunta.

CONTEXTO DA BASE DE CONHECIMENTO
================================
{context}
================================

PERGUNTA DO USUÁRIO
================================
{question}
================================

Instruções adicionais:
- Priorize o contexto fornecido.
- Não invente fatos, fontes ou procedimentos.
- Se não houver informação suficiente, informe essa limitação.
- Mantenha a resposta no escopo defensivo.
- Não peça senhas, tokens ou outras credenciais reais.
- Se a situação parecer um possível incidente, explique ações iniciais
  seguras e quando procurar a equipe responsável.
""".strip()


def _call_ollama(prompt: str) -> str:
    """Envia uma solicitação para a API local do Ollama."""
    payload = {
        "model": OLLAMA_MODEL,
        "system": SYSTEM_PROMPT,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
        },
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        f"{OLLAMA_URL.rstrip('/')}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=OLLAMA_TIMEOUT) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Não foi possível conectar ao Ollama. "
            "Verifique se o Ollama está em execução e se a URL está correta."
        ) from exc
    except TimeoutError as exc:
        raise RuntimeError(
            "O modelo demorou mais que o tempo limite para responder."
        ) from exc

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("O Ollama retornou uma resposta inválida.") from exc

    response_text = result.get("response")

    if not response_text:
        raise RuntimeError("O Ollama não retornou conteúdo na resposta.")

    return str(response_text).strip()


# ---------------------------------------------------------------------------
# API principal utilizada pelo app.py
# ---------------------------------------------------------------------------

def ask_agent(question: str) -> str:
    """
    Processa uma pergunta usando a base de conhecimento e o LLM.

    A função é mantida simples para que o app.py dependa somente desta
    interface e a implementação possa evoluir posteriormente para RAG,
    embeddings ou outro provedor de LLM.
    """
    question = question.strip()

    if not question:
        return "Digite uma pergunta para o CyberGuard AI."

    # Recuperação de conhecimento
    if search_knowledge is None:
        context = (
            "A camada de recuperação (`knowledge.py`) ainda não está "
            "disponível. Não há contexto recuperado da base."
        )
    else:
        try:
            results = search_knowledge(question, limit=5)
            context = _format_sources(results)
        except Exception as exc:
            context = (
                "Não foi possível consultar a base de conhecimento. "
                f"Erro técnico: {type(exc).__name__}: {exc}"
            )

    prompt = _build_prompt(question, context)

    return _call_ollama(prompt)


# ---------------------------------------------------------------------------
# Execução direta para teste
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("CyberGuard AI - teste do agente")
    print(f"Modelo: {OLLAMA_MODEL}")
    print(f"Ollama: {OLLAMA_URL}")
    print()

    question = input("Pergunta: ").strip()

    if question:
        try:
            print("\nResposta:\n")
            print(ask_agent(question))
        except Exception as exc:
            print(f"\nErro: {type(exc).__name__}: {exc}")
