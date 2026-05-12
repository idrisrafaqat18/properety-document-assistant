# 📄 Smart Property Document Assistant (Local RAG)

A specialized Retrieval-Augmented Generation (RAG) application engineered to analyze property and legal documents. This project leverages **fully local AI models** to ensure maximum data privacy, making it an ideal solution for sensitive real estate agreements and legal paperwork.

## 🚀 Key Features
- **100% Privacy-First:** Powered by **Ollama (Qwen 2.5)** and **HuggingFace Embeddings**. No document data ever leaves your local machine.
- **Persistent Vector Memory:** Uses **ChromaDB** to store document "chunks," allowing the AI to retain knowledge across multiple sessions.
- **Context-Aware Citations:** Automatically extracts page numbers from document metadata to verify every answer provided by the AI, minimizing hallucinations.
- **Expert Real Estate Persona:** Custom system prompts transform the LLM into a concise, professional assistant tailored for the Pakistani property market.
- **Database Auditing:** Includes specialized utility scripts to inspect and verify the data integrity of the vector store.

## 🛠️ Technical Stack
- **Language:** Python 3.10+
- **LLM:** Qwen 2.5 (Local via Ollama)
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2`[cite: 1]
- **Orchestration:** LangChain (Classic & Community)[cite: 1]
- **Vector Store:** ChromaDB[cite: 1]
- **Frontend:** Streamlit[cite: 1]


⚙️ Installation & Setup
1. Prerequisites

Install Ollama and pull the model:

ollama pull qwen2.5

2. Environment Setup

# Clone the repository
git clone [https://github.com/idrisrafaqat18/properety-document-assistant.git](https://github.com/idrisrafaqat18/properety-document-assistant.git)
cd properety-document-assistant

# Install required dependencies
pip install streamlit chromadb pypdf sentence-transformers langchain-community langchain-core langchain-ollama langchain-huggingface langchain-chroma

3. Run the Application

streamlit run src/rag_app.py

🔍 Engineering Highlights

    Smart Chunking Strategy: Utilizes RecursiveCharacterTextSplitter with 1000-character blocks and 100-character overlaps[cite: 1].

    Stateful Persistence: Implemented logic to detect existing databases on startup to prevent redundant embedding generation[cite: 1].

    Robust UI Interaction: Designed a safe interaction layer using tuple-based response handling to prevent runtime errors[cite: 1].

Developed by Idris Rafaqat Hussain

AI/ML Engineer focused on Agentic AI & Autonomous Local Systems

