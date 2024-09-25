import time
from traditional_rag import TraditionalRAG
from neo4j_rag import Neo4jRAG
from pdf_processing import extract_text_from_pdf, chunk_text

# Initialize models
traditional_rag = TraditionalRAG()
neo4j_rag = Neo4jRAG(uri="url_here", user="neo4j", password="password")

def compare_query_times(query_text, chunks):
    # Traditional RAG Query
    start_trad = time.time()
    traditional_rag.query(query_text, chunks)
    end_trad = time.time()
    
    # Neo4j RAG Query
    start_neo = time.time()
    neo4j_rag.query(query_text)
    end_neo = time.time()

    # Print results
    print(f"Traditional RAG Query Time: {end_trad - start_trad:.2f} seconds")
    print(f"Neo4j RAG Query Time: {end_neo - start_neo:.2f} seconds")

# Sample PDF processing
pdf_text = extract_text_from_pdf("sample.pdf")
chunks = list(chunk_text(pdf_text))

# Sample Query
compare_query_times("Your sample query here", chunks)
