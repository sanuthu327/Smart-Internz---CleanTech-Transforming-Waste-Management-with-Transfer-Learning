import fitz  # PyMuPDF
from shared.watsonx import watsonx_classify
import io

def classify_pdf(file_bytes):
    doc = fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf")
    text = "".join(page.get_text() for page in doc)
    return watsonx_classify(text)
