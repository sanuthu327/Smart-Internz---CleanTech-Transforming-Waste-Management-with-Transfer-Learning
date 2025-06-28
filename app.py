import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared.watsonx import watsonx_classify
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.classifier import classify_pdf
from services.codegen import generate_code


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/classify")
async def classify(file: UploadFile = File(...)):
    content = await file.read()
    result = classify_pdf(content)
    return result

@app.post("/codegen")
async def codegen(prompt: dict):
    try:
        code = generate_code(prompt["prompt"])
        return {"code": code}
    except Exception as e:
        return {"error": str(e)}

