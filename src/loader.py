from langchain_community.document_loaders import PyPDFLoader
from src.paper_structure import detect_section
import os


def load_documents():

    docs = []

    for file in os.listdir("data"):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(os.path.join("data", file))

            pages = loader.load()

            for page in pages:

                section = detect_section(page.page_content)

                page.metadata["section"] = section

                docs.append(page)

    return docs