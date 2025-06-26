import os
from typing import List

def chunk_text(text: str, max_tokens: int = 300) -> List[str]:
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) <= max_tokens:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

with open("data/nephrology_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

chunks = chunk_text(raw_text)

os.makedirs("embeddings", exist_ok=True)

with open("embeddings/nephrology_chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n---\n")

print(f"✅ Chunked {len(chunks)} text blocks to embeddings/nephrology_chunks.txt")
