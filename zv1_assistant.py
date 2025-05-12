import fitz  # PyMuPDF
import os
import json
import re
import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer
from tqdm import tqdm



def load_index(index_path):
    return faiss.read_index(index_path)


def load_metadata(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_prompt(question, retrieved_chunks):
    context = "\n\n".join([
        f"[Page {chunk['page']}] {chunk['text']}" for chunk in retrieved_chunks
    ])
    # prompt for the LLM, can be change optimize according to the need
    prompt = f"""You are a helpful assistant answering based on the Sony ZV-1 camera manual.

Use the following manual content to answer the user's question as clearly and accurately as possible.

Manual Content:
{context}

Question: {question}
Answer:"""

    return prompt

# api query with the prompt and the model to the mistral from ollama
def query_ollama(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error querying Ollama: {e}"


# main function that call the different functions and answer accordingly
def ask(question, index, metadata, embedding_model, llm_model_name="mistral", top_k=3):

    # Step 1: Embed query
    query_embedding = embedding_model.encode([question]).astype("float32")

    # Step 2: Search FAISS
    distances, indices = index.search(query_embedding, top_k)
    retrieved_chunks = [metadata[idx] for idx in indices[0]]

    # Step 3: Build prompt
    prompt = build_prompt(question, retrieved_chunks)

    # Step 4: Get answer from LLM
    answer = query_ollama(prompt, model=llm_model_name)

    # Step 5: Print everything
    print("\n🔍 Retrieved chunks:")
    for i, chunk in enumerate(retrieved_chunks):
        print(f"\n[Page {chunk['page']}] (score: {distances[0][i]:.2f})")
        print(chunk['text'])

    print("\n🤖 LLM Answer:")
    print(answer)
    return answer

# function to in
def setup_assistant():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    index = load_index("zv1_faiss.index")
    metadata = load_metadata("zv1_metadata.json")
    return index, model, metadata

# # what we need to ask a question to our gpt and get a response
# query = "how to have shoot a video in manual mode?"
# ask(query, index, metadata, model)
