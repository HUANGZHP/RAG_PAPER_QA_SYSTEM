from langchain_community.vectorstores import Chroma

def create_vector_db(chunks, embedding):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="vector_store"
    )

    vectordb.persist()

    return vectordb


def load_vector_db(embedding):

    vectordb = Chroma(
        persist_directory="vector_store",
        embedding_function=embedding
    )

    return vectordb