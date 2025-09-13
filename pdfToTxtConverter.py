import os
from pdf2image import convert_from_path
import pytesseract

# Optional: set tesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def pdf_to_text(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for page_num, page in enumerate(pages):
        page_text = pytesseract.image_to_string(page)
        text += f"--- Page {page_num + 1} ---\n"
        text += page_text + "\n"
    return text

def batch_pdf_to_text(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"Processing {filename}...")

            extracted_text = pdf_to_text(pdf_path)

            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(extracted_text)

            print(f"Saved: {output_file}")

# Usage
pdf_folder = "path_to_your_pdf_folder"
text_output_folder = "path_to_save_txt_files"
batch_pdf_to_text(pdf_folder, text_output_folder)