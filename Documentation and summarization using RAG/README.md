# 📄 **Document Search and Summarization using RAG**

---

## 🧠 **Overview**
This project implements a **Retrieval-Augmented Generation (RAG)** system for **document search and summarization** using **Large Language Models (LLMs)**.  
The system retrieves relevant documents from a text corpus using **semantic search** and generates **concise summaries** based on user queries.

The solution is built using **Hugging Face models**, **FAISS** for vector similarity search, and a **Gradio** user interface.  
The entire pipeline is designed to run in **Google Colab**.

---

## 🎯 **Objective**
The objective of this project is to design a system that can:
- 🔍 Efficiently search large text corpora  
- 📝 Generate coherent and meaningful summaries  
- 🤖 Utilize modern Large Language Models  

This implementation strictly follows the **assignment requirements**.

---

## 📚 **Dataset**
- **📌 Dataset Name:** AG News  
- **🌐 Source:** Hugging Face Datasets  
- **📰 Description:** A public dataset containing news articles across categories such as **World, Sports, Business, and Technology**  
- **⚠️ Note:** The dataset is **automatically downloaded** during execution.  
  ➜ **No manual dataset is required**

---

## 🛠️ **Models and Tools Used**
- **🔗 Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`  
- **🧠 Summarization Model:** `facebook/bart-large-cnn`  
- **🗂️ Vector Store:** FAISS  
- **🖥️ User Interface:** Gradio  
- **📊 Evaluation Metrics:** ROUGE (ROUGE-1, ROUGE-2, ROUGE-L)

---

## 🔄 **Methodology**
1. 📥 Load and preprocess text data from the AG News dataset  
2. 🧮 Generate dense vector embeddings for each document  
3. ⚡ Index embeddings using **FAISS** for fast similarity search  
4. ❓ Accept user queries and retrieve the **Top-K relevant documents**  
5. ✍️ Generate summaries using a transformer-based summarization model  
6. 📈 Evaluate retrieval and summarization performance  

---

## 📊 **Evaluation**
- **🔍 Search Evaluation:**  
  Top-K retrieval accuracy is measured by checking whether the original document appears among the retrieved results.
  
- **📝 Summarization Evaluation:**  
  Summary quality is evaluated using **ROUGE metrics**, measuring overlap between generated summaries and reference text segments.

---

## 🖥️ **User Interface**
A **Gradio-based web interface** allows users to:
- 🗣️ Enter information-seeking queries  
- 🔢 Adjust the number of retrieved documents (Top-K)  
- 📏 Control the summary length  
- 📄 View retrieved documents and generated summaries interactively  

---

## 🚀 **How to Run (Google Colab)**
1. 📂 Open the provided notebook in **Google Colab**  
2. ▶️ Run all cells sequentially  
3. ⬇️ The dataset will be downloaded automatically  
4. 🌐 Launch the Gradio interface  
5. 🔎 Enter a query related to the news articles and view results  

---

## 📦 **Requirements**
- 🐍 Python 3.8 or above  
- torch  
- transformers  
- sentence-transformers  
- datasets  
- faiss-cpu  
- gradio  
- evaluate  
- rouge-score  

---

## 💬 **Example Queries**
- “Summarize recent technology news”  
- “What is this article about?”  
- “Give key points from the retrieved document”  

---

## ⚠️ **Challenges and Solutions**
- **Challenge:** Handling short documents during summarization  
  **✅ Solution:** Dynamic adjustment of summary length based on input size  

- **Challenge:** Efficient retrieval from large document collections  
  **✅ Solution:** Use of FAISS for fast and scalable vector similarity search  

---

## ✅ **Conclusion**
This project demonstrates an **effective and scalable** approach to document retrieval and summarization using modern NLP techniques.  
By combining **semantic search** with **Large Language Models**, the system provides accurate and meaningful summaries while maintaining efficiency and usability.

---
