import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

class DocumentAssistant:    
    def __init__(self):
        # 1. Initialize the Embedding model
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # 2. Initialize the Local LLM
        # Ensure Ollama is running qwen2.5 on your machine
        self.llm = OllamaLLM(model="qwen2.5") 
        
        self.persist_directory = "./chroma_db"
        
        # 3. Load or Create the Vector Database
        try:
            # We check if the directory exists first to avoid unnecessary errors
            if os.path.exists(self.persist_directory):
                self.vector_db = Chroma(
                    persist_directory=self.persist_directory, 
                    embedding_function=self.embeddings
                )
                print("Successfully loaded existing database.")
            else:
                self.vector_db = None
                print("No existing database found.")
        except Exception as e:
            self.vector_db = None
            print(f"Error loading database: {e}")

    def ingest_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        
        # Chunking strategy: 1000 chars with 100 overlap helps maintain context
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(pages)

        if self.vector_db is None:
            self.vector_db = Chroma.from_documents(
                documents=chunks, 
                embedding=self.embeddings, 
                persist_directory=self.persist_directory
            )
        else:
            self.vector_db.add_documents(chunks)
        
        return len(chunks)
    
    def ask_question(self, question):
        # Safely return a tuple to prevent 'too many values to unpack' in streamlit
        if not self.vector_db:
            return "I have no memory! Please upload a document first.", set()

        # 1. Define the "System Prompt"
        system_prompt = (
            "You are an expert Real Estate Assistant in Pakistan. "
            "Use the provided context to answer the user's question about the property document. "
            "If the answer isn't in the context, say you don't know—don't hallucinate. "
            "Be concise and professional. Use bullet points for summaries."
            "\n\n"
            "{context}"
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        # 2. Create the "Stuff" chain
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)

        # 3. Create the final Retrieval Chain
        # Increasing k=5 gives the AI more context for better summaries
        retriever = self.vector_db.as_retriever(search_kwargs={"k": 5})
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        
        # 4. Invoke the chain
        response = rag_chain.invoke({"input": question})
        
        # Extract page numbers from metadata
        sources = [doc.metadata.get("page", "N/A") for doc in response["context"]]
        
        # Terminal Debugging
        print(f"\n--- Debug: Processing Question: {question} ---")
        for i, doc in enumerate(response["context"]):
            print(f"Chunk {i} (Page {doc.metadata.get('page')}): {doc.page_content[:100]}...")

        return response["answer"], set(sources)