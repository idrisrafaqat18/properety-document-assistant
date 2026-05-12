import streamlit as st
from rag_engine import DocumentAssistant
import os

st.set_page_config(page_title="Document AI", page_icon="📄")

# Initialize the assistant in session state
if 'assistant' not in st.session_state:
    st.session_state.assistant = DocumentAssistant()

st.title("📄 Smart Document Assistant")
st.write("Upload a PDF and ask questions about its content.")

# 1. File Upload
uploaded_file = st.file_uploader("Upload Property Document", type="pdf")

if uploaded_file:
    # Save temp file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Analyzing document..."):
        st.session_state.assistant.ingest_pdf("temp.pdf")
    st.success("Document ready for questions!")

# 2. Chat Interface
question = st.text_input("What would you like to know from this document?")

if question:
    with st.spinner("Thinking..."):
        # The engine returns (answer, sources)
        result = st.session_state.assistant.ask_question(question)
        
        # Safe unpacking to prevent ValueError
        if isinstance(result, tuple) and len(result) == 2:
            answer, sources = result
            st.markdown(f"### Answer")
            st.write(answer)
            
            if sources:
                # Clean up source display
                clean_sources = ", ".join(map(str, sorted(sources)))
                st.info(f"🔍 **Sources verified from:** Pages {clean_sources}")
        else:
            # Fallback if an error string is returned
            st.error(result)

# 3. Sidebar Status
with st.sidebar:
    st.header("Storage Status")
    if st.session_state.assistant.vector_db:
        db_content = st.session_state.assistant.vector_db.get()
        count = len(db_content['ids'])
        st.success(f"Database contains {count} chunks.")
    else:
        st.warning("Database is currently empty.")