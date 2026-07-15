from langchain_community.document_loaders import (
    PyPDFDirectoryLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def load_documents():

    loader = PyPDFDirectoryLoader("data")

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    )

    chunks = splitter.split_documents(documents)

    print(f"Documentos: {len(documents)}")
    print(f"Chunks: {len(chunks)}")

    return chunks