from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class TraditionalRAG:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None

    def create_embeddings(self, text_chunks):
        """Create embeddings for text chunks and store them in FAISS."""
        embeddings = self.model.encode(text_chunks, convert_to_tensor=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1]) 
        self.index.add(np.array(embeddings))
        return embeddings

    def query(self, query_text, text_chunks, top_k=5):
        """Retrieve the most similar chunks for a given query."""
        query_embedding = self.model.encode([query_text], convert_to_tensor=False)
        _, indices = self.index.search(np.array(query_embedding), top_k)
        return [text_chunks[i] for i in indices[0]]

