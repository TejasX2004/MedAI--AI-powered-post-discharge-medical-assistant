import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.rag_utils import load_and_embed_pdf

load_and_embed_pdf("data/comprehensive-clinical-nephrology.pdf")
print("✅ PDF embedded into FAISS vectorstore.")

