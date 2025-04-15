# 📊 FinSight — AI-Powered Financial Research Assistant

**FinSight** is an intelligent research assistant designed to help users gain insights from multiple financial or research-related web sources in seconds. Built using powerful LLMs, embeddings, and retrieval-augmented generation (RAG), FinSight allows users to simply paste URLs and start asking complex questions — all within a clean and interactive Streamlit interface.

---

## 🚀 Features

- 🔗 **Multi-URL Support:** Paste up to 4 URLs (research articles, blogs, or reports) to fetch and analyze their content.  
- 🧠 **LLM-Powered QA:** Ask questions about the combined content and get accurate, citation-backed answers.  
- 🧾 **Sources Included:** Each answer includes references to the original source(s) to maintain credibility.  
- ⚡ **In-Memory Vector Store:** Fast, transient vector database created at runtime — no disk storage needed.  
- 💬 **Chat-like Interface:** Smooth and responsive UI built with Streamlit for an intuitive experience.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Backend:** `langchain-openai`, `ChatOpenAI`  
- **Embeddings & RAG:** LangChain + FAISS (in-memory) 
- **State Management:** Streamlit’s `session_state`

---

## 🧪 How It Works

1. **User Inputs:** You enter up to 4 URLs into the sidebar.  
2. **Web Scraping:** Each URL is scraped for its textual content using Langchain's `UnstructuredURLLoader`.  
3. **Chunking & Embedding:** Content is split into chunks and converted into vector embeddings.  
4. **Vector Storage:** FAISS stores these vectors *in memory* for runtime-only persistence.  
5. **QA Chain:** Your queries are answered via `RetrievalQAWithSourcesChain` using context-aware retrieval.  
6. **Response Display:** Answer + sources shown instantly in the main interface.

---

## 📦 Installation

```bash
git clone https://github.com/Zorain98/FinSight-Financial-Research-AI-Agent.git
cd FinSight
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔑 API Keys

Create a .streamlit folder and inside it, create a secrets.toml file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 📚 Example Use Cases

- Compare and extract insights from multiple financial blogs.  
- Analyze academic papers for key findings and referenced studies.  
- Summarize lengthy market reports and identify core trends.  
- Ask follow-up questions and dive deeper into research content.

---

## 💡 Future Improvements

- PDF and YouTube transcript support  
- Add file upload for offline documents  
- Save chat history and provide downloadable summaries  
- Deploy on Streamlit Cloud or Hugging Face Spaces  

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT License](LICENSE)

---

## 🌟 Show Your Support

If you found this project useful, please ⭐ the repo and share it!
