import datetime
from rag.rag_utils import load_vectorstore
from tools.web_search import web_search
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain_community.chat_models import ChatOllama  # 🔁 Changed from ChatOpenAI

class ClinicalAgent:
    def __init__(self):
        self.vectorstore = load_vectorstore()
        self.chain = load_qa_with_sources_chain(
            ChatOllama(model="mistral", temperature=0), chain_type="stuff"
        )
        self.log_path = "logs/clinical_agent.log"

    def answer_query(self, query, patient_name):
        docs = self.vectorstore.similarity_search(query, k=4)
        response = self.chain.run(input_documents=docs, question=query)

        if "I don't know" in response or len(response.strip()) < 30:
            web_answer, url = web_search(query)
            self._log_interaction(patient_name, query, web_answer, source="web", url=url)
            return f"🔎 *Web Answer:* {web_answer}\n\nSource: {url}"

        self._log_interaction(patient_name, query, response, source="RAG")
        return f"📘 *Reference Answer:*\n{response}"

    def _log_interaction(self, patient, question, answer, source="RAG", url=None):
        timestamp = datetime.datetime.now().isoformat()
        with open(self.log_path, "a") as f:
            f.write(f"{timestamp} | Patient: {patient} | Source: {source} | Q: {question} | A: {answer[:200]}\n")
