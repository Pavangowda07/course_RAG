import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = joblib.load('embedding_df.joblib')

# -----------------------------
# Functions (reuse your code)
# -----------------------------

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return r.json()["embeddings"]

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    })
    return r.json()["response"]

# -----------------------------
# UI
# -----------------------------

st.set_page_config(page_title="CourseRAG", layout="wide")

st.title("🎓 CourseRAG Assistant")
st.write("Ask questions from your video course!")

query = st.text_input("💬 Ask your question:")

if st.button("Search") and query:

    with st.spinner("🔍 Searching..."):
        question_embedding = create_embedding([query])[0]

        similarities = cosine_similarity(
            np.vstack(df['embedding']),
            [question_embedding]
        ).flatten()

        top_k = 5
        indices = similarities.argsort()[::-1][:top_k]

        results = df.loc[indices]

        context = results[["title", "number", "start", "end", "text"]].to_json(orient="records")

        prompt = f"""
        You are a helpful assistant.
        Here I am teaching web development in my Sigma web development course. 
        You are given video chunks with:
        - video title
        - video number
        - start time (in seconds)
        - end time (in seconds)
        - transcript text

        Context:
        {context}

        Question:
        {query}
        User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp in minutes) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course.
        Instructions:
        - Answer in a clear and human-friendly way
        - Recommend which video the user should watch
        - ALWAYS convert timestamps from seconds into **minutes:seconds format (mm:ss)** like YouTube
        - Example: 160 seconds → 2:40
        - Mention time ranges like: 2:40 - 2:45
        - Do NOT show raw seconds
        - Do NOT mention the JSON format
        - If unrelated, say you only answer course-related questions

        Answer clearly. Mention video name and timestamps.
        """

        answer = inference(prompt)

    # -----------------------------
    # Display Results
    # -----------------------------
    st.subheader("📌 Answer")
    st.write(answer)

    st.subheader("🎥 Relevant Sections")

    for _, row in results.iterrows():
        st.markdown(f"""
        **📺 Video {row['number']} - {row['title']}**
        ⏱ {round(row['start']/60,2)} min → {round(row['end']/60,2)} min  
        📖 {row['text'][:150]}...
        """)