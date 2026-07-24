import streamlit as st
from agente import criar_agente

st.set_page_config(page_title="CyberGuard - Seguranca TechCorp", page_icon="🛡️")
st.title("🛡️ CyberGuard - Assistente de Ciberseguranca")
st.caption("Tire duvidas sobre phishing, senhas, home office e resposta a incidentes.")

if "agente" not in st.session_state:
    with st.spinner("Carregando base de conhecimento..."):
        st.session_state.agente = criar_agente()
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("Ex: Cliquei num link suspeito, o que faco?"):
    st.session_state.msgs.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    with st.chat_message("assistant"):
        with st.spinner("Consultando documentos..."):
            r = st.session_state.agente.invoke({"input": p})
            fontes = {d.metadata.get("fonte", "?") for d in r["context"]}
            txt = r["answer"] + f"\n\n📎 **Fontes:** {', '.join(sorted(fontes))}"
        st.markdown(txt)
    st.session_state.msgs.append({"role": "assistant", "content": txt})