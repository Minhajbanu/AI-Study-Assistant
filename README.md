# 🤖 AI Study Assistant


An **AI-powered Study Assistant** that allows students to upload study materials (PDF/TXT) and interact with them through a chatbot while automatically generating **structured study notes**.

The project uses **Retrieval-Augmented Generation (RAG)** with local Large Language Models to provide accurate answers based on uploaded documents.

---

## 🚀 Features

- 📄 Upload study materials (PDF/TXT)
- 🤖 Chat with your documents
- 📝 Generate structured study notes automatically
- 🔍 Semantic search using embeddings
- ⚡ Runs completely with **local LLMs**
- 📚 Vector database for efficient retrieval

---

## 🏗 System Architecture

```
User Uploads Document
        │
        ▼
Text Extraction
        │
        ▼
Text Chunking
        │
        ▼
Embeddings Generation
(all-MiniLM-L6-v2)
        │
        ▼
Vector Database (FAISS)
        │
        ▼
Retriever
        │
        ▼
LLM (Gemma / Mistral via Ollama)
        │
        ▼
Chatbot Answer / Notes Generation
```

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core Programming |
| Streamlit | Web Interface |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| Sentence Transformers | Embeddings |
| Ollama | Local LLM Runner |

### Models Used

- **Gemma**
- **all-MiniLM-L6-v2**

---

## 📂 Project Structure

```
AI-Study-Assistant
│
├── app.py
├── chatbot.py
├── notes_generator.py
├── rag_pipeline.py
├── requirements.txt
├── users.db
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI-Study-Assistant.git
cd AI-Study-Assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama

Download Ollama:

https://ollama.ai

Run the Ollama server:

```bash
ollama serve
```

---

### 5️⃣ Download LLM Models

```bash
ollama pull gemma3:4b
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 How It Works

1. User uploads study documents
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. Stored in a **FAISS vector database**
5. When a question is asked:
   - Relevant chunks are retrieved
   - Context is sent to the LLM
   - LLM generates the answer

This approach is known as **Retrieval-Augmented Generation (RAG)**.

---

## 💡 Use Cases

- Exam preparation
- Quick revision
- Interactive document Q&A
- Automatic study notes creation

---

## 📌 Future Improvements

- Support for DOCX and PPT files
- Multi-document querying
- Conversation memory
- Export notes as PDF
- Improved UI

---

## 👨‍💻 Author

**Minhaj Banu**

AI / Machine Learning Enthusiast
