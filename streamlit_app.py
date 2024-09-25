import streamlit as st
from pdf_processing import extract_text_from_pdf, chunk_text
from traditional_rag import TraditionalRAG
from neo4j_rag import Neo4jRAG
import time

# Initialize models
traditional_rag = TraditionalRAG()
# Use Neo4j Aura connection
neo4j_rag = Neo4jRAG(uri="url_here", user="neo4j", password="passowrd")

# PDF Handling
st.title("Chat with PDF using RAG")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.write("Processing PDF...")

    pdf_text = extract_text_from_pdf(uploaded_file)
    chunks = list(chunk_text(pdf_text))

    # Option to choose between approaches
    approach = st.radio("Choose the RAG approach", ("Traditional RAG", "Neo4j RAG"))

    # Create embeddings based on selected approach
    if approach == "Traditional RAG":
        traditional_rag.create_embeddings(chunks)
        st.write("Embeddings created for Traditional RAG.")
    else:
        neo4j_rag.create_embeddings(chunks)
        st.write("Embeddings created for Neo4j RAG.")

    # Query Input
    query_text = st.text_input("Enter your query")

    if query_text:
        start_time = time.time()

        if approach == "Traditional RAG":
            result = traditional_rag.query(query_text, chunks)
        else:
            result = neo4j_rag.query(query_text)

        end_time = time.time()
        st.write("Response:")
        st.write(result)
        st.write(f"Query time: {end_time - start_time:.2f} seconds")
