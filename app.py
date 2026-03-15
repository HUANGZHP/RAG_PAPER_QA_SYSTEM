import streamlit as st
import os

from src.loader import load_documents
from src.splitter import split_documents
from src.embedding import load_embedding
from src.vector_db import create_vector_db, load_vector_db
from src.rag_pipeline import generate_answer


st.title("📚 论文智能问答系统 (RAG)")

st.write("上传论文PDF，然后提出问题。")


# 创建 data 文件夹
if not os.path.exists("data"):
    os.makedirs("data")


uploaded_files = st.file_uploader(
    "上传论文PDF",
    type="pdf",
    accept_multiple_files=True
)


if uploaded_files:

    for uploaded_file in uploaded_files:

        file_path = os.path.join("data", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

    st.success("PDF 上传成功")


if st.button("构建知识库"):

    docs = load_documents()

    chunks = split_documents(docs)

    embedding = load_embedding()

    create_vector_db(chunks, embedding)

    st.success("知识库构建完成")


# 聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


query = st.chat_input("请输入问题")


if query:

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    embedding = load_embedding()

    vectordb = load_vector_db(embedding)

    answer, chunks = generate_answer(query, vectordb, st.session_state.messages)

    with st.chat_message("assistant"):

        st.markdown(answer)

        st.markdown("### 参考论文段落")

        for c in chunks:

            st.markdown("**来源：** " + str(c["source"]))

            st.markdown(c["text"][:400])

            st.markdown("---")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })