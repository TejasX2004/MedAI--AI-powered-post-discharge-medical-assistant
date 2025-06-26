# 🏥 MedAI — Post-Discharge Virtual Health Assistant

**MedAI** is an intelligent, multi-agent application that assists patients post-discharge. It provides tailored summaries of discharge instructions, answers health-related questions using a Retrieval-Augmented Generation (RAG) pipeline, and integrates fallback web search for broader support.

---

## 📌 Features

* 🔹 Patient report retrieval using name matching
* 🔹 Summarized discharge instructions and medications
* 🔹 Clinical Q\&A using LLMs + FAISS vector database
* 🔹 Fallback web search integration (e.g., DuckDuckGo or Bing)
* 🔹 Logging of all interactions and queries
* 🔹 Multi-agent system (Receptionist + Clinical Assistant)
* 🔹 Built-in support for local LLMs like `mistral` via Ollama

---

## 🧱 Project Structure

```
medai/
├── app/
│   └── interface.py            # Streamlit app entry point
├── agents/
│   ├── receptionist_agent.py   # Handles patient name and summary
│   └── clinical_agent.py       # Handles medical questions via RAG
├── rag/
│   └── rag_utils.py            # FAISS vectorstore utils
├── tools/
│   ├── web_search.py           # Web fallback function
│   └── patient_lookup.py       # Load and filter patient data
├── data/
│   └── patients.json           # Sample patient discharge data
├── logs/
│   └── *.log                   # Query and interaction logs
├── .gitattributes              # Git LFS tracked files
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ▶️ Application Diagram

```text
           ┌────────────┐
           │  Streamlit │
           └─────┬──────┘
                 │
         User Input (Name / Query)
                 │
        ┌────────▼────────┐
        │ ReceptionistAgent│◄──── Patient Lookup (JSON)
        └────────┬────────┘
                 │
        Patient Match Found?
                 │Yes
                 ▼
    ┌───────────────────────────┐
    │ Summary + Query Interface│
    └────────────┬─────────────┘
                 ▼
        ┌────────▼────────┐
        │ ClinicalAgent   │
        └────────┬────────┘
                 ▼
          Vectorstore (FAISS)
                 │
     RAG via LangChain + LLM (Mistral/Ollama)
                 ▼
      Web Search Fallback (if needed)
                 ▼
           Final Answer to UI
```

---

## ⚙️ Architecture Justification

### 🧠 LLM Selection

* **Mistral via Ollama**: Chosen for local, performant inference. Great for offline use and reduced API costs.
* Fallback to **OpenAI Chat Models** possible by changing the config.

### 📚 Vector Database

* **FAISS** provides in-memory, efficient similarity search.
* Embeddings built from patient discharge instructions.

### 🔁 RAG Implementation

* Uses LangChain's `load_qa_with_sources_chain`.
* Allows contextual answer generation backed by retrieved docs.

### 🤖 Multi-Agent Design

* **ReceptionistAgent**: Manages user input, patient retrieval, and summary display.
* **ClinicalAgent**: Answers queries with RAG and handles web fallback.

### 🌐 Web Search Integration

* When LLM + RAG fails or lacks context, the query is routed to a web search utility.
* Returns top web result and source URL.

### 📂 Patient Data Retrieval

* Uses `lookup_patient_by_name()` to match user input with structured data.
* Handles fuzzy matching and multiple patients.

### 🪵 Logging System

* Logs stored in `/logs/` directory.
* ClinicalAgent logs queries + answers.
* Receptionist logs patient selection.

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/medai.git
cd medai
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# OR
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app/interface.py
```

Then open `http://localhost:8501` in your browser.

---

## 🛡 Disclaimers

* This project is a **prototype** and **not meant for real-world clinical use**.
* All health advice should be validated by licensed practitioners.

---
