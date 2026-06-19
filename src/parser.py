from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()

        if content:
            text += content + "\n" # Add newline after each page

    text = text.replace("\n", " ") # Replace newlines with spaces
    text = " ".join(text.split()) # Remove extra spaces

    return text