import PyPDF2

import PyPDF2

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file provided by Streamlit's uploader."""
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text


def chunk_text(text, chunk_size=500):
    """Split text into chunks of a given size."""
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])
