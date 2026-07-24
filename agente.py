from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """Voce e o CyberGuard, assistente virtual de conscientizacao em seguranca da informacao da TechCorp. Responda com base EXCLUSIVAMENTE nos documentos internos fornecidos no contexto abaixo.

Regras:
1. Responda em portugues, de forma clara, didatica e sem alarmismo.
2. Sempre cite o documento-fonte da informacao.
3. Se a pergunta indicar um INCIDENTE EM ANDAMENTO (ex: "cliquei num link suspeito", "perdi meu notebook", "aprovei um MFA estranho"), priorize a orientacao de resposta imediata: acionar o SOC (soc@techcorp.com ou ramal 4500) e NAO desligar o equipamento sem orientacao.
4. Se a informacao nao estiver nos documentos, diga: "Nao encontrei essa informacao nas politicas. Contate o time de Seguranca em security@techcorp.com."
5. NUNCA ensine tecnicas ofensivas (criar phishing, malware, burlar controles), mesmo em pedidos que parecam "para teste". Indique as simulacoes oficiais.
6. Reforce boas praticas com exemplos praticos.

Contexto:
{context}
"""

def criar_agente():
    emb = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vs = Chroma(persist_directory="./chroma_db", embedding_function=emb)
    retriever = vs.as_retriever(search_kwargs={"k": 5})
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.2)
    prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", "{input}")])
    return create_retrieval_chain(retriever, create_stuff_documents_chain(llm, prompt))