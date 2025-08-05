# Resume Parser using NLP & Streamlit

import streamlit as st
import pdfplumber
import docx2txt
import spacy
import re

# Load SpaCy NLP Model
nlp = spacy.load('en_core_web_sm')

# Helper Functions
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def extract_text_from_docx(uploaded_file):
    return docx2txt.process(uploaded_file)

def extract_emails(text):
    return re.findall(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)

def extract_phone_numbers(text):
    return re.findall(r'\b\d{10}\b', text)

def extract_names(text):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    return names

def extract_skills(text):
    skills_db = ['python', 'java', 'c++', 'machine learning', 'deep learning', 'nlp', 'sql', 'excel', 'tensorflow', 'keras']
    skills_found = [skill for skill in skills_db if skill.lower() in text.lower()]
    return skills_found

# Streamlit UI
st.title('Resume Parser using NLP')

uploaded_file = st.file_uploader('Upload Resume (PDF or DOCX)', type=['pdf', 'docx'])

if uploaded_file is not None:
    if uploaded_file.type == 'application/pdf':
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    st.subheader('Extracted Information:')

    emails = extract_emails(resume_text)
    phone_numbers = extract_phone_numbers(resume_text)
    names = extract_names(resume_text)
    skills = extract_skills(resume_text)

    st.write(f'**Name(s):** {names}')
    st.write(f'**Email(s):** {emails}')
    st.write(f'**Phone Number(s):** {phone_numbers}')
    st.write(f'**Skills:** {skills}')

    with st.expander("Show Full Resume Text"):
        st.write(resume_text)

    st.success("Parsing Completed!")

else:
    st.info("Please upload a resume to proceed.")


