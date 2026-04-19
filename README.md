# 🎓 CourseRAG: RAG-Based Video Course Assistant

CourseRAG is an end-to-end **Retrieval-Augmented Generation (RAG)** system that enables users to ask questions about video-based courses and receive **context-aware answers with timestamps and video references**.

---

## 🚀 Features

* 🎥 Converts course videos into searchable knowledge
* 🎧 Extracts audio from videos using FFmpeg
* 📝 Transcribes audio using Whisper
* 🧹 Smart chunking for better retrieval
* 🧠 Semantic search using embeddings (bge-m3 via Ollama)
* 🔍 Retrieves most relevant video segments
* 🤖 Generates human-like answers using LLM (LLaMA3)
* ⏱ Provides **YouTube-style timestamps (mm:ss)**
* 🌐 Interactive UI using Streamlit

---

## 🧠 How It Works

```
Videos → Audio → Transcription → Chunking → Embeddings → Vector Store
                                                           ↓
User Query → Embedding → Similarity Search → Context → LLM → Answer
```

---

## 📂 Project Structure

```
course_RAG/
│
├── videos/                # Input course videos
├── audios/                # Extracted audio files
├── jsons/                 # Raw transcripts (Whisper output)
├── newjsons/              # Processed & merged chunks
├── embedding_df.joblib    # Stored embeddings (vector DB)
│
├── mp4_to_mp3.py          # Convert videos to audio
├── mp3_to_jsons.py        # Transcribe audio → JSON
├── merging_chunks.py      # Merge chunks for better context
├── jsons_to_embeddings.py # Generate embeddings
├── embeddings_to_response.py # Query → Answer pipeline
│
├── app.py                 # Streamlit UI
├── prompt.txt             # Debugging prompt
├── response.txt           # Output response
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/courseRAG.git
cd courseRAG
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install FFmpeg

Make sure FFmpeg is installed and added to PATH:

```bash
ffmpeg -version
```

---

### 4. Setup Ollama

Install Ollama and pull required models:

```bash
ollama pull bge-m3
ollama pull llama3.2:3b
```

---

## ▶️ Usage

### Step 1: Convert Videos to Audio

```bash
python mp4_to_mp3.py
```

---

### Step 2: Transcribe Audio

```bash
python mp3_to_jsons.py
```

---

### Step 3: Merge Chunks

```bash
python merging_chunks.py
```

---

### Step 4: Generate Embeddings

```bash
python jsons_to_embeddings.py
```

---

### Step 5: Run Query System

```bash
python embeddings_to_response.py
```

---

### Step 6: Run UI

```bash
streamlit run app.py
```

---

## 💡 Example Output

```
To learn about the HTML <img> tag, refer to:

📺 Video 5 - Image, Lists, and Tables in HTML  
⏱ 2:40 – 2:45  

This section explains how images are embedded in web pages using the <img> tag.
```

## ⏳ Performance Note (Transcription Time)

⚠️ **Important:** The transcription step (`mp3_to_jsons.py`) can take a significant amount of time depending on your system specifications.

* Using models like **Whisper large-v2** is **computationally intensive**
* On CPU, transcription can be **very slow (real-time or slower)**
* Performance improves significantly with a **GPU**

### 🚀 Recommendations

* ✅ Use a system with a **dedicated GPU** for faster processing
* ✅ Rent a GPU from cloud providers (e.g., Google Colab, AWS, Paperspace)
* ✅ Alternatively, use **Whisper APIs** for faster and scalable transcription

This step is a **one-time preprocessing cost**, after which the system runs efficiently for querying.


---

## 🧪 Tech Stack

* Python
* Streamlit
* Whisper (Speech-to-Text)
* Ollama (Local LLM + Embeddings)
* bge-m3 (Embedding model)
* LLaMA3 (LLM)
* Pandas & NumPy
* Scikit-learn (Cosine Similarity)

---

## ⚠️ Limitations

* Requires local Ollama setup (not cloud-ready by default)
* Performance depends on hardware (Whisper + LLM)
* Basic vector storage (uses Pandas instead of FAISS/Chroma)

---

## 🚀 Future Improvements

* ✅ Deployable backend (FastAPI + cloud hosting)
* ✅ Vector DB (FAISS / ChromaDB)
* ✅ Chat memory for follow-up questions
* ✅ Video playback with timestamp jumping
* ✅ Hybrid search (semantic + keyword)
* ✅ Multi-course support

---

## 📌 Key Learnings

* Built RAG pipeline from scratch (no frameworks)
* Understood embeddings & semantic search deeply
* Learned prompt engineering & hallucination control
* Implemented end-to-end AI system design

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* OpenAI Whisper
* Ollama
* HuggingFace (bge models)
* Streamlit

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

---
