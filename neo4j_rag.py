from py2neo import Graph
from sentence_transformers import SentenceTransformer
import numpy as np

from py2neo import Graph

class Neo4jRAG:
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, auth=(user, password))

    def create_embeddings(self, chunks):
        """Create embeddings and store them in Neo4j Aura."""
        for chunk in chunks:
            query = """
            MERGE (d:Document {content: $content})
            """
            self.graph.run(query, content=chunk)

    def query(self, question):
        """Query Neo4j Aura for the relevant chunk."""
        cypher_query = """
        MATCH (d:Document)
        WHERE d.content CONTAINS $question
        RETURN d.content LIMIT 1
        """
        result = self.graph.run(cypher_query, question=question)
        
        # 'evaluate' will return a single value (d.content)
        return result.evaluate() if result else "No relevant content found."

