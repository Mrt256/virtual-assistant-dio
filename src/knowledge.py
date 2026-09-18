"""
CyberGuard AI - Base de conhecimento.

Este módulo lê os documentos Markdown existentes em:

    data/
        phishing/
        malware/
        senhas/
        incidentes/
        redes/
        backup/
        conceitos/

A primeira versão utiliza uma busca simples baseada em palavras-chave.
Ela foi mantida propositalmente sem banco vetorial/embeddings para que
o projeto seja fácil de entender, executar e demonstrar.

Posteriormente, este módulo pode evoluir para embeddings + RAG sem que
o restante da aplicação precise mudar sua interface principal.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"


# ---------------------------------------------------------------------------
# Stopwords
# ---------------------------------------------------------------------------

STOPWORDS = {
    "a", "à", "ao", "aos", "as", "às", "até", "com", "como", "da", "das",
    "de", "dela", "dele", "deles", "do", "dos", "e", "é", "em", "entre",
    "era", "essa", "esse", "esta", "este", "eu", "foi", "há", "isso",
    "isto", "já", "mais", "mas", "me", "mesmo", "na", "nas", "não", "nem",
    "no", "nos", "num", "numa", "o", "os", "ou", "para", "pela", "pelas",
    "pelo", "pelos", "por", "que", "qual", "quando", "se", "sem", "ser",
    "seu", "sua", "suas", "também", "tem", "tenho", "um", "uma", "umas",
    "uns", "vai", "você", "vocês",
}


# ---------------------------------------------------------------------------
# Leitura e normalização
# ---------------------------------------------------------------------------

def _normalize(text: str) -> str:
    """Normaliza texto para comparação."""
    text = text.lower()

    # Mantém letras/números e transforma pontuação em espaços.
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)

    # Remove espaços duplicados.
    return re.sub(r"\s+", " ", text).strip()


def _tokenize(text: str) -> list[str]:
    """Transforma uma frase em tokens úteis para busca."""
    normalized = _normalize(text)

    tokens = []
    for token in normalized.split():
        if len(token) < 3:
            continue
        if token in STOPWORDS:
            continue
        tokens.append(token)

    return tokens


# ---------------------------------------------------------------------------
# Frontmatter YAML simples
# ---------------------------------------------------------------------------

def _parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """
    Extrai um frontmatter YAML simples.

    O projeto utiliza principalmente campos escalares e uma lista
    chamada 'fontes'. Para evitar dependência adicional, o parser
    suporta somente a estrutura utilizada pelos documentos atuais.
    """
    content = content.lstrip("\ufeff")

    if not content.startswith("---"):
        return {}, content

    lines = content.splitlines()

    if len(lines) < 3:
        return {}, content

    end_index = None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, content

    metadata: dict[str, Any] = {}
    current_list_key: str | None = None

    for line in lines[1:end_index]:
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        # Item de lista, por exemplo:
        #   - CERT.br
        if stripped.startswith("- ") and current_list_key:
            metadata.setdefault(current_list_key, []).append(
                stripped[2:].strip()
            )
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            metadata[key] = []
            current_list_key = key
            continue

        current_list_key = None

        # Remove aspas simples ou duplas quando presentes.
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]

        metadata[key] = value

    body = "\n".join(lines[end_index + 1:]).strip()

    return metadata, body


# ---------------------------------------------------------------------------
# Carregamento da base
# ---------------------------------------------------------------------------

def load_knowledge_base(data_dir: Path = DATA_DIR) -> list[dict[str, Any]]:
    """
    Carrega todos os arquivos .md da base de conhecimento.

    Retorna uma lista de documentos com metadados, conteúdo e caminho.
    """
    if not data_dir.exists():
        return []

    documents: list[dict[str, Any]] = []

    for file_path in sorted(data_dir.rglob("*.md")):
        try:
            raw_content = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        metadata, body = _parse_frontmatter(raw_content)

        relative_path = file_path.relative_to(data_dir)

        category = metadata.get("categoria")
        if not category:
            category = relative_path.parts[0] if relative_path.parts else "geral"

        title = metadata.get("titulo")

        if not title:
            title = file_path.stem.replace("_", " ").replace("-", " ").title()

        documents.append(
            {
                "arquivo": str(relative_path).replace("\\", "/"),
                "caminho": str(file_path),
                "titulo": title,
                "categoria": category,
                "tipo": metadata.get("tipo", ""),
                "nivel": metadata.get("nivel", ""),
                "versao": metadata.get("versao", ""),
                "fontes": metadata.get("fontes", []),
                "conteudo": body,
                "texto_busca": _normalize(
                    f"{title} {category} {metadata.get('tipo', '')} "
                    f"{body}"
                ),
            }
        )

    return documents


# ---------------------------------------------------------------------------
# Busca
# ---------------------------------------------------------------------------

def _score_document(document: dict[str, Any], query_tokens: list[str]) -> float:
    """
    Calcula uma pontuação simples de relevância.

    Termos encontrados no título/categoria recebem maior peso do que
    ocorrências genéricas no corpo do documento.
    """
    if not query_tokens:
        return 0.0

    title = _normalize(str(document.get("titulo", "")))
    category = _normalize(str(document.get("categoria", "")))
    doc_type = _normalize(str(document.get("tipo", "")))
    content = document.get("texto_busca", "")

    score = 0.0
    matched = 0

    for token in query_tokens:
        if token in title:
            score += 5.0
            matched += 1
        elif token in category:
            score += 4.0
            matched += 1
        elif token in doc_type:
            score += 3.0
            matched += 1
        elif token in content:
            score += 1.0
            matched += 1

    # Bônus para perguntas que possuem vários termos coincidentes.
    coverage = matched / len(query_tokens)
    score += coverage * 2.0

    return score


def search_knowledge(
    query: str,
    limit: int = 5,
    data_dir: Path = DATA_DIR,
) -> list[dict[str, Any]]:
    """
    Busca documentos relevantes na base.

    Args:
        query: pergunta ou termos pesquisados.
        limit: quantidade máxima de documentos retornados.
        data_dir: caminho da base de conhecimento.

    Returns:
        Lista de documentos ordenados por relevância.
    """
    if limit <= 0:
        return []

    documents = load_knowledge_base(data_dir)

    if not documents:
        return []

    query_tokens = _tokenize(query)

    if not query_tokens:
        return documents[:limit]

    scored_documents: list[dict[str, Any]] = []

    for document in documents:
        score = _score_document(document, query_tokens)

        if score > 0:
            result = document.copy()
            result["score"] = round(score, 4)
            scored_documents.append(result)

    scored_documents.sort(
        key=lambda item: (
            item["score"],
            len(item.get("conteudo", "")),
        ),
        reverse=True,
    )

    return scored_documents[:limit]


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def list_documents(data_dir: Path = DATA_DIR) -> list[dict[str, Any]]:
    """Retorna um resumo dos documentos disponíveis."""
    documents = load_knowledge_base(data_dir)

    return [
        {
            "arquivo": document["arquivo"],
            "titulo": document["titulo"],
            "categoria": document["categoria"],
            "tipo": document["tipo"],
            "nivel": document["nivel"],
            "versao": document["versao"],
        }
        for document in documents
    ]


def get_statistics(data_dir: Path = DATA_DIR) -> dict[str, Any]:
    """Retorna estatísticas simples da base."""
    documents = load_knowledge_base(data_dir)

    categories: dict[str, int] = {}

    for document in documents:
        category = document["categoria"]
        categories[category] = categories.get(category, 0) + 1

    return {
        "total_documentos": len(documents),
        "categorias": categories,
    }


# ---------------------------------------------------------------------------
# Teste pelo terminal
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    stats = get_statistics()

    print("CyberGuard AI - Base de Conhecimento")
    print(f"Diretório: {DATA_DIR}")
    print(f"Documentos encontrados: {stats['total_documentos']}")
    print()

    if stats["categorias"]:
        print("Documentos por categoria:")
        for category, amount in sorted(stats["categorias"].items()):
            print(f"  - {category}: {amount}")

    print()
    query = input("Pesquisar na base: ").strip()

    if query:
        results = search_knowledge(query, limit=5)

        print()
        if not results:
            print("Nenhum documento relevante encontrado.")
        else:
            print("Resultados:")
            for result in results:
                print(
                    f"- {result['titulo']} "
                    f"[{result['categoria']}] "
                    f"(score={result['score']})"
                )
                print(f"  {result['arquivo']}")
