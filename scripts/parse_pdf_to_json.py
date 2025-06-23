import fitz  # PyMuPDF
import json
import os

INPUT_DIR = 'input_data'
OUTPUT_DIR = 'parsed_json'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text.strip()

def create_json_from_pdf(pdf_path):
    text = extract_pdf_text(pdf_path)
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(OUTPUT_DIR, f"{filename}.json")

    # Customize this structure as needed
    data = {
        "filename": filename,
        "content": text
    }

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, file)
            create_json_from_pdf(pdf_path)

if __name__ == "__main__":
    main()
