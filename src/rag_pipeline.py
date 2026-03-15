from langchain_openai import ChatOpenAI

from src.retriever import retrieve_documents
from src.reranker import rerank


def generate_answer(query, vectordb, chat_history):

    docs = retrieve_documents(vectordb, query, k=6)

    docs = rerank(query, docs, top_k=3)

    context = ""

    retrieved_chunks = []

    for doc in docs:

        context += doc.page_content + "\n"

        retrieved_chunks.append({
            "text": doc.page_content,
            "source": doc.metadata.get("source")
        })

    history_text = ""

    for message in chat_history:
        role = message["role"]
        content = message["content"]

        if role == "user":
            history_text += f"用户: {content}\n"
        else:
            history_text += f"助手: {content}\n"

    prompt = f"""
你是一个论文阅读助手。

以下是之前的对话记录：
{history_text}

请根据论文内容回答用户的问题。

论文内容：
{context}

当前问题：
{query}

请用中文回答。
"""

    llm = ChatOpenAI(temperature=0)

    response = llm.invoke(prompt)

    answer = response.content

    return answer, retrieved_chunks