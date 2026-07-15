from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from src.loader import load_documents


def create_vectorstore():

    print("\nCargando documentos...")

    documents = load_documents()

    print("\nCreando embeddings...")

    embeddings = HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )

    print("\nGenerando base vectorial...")

    vectorstore = FAISS.from_documents(

        documents,

        embeddings

    )

    vectorstore.save_local("db")

    print("\nBase vectorial creada correctamente.")


if __name__ == "__main__":

    create_vectorstore()