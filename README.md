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

    Prerequisites

        Install Ollama and pull the model:
        Bash

        ollama pull qwen2.5

    Environment Setup
    Bash

    # Clone the repository
    git clone https://github.com/idrisrafaqat18/properety-document-assistant.git
    cd property-document-assistant

    # Install required dependencies
    pip install -r requirements.txt


3. **Run the Application**
   ```bash
   streamlit run src/rag_app.py
   

🔍 Engineering Highlights

    Smart Chunking Strategy: Utilizes RecursiveCharacterTextSplitter with 1000-character blocks and 100-character overlaps to maintain semantic context across paragraph breaks.

    Stateful Persistence: Implemented logic to detect existing databases on startup, preventing redundant embedding generation and optimizing computation time.

    Robust UI Interaction: Designed a safe interaction layer between the engine and frontend using tuple-based response handling to prevent runtime unpacking errors.

Developed by Idris Rafaqat Hussain

AI/ML Engineer focused on Agentic AI & Autonomous Local Systems

