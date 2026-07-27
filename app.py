import streamlit as st
from agente import criar_agente

st.set_page_config(page_title="CyberGuard - TechCorp", page_icon="🛡️", layout="wide")

st.title("🛡️ CyberGuard")
st.markdown("### Assistente de Conscientização em Cibersegurança da **TechCorp**")
st.caption(
    "Canal interno e exclusivo para **colaboradores** tirarem dúvidas sobre phishing, "
    "senhas, MFA, home office e resposta a incidentes — 24h por dia, com base nas "
    "políticas oficiais da empresa."
)

with st.sidebar:
    st.header("🏢 Sobre o CyberGuard")
    st.markdown(
        "Sou o assistente virtual do time de Segurança da Informação da **TechCorp**. "
        " Fui criado para ajudar **você, colaborador**, a adotar práticas seguras no dia a dia, "
        "respondendo com base nas políticas e documentos internos da empresa."
    )
    st.markdown("**Posso ajudar com:**")
    st.markdown("- 🎣 Reconhecer e reportar phishing")
    st.markdown("- 🔐 Regras de senhas e MFA")
    st.markdown("- 🏠 Segurança no home office")
    st.markdown("- 🚨 O que fazer em um incidente")
    st.markdown("- 📚 Termos de segurança (glossário)")
    st.divider()
    st.markdown(
        "⚠️ **Aviso:** orientação informativa, não substitui o parecer do time de Segurança. "
        "Em incidentes reais, acione o SOC: `soc@techcorp.com` / ramal **4500**."
    )

if "agente" not in st.session_state:
    with st.spinner("Carregando base de conhecimento..."):
        st.session_state.agente = criar_agente()
    st.session_state.msgs = []

if not st.session_state.msgs:
    with st.chat_message("assistant"):
        st.markdown(
            "Olá, colaborador da TechCorp! 👋 Sou o **CyberGuard**.\n\n"
            "Estou aqui para tirar suas dúvidas de cibersegurança com base nas políticas "
            "internas da empresa. Pode me perguntar, por exemplo:"
        )
        st.markdown(
            "- *Cliquei em um link suspeito, o que faço?*\n"
            "- *Quantos caracteres minha senha precisa ter?*\n"
            "- *Posso usar o Wi-Fi do café para trabalhar?*"
        )

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("Ex: Cliquei num link suspeito, o que faço?"):
    st.session_state.msgs.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    with st.chat_message("assistant"):
        with st.spinner("Consultando as políticas da TechCorp..."):
            r = st.session_state.agente.invoke({"input": p})
            fontes = {d.metadata.get("fonte", "?") for d in r["context"]}
            txt = r["answer"] + f"\n\n📎 **Fontes:** {', '.join(sorted(fontes))}"
        st.markdown(txt)
    st.session_state.msgs.append({"role": "assistant", "content": txt})