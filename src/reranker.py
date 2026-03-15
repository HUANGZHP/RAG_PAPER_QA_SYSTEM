from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs, top_k=3):

    pairs = []

    for doc in docs:
        pairs.append((query, doc.page_content))

    scores = model.predict(pairs)

    scored_docs = list(zip(scores, docs))

    scored_docs.sort(key=lambda x: x[0], reverse=True)

    return [doc for _, doc in scored_docs[:top_k]]