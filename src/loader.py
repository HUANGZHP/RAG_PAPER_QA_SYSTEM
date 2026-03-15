import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_path="data"):

    documents = []

    for file in os.listdir(data_path):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(os.path.join(data_path, file))

            docs = loader.load()

            for d in docs:
                d.metadata["source"] = file

            documents.extend(docs)

    return documents