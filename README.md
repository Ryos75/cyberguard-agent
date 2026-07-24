# 🛡️ CyberGuard — Agente de IA para Conscientização em Cibersegurança

Agente conversacional corporativo que responde dúvidas de colaboradores sobre
**phishing, senhas, MFA, home office e resposta a incidentes**, com base em
documentos internos da empresa (RAG). Desenvolvido para o desafio **Alura Agentes**.

>  **Demo rodando na nuvem (OCI):**
>
> ![Demo do CyberGuard](assets/demo.gif)
> *(imagem/vídeo a ser adicionado após o deploy na Oracle Cloud)*

## 🎯 O que o CyberGuard faz

- Responde perguntas com base **exclusivamente** em documentos internos (sem alucinar).
- Cobre **8 formatos** de arquivo: PDF, DOCX, XLSX, PPTX, MD, CSV, JSON e HTML.
- Trata **incidentes em andamento** com urgência (orienta acionar o SOC, não desligar a máquina).
- **Recusa** pedidos ofensivos (ex.: "criar um phishing") e indica as simulações oficiais.
- Cita o **documento-fonte** de cada resposta.

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


## 🧠 Domínio de conhecimento (empresa fictícia TechCorp)

| Documento | Formato | Conteúdo |
|---|---|---|
| Política de Segurança da Informação | PDF | Classificação da informação, MFA, SOC |
| Manual de Senhas e MFA | DOCX | Regras de senha, Bitwarden, MFA fatigue |
| Inventário de Ativos | XLSX | Sistemas críticos, RTO/RPO |
| Treinamento Anti-Phishing | PPTX | Os 7 sinais de phishing |
| Política de Home Office | MD | VPN, Wi-Fi, bloqueio de tela |
| Histórico de Incidentes | CSV | Casos anonimizados e lições aprendidas |
| Glossário de Segurança | JSON | Phishing, ransomware, zero trust, etc. |
| FAQ "O que fazer se..." | HTML | Resposta imediata a incidentes |

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

☁️ Infraestrutura
Hospedado em VM Oracle Cloud Infrastructure (Always Free) .
(detalhes para implantar a serem completados)

⚠️ Aviso
Projeto educacional com documentos fictícios . O agente fornece orientação
informativa de conscientização, não substitui políticas oficiais nem aparência de segurança.

📄 Licença
MIT