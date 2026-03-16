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
            "source": doc.metadata.get("source"),
            "section": doc.metadata.get("section")
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
    你是一位学术论文阅读助手，帮助用户理解论文内容。

    回答问题时请遵循以下原则：

    1. 使用严谨、学术化的表达
    2. 如果问题涉及方法，请解释核心思想
    3. 如果涉及实验，请说明实验目的与结果
    4. 如果涉及论文贡献，请总结关键创新点

    论文上下文：
    {context}

    历史对话：
    {history_text}

    用户问题：
    {query}

    请用中文回答，并尽量结构化表达。
    """

    llm = ChatOpenAI(temperature=0)

    response = llm.invoke(prompt)

    answer = response.content

    return answer, retrieved_chunks