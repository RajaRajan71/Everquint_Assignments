📘 Document Search and Summarization using RAG
Overview

This project implements a Retrieval-Augmented Generation (RAG) system for document search and summarization using Large Language Models. The system retrieves relevant documents from a text corpus using semantic search and generates concise summaries based on user queries.

The solution is built using Hugging Face models, FAISS for vector search, and a Gradio user interface. The entire pipeline runs in Google Colab.

Objective

The objective of this project is to efficiently search large textual datasets and generate coherent summaries using Large Language Models, as specified in the assignment requirements.

Dataset

Dataset Name: AG News

Source: Hugging Face Datasets

Description: A public dataset consisting of news articles from multiple categories such as World, Sports, Business, and Technology.

Note: The dataset is automatically downloaded during execution. No manual dataset is required.

Models and Tools Used

Embedding Model: sentence-transformers/all-MiniLM-L6-v2

Summarization Model: facebook/bart-large-cnn

Vector Database: FAISS

Interface: Gradio

Evaluation Metrics: ROUGE (ROUGE-1, ROUGE-2, ROUGE-L)

Methodology

Load and preprocess text data from the AG News dataset.

Generate dense vector embeddings for each document using a Sentence Transformer.

Index the embeddings using FAISS for efficient similarity-based retrieval.

Accept user queries and retrieve the top-K most relevant documents.

Generate summaries of retrieved documents using a transformer-based summarization model.

Evaluate the system using retrieval accuracy and ROUGE metrics.

Evaluation

Search Evaluation: Top-K accuracy is measured by checking whether the original document appears in the retrieved results for generated queries.

Summarization Evaluation: ROUGE metrics are used to measure overlap between generated summaries and reference text segments.

User Interface

A Gradio-based web interface allows users to:

Enter information-seeking queries related to the dataset

Select the number of documents to retrieve (Top-K)

Control the length of the generated summary

View retrieved documents and generated summaries interactively

How to Run (Google Colab)

Open the provided notebook in Google Colab.

Run all cells sequentially.

The dataset will be downloaded automatically.

Launch the Gradio interface.

Enter a query related to the news articles and view results.

Requirements

Python 3.8 or above

torch

transformers

sentence-transformers

datasets

faiss-cpu

gradio

evaluate

rouge-score

Example Queries

"Summarize recent technology news"

"What is this article about?"

"Give key points from the retrieved document"

Challenges and Solutions

Challenge: Handling short documents during summarization
Solution: Dynamic adjustment of summary length based on input size.

Challenge: Efficient retrieval from large text corpora
Solution: Use of FAISS for fast vector similarity search.

Conclusion

This project demonstrates an effective and scalable approach to document retrieval and summarization using modern NLP techniques. By combining semantic search with Large Language Models, the system provides accurate and meaningful summaries while maintaining efficiency and usability.
