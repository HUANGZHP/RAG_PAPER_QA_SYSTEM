#   使用 BGE embedding
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_embedding():

    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en"
    )

    return embedding