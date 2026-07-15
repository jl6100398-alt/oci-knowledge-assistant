from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "db",
    embeddings,
    allow_dangerous_deserialization=True
)

query = "¿Qué es una VCN?"

docs = db.similarity_search(query, k=3)

print("\nResultados encontrados:\n")

for i, doc in enumerate(docs, start=1):
    print(f"Resultado {i}")
    print("-" * 60)
    print(doc.page_content)
    print("\nFuente:", doc.metadata)
    print()