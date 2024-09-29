import streamlit as st
from PyPDF2 import PdfReader

# Function to extract text from specific pages in a PDF
def extract_text_from_pdf(pdf, start_page, end_page):
    try:
        reader = PdfReader(pdf)
        text = ""
        for page_num in range(start_page - 1, end_page):
            text += reader.pages[page_num].extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"


# Streamlit App UI

st.title("Question Paper Generator")

# File Upload for PDF
uploaded_pdf = st.file_uploader("Upload your course book PDF", type="pdf")

if uploaded_pdf:
    # Take input for start and end page numbers
    start_page = st.number_input("Enter the start page number:", min_value=1, step=1)
    end_page = st.number_input("Enter the end page number:", min_value=start_page, step=1)
    course_text = extract_text_from_pdf(uploaded_pdf, start_page, end_page)
    st.write(f"Sample course text from selected pages:{course_text}")