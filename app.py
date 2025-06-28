import streamlit as st
import requests

st.set_page_config(page_title="SmartSDLC", layout="centered")
st.title("SmartSDLC Dashboard")

st.subheader("Upload PDF Requirements")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file:
    with st.spinner("Classifying requirements..."):
        res = requests.post("http://localhost:8000/classify", files={"file": uploaded_file})
        if res.status_code == 200:
            output = res.json()
            for phase, items in output.items():
                st.markdown(f"### {phase}")
                for line in items:
                    st.write("-", line)

st.subheader("AI Code Generator")
prompt = st.text_area("Enter requirement prompt")
if st.button("Generate Code") and prompt:
    with st.spinner("Generating code..."):
        res = requests.post("http://localhost:8000/codegen", json={"prompt": prompt})
        st.code(res.json().get("code"))
