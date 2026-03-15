# 📚 论文智能问答系统（RAG）

一个基于 **RAG（Retrieval-Augmented Generation）** 的论文问答系统。
用户可以上传论文 PDF，系统会自动构建知识库，并利用大语言模型回答关于论文内容的问题。

该项目展示了一个完整的 **RAG 应用流程**：文档加载 → 文本切分 → 向量检索 → Reranker排序 → 大模型生成回答。

---

# 🚀 功能介绍

本项目实现了以下功能：

📄 **PDF论文上传**
用户可以直接上传论文 PDF 文件。

🧠 **自动构建知识库**
系统会自动对论文进行文本切分并生成向量数据库。

🔎 **语义检索**
当用户提出问题时，系统会在论文中检索最相关的段落。

📊 **Reranker排序**
使用交叉编码器对检索结果进行重新排序，提高检索质量。

🤖 **大模型生成回答**
将检索到的论文内容作为上下文输入给大语言模型生成答案。

💬 **多轮对话记忆**
系统支持聊天式问答，可以记住之前的对话内容。

📑 **引用论文原文段落**
系统会展示回答所参考的论文段落来源。

---

# 🛠️ 使用方法

## 1️⃣ 安装依赖

在项目目录中运行：

```
pip install -r requirements.txt
```

---

## 2️⃣ 启动系统

运行：

```
streamlit run app.py
```

浏览器访问：

```
http://localhost:8501
```

---

## 3️⃣ 使用步骤

1️⃣ 上传论文 PDF 文件

2️⃣ 点击 **构建知识库**

3️⃣ 在聊天框输入问题

4️⃣ 系统会返回答案并展示相关论文段落

---

# 💡 示例

用户提问：

```
RAG 是什么？
```

系统回答示例：

```
RAG（Retrieval-Augmented Generation）是一种结合信息检索与语言模型生成能力的方法。
系统首先从知识库中检索相关内容，然后将这些内容作为上下文输入给语言模型，
从而生成更加准确、可靠的回答。
```

系统同时会显示：

```
参考论文段落：
RAG combines retrieval and generation to improve factual grounding...
```

---

# 📂 项目结构

```
rag-paper-qa-system
│
├── data/                  # 存放上传的论文PDF
│
├── src/
│   ├── loader.py          # PDF加载
│   ├── splitter.py        # 文本切分
│   ├── embedding.py       # 向量化模型
│   ├── vector_db.py       # 向量数据库
│   ├── retriever.py       # 语义检索
│   ├── reranker.py        # Reranker排序
│   └── rag_pipeline.py    # RAG核心流程
│
├── chroma_db/             # 向量数据库
├── app.py                 # Web应用入口
├── requirements.txt       # 项目依赖
└── README.md
```

---

# 🧩 各个文件的作用

### app.py

系统入口文件，负责启动 Streamlit Web 界面，实现用户交互，例如上传论文、输入问题和展示回答。

---

### loader.py

负责加载论文 PDF 文件，并将其转换为可处理的文本内容。

---

### splitter.py

将论文文本切分为多个较小的文本块（chunk），方便后续向量化和检索。

---

### embedding.py

加载向量化模型，将文本转换为向量表示（Embedding）。

---

### vector_db.py

创建和加载向量数据库（Chroma），用于存储论文文本的向量。

---

### retriever.py

根据用户问题在向量数据库中进行语义检索，找到最相关的文本段落。

---

### reranker.py

使用 Reranker 模型对检索到的文本进行重新排序，从而提高检索质量。

---

### rag_pipeline.py

RAG 系统核心逻辑，包括：

* 调用检索模块
* 使用 Reranker排序
* 构建上下文
* 调用大语言模型生成最终回答

---

# 🧰 技术栈

* Python
* LangChain
* Chroma 向量数据库
* Sentence Transformers
* Streamlit
* OpenAI API

---

# 📌 项目用途

该项目适合用于：

* 学习 **RAG系统实现流程**
* 作为 **大模型应用开发实践项目**
* 构建自己的论文问答助手
