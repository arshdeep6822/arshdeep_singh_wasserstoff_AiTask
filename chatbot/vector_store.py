## WE WILL INITIALISE A FAISS VECTOR STORE THAT WILL STORE OUR TEXT WE RETRIEVED FROM THE WEBSITE ##
## THE VECTOR STORE WILL BE USED TO SEARCH FOR SIMILAR POSTS WHEN THE USER ASKS A QUESTION ##


import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List


class VectorStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.sentence_transformer = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(self.sentence_transformer.get_sentence_embedding_dimension())
        self.corpus = []

    def add_texts(self, texts: List[str]):
        """Add texts to the vector store"""
        self.corpus.extend(texts)
        for text in texts:
            embedding = self.sentence_transformer.encode(text).astype('float32')
            self.index.add(np.array([embedding]))

    def search(self, query: str, top_k: int = 3) -> List[str]:
        """Search for relevant texts"""
        query_embedding = self.sentence_transformer.encode([query])[0]
        distances, indices = self.index.search(
            np.array([query_embedding], dtype=np.float32), 
            top_k
        )
        return [self.corpus[idx] for idx in indices[0]]