import streamlit as st

st.set_page_config(page_title="GitHub Profile ReadME Generator", page_icon="src/favicon.png", layout="wide")
from WebPages.create_page import CreatePage
from WebPages.preview import preview
from WebPages import download_readme

col1, col2 = st.columns(2)
with open("src/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with col2:
    x = CreatePage()
    x.create_page()

with col1:
    markdown = preview(x)

with col2:
    download_readme(markdown)

