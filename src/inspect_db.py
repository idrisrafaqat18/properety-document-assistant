import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 1. Point to your existing database
persist_directory = "./chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Load the collection
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# 3. Get the data
data = db.get() 

print(f"--- Database Inspection ---")
print(f"Total Chunks Stored: {len(data['ids'])}")

if len(data['ids']) > 0:
    print(f"First Chunk Preview: {data['documents'][0][:100]}...")
    print(f"Metadata Example: {data['metadatas'][0]}")
else:
    print("❌ The database is empty.")