import fitz  # PyMuPDF

pdf_path = "data/comprehensive-clinical-nephrology.pdf"
output_path = "data/nephrology_text.txt"

doc = fitz.open(pdf_path)
with open(output_path, "w", encoding="utf-8") as f:
    for page in doc:
        text = page.get_text()
        f.write(text + "\n\n")

print("✅ Extracted PDF text to nephrology_text.txt")
