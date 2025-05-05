# sony-zv1-camera-assistant
Local chatbot that answers questions about the Sony ZV-1 camera manual using Python, FAISS, and a local LLM (via Ollama).

# 📷 Sony ZV-1 Manual Assistant (Vibe Code Edition)

This is a fully local AI assistant that answers questions about the Sony ZV-1 camera using its official PDF manual.

I built this as a **Vibe Code** challenge — coding fast, with minimal setup, to prove how powerful open-source tools can be when combined simply. This assistant can easily be adapted to **any camera** or **any long document** by just changing the PDF and adjusting the input accordingly.

---

## 🔍 What It Does

- Extracts text from the PDF manual
- Chunks the text into readable parts
- Embeds those chunks using sentence-transformers
- Stores them in a FAISS vector index
- Uses **semantic search** to retrieve relevant info based on your question
- Generates a helpful natural-language answer using a **local LLM via Ollama**

---

## 🛠️ Technologies Used

All components are **100% open source**:

- `Python 3.x`
- [`PyMuPDF`](https://pymupdf.readthedocs.io/en/latest/) – PDF text extraction
- [`SentenceTransformers`](https://www.sbert.net/) – Embedding model (`all-MiniLM-L6-v2`)
- [`FAISS`](https://github.com/facebookresearch/faiss) – Vector search engine
- [`Ollama`](https://ollama.com) – Local LLM serving
- Local LLMs like `mistral`, `llama2`, or `gemma` (open-source — huge thanks to [Mistral AI](https://mistral.ai) and other contributors 💙)

---

## 💡 Adapting It to Other Devices

Just swap the PDF in the `data/` folder and adjust the chunking script. You can turn this into a local assistant for:
- Other cameras
- Smartphones
- Software user manuals
- Game rulebooks... anything long and hard to Ctrl+F

---

## ⚙️ Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
