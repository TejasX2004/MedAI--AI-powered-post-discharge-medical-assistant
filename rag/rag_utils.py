# rag/rag_utils.py
import os
import faiss
import pickle
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def load_and_embed_pdf(pdf_path, persist_path="embeddings/nephrology_faiss"):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Chunk
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    # Embed
    
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save FAISS index
    os.makedirs(persist_path, exist_ok=True)
    vectorstore.save_local(persist_path)

    return vectorstore

def load_vectorstore(persist_path="embeddings/nephrology_faiss"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(persist_path, embeddings,allow_dangerous_deserialization=True)
