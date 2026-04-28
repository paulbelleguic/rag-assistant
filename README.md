# Academic RAG Assistant

Academic RAG Assistant is a portfolio project focused on building an academic AI assistant for course materials. The application lets users upload `.pdf` or `.txt` documents, index them locally, ask natural language questions, and generate short summaries grounded in the uploaded content.

## Project Goal

Build an end-to-end RAG application that covers:

- document loading
- text extraction
- chunking
- embeddings
- vector search with FAISS
- answer generation
- Streamlit interface

The current version is designed for academic usage: course PDFs, lecture notes, study documents, and revision material.

## Current Features

- Upload and index a `.pdf` or `.txt` document
- Ask questions about the uploaded document
- Generate a short document summary
- Display retrieved sources
- Display relevant passages with similarity scores
- Re-rank retrieved passages with a simple keyword-based heuristic
- Use a fallback answer strategy when the local model output is weak

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face embeddings
- Transformers
- PyPDF

## How It Works

1. The user uploads a document.
2. The document is loaded and converted into LangChain `Document` objects.
3. The text is split into chunks.
4. Chunks are embedded with a local Hugging Face model.
5. Embeddings are stored in a FAISS vector index.
6. A user question is embedded and matched against the indexed chunks.
7. The most relevant passages are re-ranked and used as context.
8. A local generation model produces an answer or a summary.

## Current Limitations

- Best performance is on simple, document-grounded questions.
- Complex reasoning and highly implicit questions remain limited.
- Response quality depends on chunking quality, retrieval quality, and the local generation model.
- The current version works on one indexed document at a time.

## Project Roadmap

### Completed

- [x] Initialize the project structure
- [x] Implement document loading
- [x] Validate document loading with tests
- [x] Implement document chunking
- [x] Validate chunking behavior
- [x] Add centralized configuration
- [x] Implement local embeddings
- [x] Build and save a FAISS index
- [x] Implement document retrieval
- [x] Build a complete RAG pipeline
- [x] Add answer generation
- [x] Display sources in the response
- [x] Add simple passage re-ranking
- [x] Add a robust fallback generation strategy
- [x] Add a Streamlit interface
- [x] Support document upload
- [x] Reposition the app as an academic assistant
- [x] Add document summary mode

### Next Versions

- [ ] Add conversation history
- [ ] Add key points extraction
- [ ] Add synthesis mode
- [ ] Support multiple documents
- [ ] Improve generation quality with a stronger model
- [ ] Add more automated tests
- [ ] Add screenshots and final architecture diagram
- [ ] Prepare the project for deployment

## Version History

### V1 - Core Ingestion

- Project structure
- Document loading
- Basic tests

### V2 - Retrieval and RAG Backend

- Chunking
- Local embeddings
- FAISS index
- Retrieval
- RAG pipeline
- Source display
- Re-ranking
- Fallback answer generation

### V3 - Academic Assistant

- Streamlit application
- Upload and indexing flow
- Question / answer mode
- Document summary mode
- Academic assistant positioning

## Project Structure

```text
rag-assistant/
|-- app/
|   |-- ingestion/
|   |   |-- loader.py
|   |   |-- pipeline.py
|   |   `-- splitter.py
|   |-- llm/
|   |   `-- generator.py
|   |-- prompts/
|   |   `-- rag_prompt.py
|   |-- retrieval/
|   |   `-- retriever.py
|   |-- vectorstore/
|   |   `-- faiss_store.py
|   |-- config.py
|   |-- main.py
|   `-- pipeline.py
|-- data/
|   |-- raw/
|   `-- processed/
|-- tests/
|-- streamlit_app.py
|-- README.md
`-- requirements.txt
```

## Run The App

Install dependencies, then launch Streamlit from the project root:

```powershell
python -m streamlit run streamlit_app.py
```

You can also run backend tests individually:

```powershell
python -m tests.test_loader
python -m tests.test_splitter
python -m tests.test_faiss_store
python -m tests.test_retriever
python -m tests.test_rag_pipeline
```

## Example Use Cases

- "Explain the notion of RAG from this course."
- "Summarize this lecture note."
- "What are the main concepts introduced in this document?"
- "Which passage best defines embeddings?"

## Why This Project Matters

This project is meant to demonstrate more than a simple chatbot. It shows the ability to:

- design a modular Python application
- work with unstructured documents
- build a retrieval-augmented generation pipeline
- debug retrieval and generation quality issues
- expose the result in an interactive application

## Next Improvement Priority

The next product step is to turn this into a stronger academic assistant by adding:

- conversation memory
- key points extraction
- synthesis features
- multi-document support
