"""
CyberGuard AI - Interface principal da aplicação.

Este arquivo contém somente a camada de interface (Streamlit).
A lógica do agente e a recuperação da base de conhecimento ficam
separadas em:
    src/agent.py
    src/knowledge.py

Execução, a partir da raiz do projeto:
    streamlit run src/app.py
"""

from pathlib import Path
import sys

import streamlit as st


# ---------------------------------------------------------------------------
# Configuração de caminhos
# ---------------------------------------------------------------------------

SRC_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SRC_DIR.parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

DATA_DIR = PROJECT_DIR / "data"


# ---------------------------------------------------------------------------
# Integração com a camada do agente
# ---------------------------------------------------------------------------

try:
    from agent import ask_agent
except ImportError:
    ask_agent = None


def generate_response(question: str) -> str:
    """
    Envia a pergunta para a camada do agente.

    O app não contém a lógica do LLM. Isso permite trocar Ollama,
    outro provedor ou a estratégia de RAG sem alterar a interface.
    """
    if ask_agent is None:
        return (
            "⚠️ O módulo `agent.py` ainda não está disponível.\n\n"
            "A interface está funcionando, mas a camada do agente ainda "
            "precisa ser implementada."
        )

    try:
        response = ask_agent(question)
    except Exception as exc:
        return (
            "Não foi possível processar a solicitação no momento.\n\n"
            f"Detalhes técnicos: `{type(exc).__name__}: {exc}`"
        )

    if response is None:
        return "O agente não retornou uma resposta."

    return str(response)


# ---------------------------------------------------------------------------
# Estado da conversa
# ---------------------------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------------------------------------------------
# Configuração da página
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------------------
# CSS leve para identidade visual
# ---------------------------------------------------------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            color: #6b7280;
            font-size: 1.05rem;
            margin-bottom: 1.5rem;
        }

        .warning-box {
            padding: 1rem;
            border-radius: 0.6rem;
            border: 1px solid rgba(128, 128, 128, 0.35);
            margin-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.title("🛡️ CyberGuard AI")
    st.caption("Assistente de Cibersegurança")

    st.divider()

    st.subheader("Sobre o agente")
    st.write(
        "Assistente voltado à prevenção, identificação inicial e "
        "resposta defensiva a situações de cibersegurança."
    )

    st.subheader("Temas da base")
    st.markdown(
        """
        - 🎣 Phishing
        - 🦠 Malware
        - 🔐 Senhas e autenticação
        - 🚨 Incidentes
        - 🌐 Redes
        - 💾 Backup
        - 📚 Conceitos de segurança
        """
    )

    st.divider()

    st.subheader("Exemplos")
    examples = [
        "Recebi um e-mail suspeito. O que devo verificar?",
        "Cliquei em um link de phishing. O que faço agora?",
        "Qual a diferença entre IDS e IPS?",
        "Como proteger meus backups contra ransomware?",
        "O que é autenticação multifator?",
    ]

    for example in examples:
        if st.button(example, use_container_width=True):
            st.session_state.pending_question = example

    st.divider()

    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pop("pending_question", None)
        st.rerun()

    st.caption("CyberGuard AI • Projeto educacional DIO")


# ---------------------------------------------------------------------------
# Cabeçalho
# ---------------------------------------------------------------------------

st.markdown('<div class="main-title">🛡️ CyberGuard AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    "Assistente virtual para prevenção e resposta inicial em cibersegurança."
    "</div>",
    unsafe_allow_html=True,
)

st.info(
    "O CyberGuard AI fornece orientação defensiva. "
    "Ele não substitui profissionais de segurança e não deve ser usado "
    "para realizar acesso não autorizado, exploração ou outras atividades ofensivas."
)


# ---------------------------------------------------------------------------
# Histórico da conversa
# ---------------------------------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------------------------------------------------------
# Entrada
# ---------------------------------------------------------------------------

pending_question = st.session_state.pop("pending_question", None)
question = st.chat_input("Digite sua dúvida sobre cibersegurança...")

if pending_question and not question:
    question = pending_question

if question:
    question = question.strip()

    if not question:
        st.warning("Digite uma pergunta antes de enviar.")
        st.stop()

    # Exibe a pergunta do usuário
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Gera a resposta
    with st.chat_message("assistant"):
        with st.spinner("Consultando a base de conhecimento..."):
            response = generate_response(question)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )


# ---------------------------------------------------------------------------
# Estado inicial
# ---------------------------------------------------------------------------

if not st.session_state.messages:
    st.markdown("### Como posso ajudar?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            **Prevenção**

            Pergunte sobre phishing, senhas, MFA, engenharia social,
            backups, redes e outras boas práticas.
            """
        )

    with col2:
        st.markdown(
            """
            **Incidentes**

            Descreva uma situação suspeita e receba orientação inicial
            sobre identificação, contenção e próximos passos.
            """
        )
