## Project Overview

Engineered a document search solution employing web scraping, AI integration, and web scrolling; enhanced user search experience for 500+ documents, leading to a 50% reduction in average retrieval time and improved user satisfaction.

This system allows users to upload PDFs, ask questions, and get summarized results quickly using advanced LLMs. It combines voice and text input options, and supports seamless interaction through a Streamlit interface.

# Document Search & Summarization System

This project implements a document search and summarization system capable of:

- Scraping textual content from the web
- Processing PDFs
- Summarizing large documents using advanced LLMs
- Accepting user input via text or voice
- Providing interactive UI with Streamlit

---

## 🚀 Features

✅ **Text-based Search & Summarization**

- Scrape content from Wikipedia or Google Search
- Summarize documents with LLMs using LangChain

✅ **Voice Input Integration**

- Capture speech with microphone
- Convert speech to text
- Trigger summarization pipelines

✅ **PDF Chat Interface**

- Upload PDF files
- Chat with PDF content via Google Gemini

✅ **Multiple Model Backends**

- Google Gemini (Gemini-Pro)
- OpenAI GPT-3.5 Turbo

✅ **Streamlit User Interfaces**

- Interactive apps for user queries and summarization

---

## 🛠 Technologies Used

- Python
- LangChain
- Streamlit
- Google Generative AI API (Gemini)
- OpenAI GPT-3.5 Turbo
- BeautifulSoup (web scraping)
- SpeechRecognition
- PyPDF2
- FAISS (vector storage)

---

## 📂 Project Structure

Document_Summarization/
- app.py
- demo.py
- gem.py
- m1.py
- model_1.py
- model_1.1.py
- model_1.2.py
- model_ui.py
- model_ui_1.py
- multi_1.py
- requirements.txt
- README.md


---

## 🖥 How to Run

### 1. Clone This Repository

If you haven’t cloned yet:

git clone https://github.com/RanjithaaL/Prompt_Summarization.git
cd Document_Summarization

### 2. Install Requirements

Install all Python dependencies:

pip install -r requirements.txt

###  3. Run

To use OPENAI_API_key:
  streamlit run app.py

To use GEMINI_API_KEY:

streamlit run gem.py

---

### Environment Variables

Make sure you have a `.env` file in your project root containing:

OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_key_here

---





