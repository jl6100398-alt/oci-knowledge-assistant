from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


class VectorStoreManager:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = FAISS.load_local(
            "db",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def search(self, question, k=3):

        return self.db.similarity_search(
            question,
            k=k
        )