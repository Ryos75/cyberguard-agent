



# 🛡️ CyberGuard — Agente de IA para Conscientização em Cibersegurança

**CyberGuard** é o assistente virtual de conscientização em segurança da informação da empresa fictícia **TechCorp**. 
Ele fica disponível 24h para que **colaboradores** tirem dúvidas sobre phishing, senhas, MFA, home office e resposta a incidentes, respondendo **exclusivamente** com base nos documentos e políticas internas da empresa (RAG).

> **Acesse ao vivo.**  https://agentecyberguard.duckdns.org
>



https://github.com/user-attachments/assets/6b05e30b-5eb9-4bdd-8782-fba4ff735a55











## 🎯 Problema de negócio

Segundo relatórios do setor (ex.: Verizon DBIR), a maioria das violações envolve o **fator humano**.
Treinamentos anuais não bastam: o colaborador precisa de orientação **no momento da dúvida**.
O CyberGuard preenche essa lacuna como um canal conversacional, centralizado e sempre disponível, reduzindo o tempo de resposta a incidentes e reforçando a cultura de segurança.

## 🏗️ Arquitetura

Documentos internos (8 formatos)
│ incorporação + chunking
▼
Embeddings (Gemini) → Vector Store (ChromaDB)
│
▼
Agente RAG (LangChain) ← LLM (Gemini)
│
▼
Interface de chat (Streamlit)


## 🧠 Decisões técnicas

- **RAG em vez de fine-tuning:** o conhecimento muda (políticas são revisadas). Com RAG, atualizar um documento e re-ingerir já reflete na resposta — sem retreinar modelo. Também elimina alucinação, pois o LLM só vê o contexto recuperado.
- **ChromaDB com persistência local:** banco vetorial leve, sem serviço externo, ideal para uma VM Always Free. Os embeddings ficam em disco (`chroma_db/`), sobrevivendo a reinícios.
- **Loaders manuais para XLSX, PPTX e JSON:** evitei a biblioteca `unstructured` (pesada e com dependências frágeis no Windows). Para XLSX, cada linha vira um documento no formato `coluna: valor`; para PPTX, cada slide vira um documento; para o glossário JSON, cada termo vira um chunk — o que **melhora** a recuperação.
- **Chunking 1000 / overlap 200:** equilíbrio entre contexto suficiente por chunk e precisão na busca; o overlap evita cortar uma regra no meio.
- **top-k = 5:** traz fontes suficientes para respostas cruzadas (ex.: incidente de phishing no CSV + prevenção no PPTX) sem poluir o prompt.
- **Modelos Gemini (free tier):** embeddings `gemini-embedding-001` e chat `gemini-3.1-flash-lite`, escolhidos por custo zero e baixa latência.
- **Streamlit como interface:** entrega um “produto” com cara real (sidebar institucional, boas-vindas, fontes citadas), não apenas um terminal — mais aderente ao uso por colaboradores leigos.
- **OCI Always Free + systemd:** custo zero e alta disponibilidade; o serviço `cyberguard` reinicia sozinho e sobe com a VM.

## 🚀 Como rodar localmente

```bash
git clone https://github.com/Ryos75/cyberguard-agent.git
cd cyberguard-agent
python -m venv venv
# Windows: venv\Scripts\activate  |  Linux/Mac: source venv/bin/activate
pip install -r requirements.txt

# Crie o .env com sua chave do Gemini:
# GOOGLE_API_KEY=sua_chave

python gerar_docs.py     # gera os documentos fictícios em docs/
python ingestao.py       # cria o vector store (chroma_db)
streamlit run app.py     # abre a interface em http://localhost:8501

🛠️ Pilha
Python · LangChain · Google Gemini · ChromaDB · Streamlit · Oracle Cloud Infrastructure (OCI)

## ☁️ Deploy na Oracle Cloud (OCI)

- **Serviço OCI utilizado:** Compute Instance (VM `VM.Standard.A1.Flex`, Always Free, Ubuntu).
- Aplicação servida por **Streamlit** atrás de serviço `systemd` (`cyberguard.service`).
- Acesso liberado via Security List (ingress 8501) + firewall da VM.
- *(Opcional)* HTTPS e domínio amigável via Nginx + Let’s Encrypt + DuckDNS.

## 🛠️ Stack

Python · LangChain · Google Gemini · ChromaDB · Streamlit · Oracle Cloud Infrastructure (OCI)

⚠️ Aviso
Projeto educacional com documentos fictícios . O agente fornece orientação
informativa de conscientização, não substitui políticas oficiais nem aparência de segurança.

📄 Licença
MIT
