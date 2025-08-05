# 📄 Resume Parser using NLP & Streamlit

A simple Resume Parser web application built with **Python, NLP (SpaCy)** and **Streamlit**.  
Upload a PDF or DOCX resume and extract essential information like **Name, Email, Phone Number, Skills**, etc.

---

## 🚀 Demo
🔗 [Live Streamlit App](https://<your-username>.streamlit.app)

---

## 📂 Features
- Upload Resume (PDF / DOCX)
- Extract Name, Email, Phone Number
- Extract Technical Skills from Resume
- View Full Resume Text
- Clean UI built with Streamlit

---

## 🛠 Tech Stack
- Python 3.x
- Streamlit
- SpaCy (NLP)
- pdfplumber (PDF Text Extraction)
- docx2txt (DOCX Text Extraction)
- Regular Expressions (Regex)

---

## 📦 Installation (Run Locally)
1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/Resume-Parser-NLP-Streamlit.git
    cd Resume-Parser-NLP-Streamlit
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download SpaCy Language Model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Run the Streamlit App:
    ```bash
    streamlit run app.py
    ```

5. Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💡 How it Works?
- Extracts text from uploaded resume (PDF/DOCX)
- Uses SpaCy for Named Entity Recognition (NER) to extract Names
- Uses Regex to find Emails and Phone Numbers
- Matches keywords from a predefined Skills list

---

## 📚 Folder Structure
