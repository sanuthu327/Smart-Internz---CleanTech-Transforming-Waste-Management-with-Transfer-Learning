## SmartSDLC Setup Instructions

1. Create virtual environment and install dependencies:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

2. Run FastAPI backend:
    cd backend
    uvicorn app:app --reload

3. In another terminal, run Streamlit frontend:
    cd frontend
    streamlit run app.py

App will be available at http://localhost:8501
