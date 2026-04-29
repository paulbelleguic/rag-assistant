# E-commerce Support Assistant

E-commerce Support Assistant is a portfolio project focused on building an AI customer support assistant for online stores. The application uses a Retrieval-Augmented Generation (RAG) pipeline to answer customer questions from support knowledge documents such as FAQ, delivery rules, return policies, payment information, and service guidelines.

## Project Goal

Build a practical AI assistant that can help customers with questions like:

- What are the delivery times?
- Can I return a discounted product?
- Which payment methods are accepted?
- How do I track my order?

The long-term goal is to evolve this project into a hybrid assistant that can answer both:

- support and policy questions from documents
- product and catalog questions from structured data

## Current Scope

The current repository provides the technical foundation for the first version of the project:

- document loading
- text extraction
- chunking
- embeddings
- vector search with FAISS
- answer generation
- Streamlit interface

This first e-commerce version starts with a support knowledge base stored in documents.

## V1 Scope

The V1 assistant answers support questions related to:

- delivery
- shipping fees
- order tracking
- returns
- exchanges
- discounted items
- refunds
- payment methods
- order cancellation
- defective products
- customer service
- promo codes

At this stage, the assistant does not yet query a product catalog.

# E-commerce Support Assistant

E-commerce Support Assistant is a portfolio project focused on building an AI customer support assistant for online stores. The application uses a Retrieval-Augmented Generation (RAG) pipeline to answer customer questions from an internal support knowledge base.

## Project Goal

Build a practical AI assistant able to answer common customer support questions such as:

- What are the delivery times?
- Can I return a discounted product?
- Which payment methods are accepted?
- How do I track my order?
- How long does a refund take?

This first version is based on a FAQ-style support document and is designed as the foundation for a larger hybrid assistant.

## V1 Scope

The V1 assistant answers support questions related to:

- delivery
- shipping fees
- order tracking
- returns
- exchanges
- discounted items
- refunds
- payment methods
- order cancellation
- defective products
- customer service
- promo codes

At this stage, the assistant does not yet query a product catalog.

## Current Features

- internal FAQ knowledge base
- local document ingestion
- text chunking
- local embeddings
- FAISS vector search
- support-oriented answer generation
- fallback answer strategy for more stable responses
- Streamlit interface
- source display
- relevant passage display

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face embeddings
- Transformers
- PyPDF

## How It Works

1. The FAQ knowledge base is loaded and indexed.
2. The text is split into chunks.
3. Chunks are embedded with a local Hugging Face model.
4. Embeddings are stored in a FAISS vector index.
5. A customer question is matched against the indexed support passages.
6. The most relevant passages are retrieved and lightly re-ranked.
7. The system generates a grounded support answer from the retrieved context.

## Example Questions

- "Quels sont les délais de livraison ?"
- "Quels sont les frais de livraison ?"
- "Puis-je retourner un article soldé ?"
- "Sous combien de temps suis-je remboursé ?"
- "Quels moyens de paiement acceptez-vous ?"
- "Comment suivre ma commande ?"
- "Puis-je annuler une commande déjà expédiée ?"

## Current Limitations

- best performance is on simple support questions directly covered by the FAQ
- the current version works from one internal knowledge base
- the assistant does not yet search a structured product catalog
- generation quality is limited by the local model

### V1 - Support Knowledge Assistant

- Upload and index support documents
- Ask customer support questions
- Display retrieved sources
- Display relevant passages with similarity scores

### V2 - Product Catalog Search

- Add structured product data
- Search by category, price, size, and color
- Return product matches from tabular data

### V3 - Hybrid Assistant

- Detect support vs product questions
- Route the request to the right data source
- Combine document answers and catalog answers

### V4 - Conversational Experience

- Add conversation history
- Support follow-up questions
- Keep short-term context

### V5 - Final Portfolio Version

- Improve UI and UX
- Add stronger response quality
- Add better README, screenshots, and architecture diagram
- Prepare a polished demo version

## Current Repository Status

This repository currently contains a reusable RAG foundation inherited from the previous prototype:

- ingestion pipeline
- vector indexing
- retrieval logic
- answer generation
- Streamlit app structure

The next step is to adapt this foundation to the e-commerce support use case, starting from a `faq.txt` knowledge base.

## Project Roadmap

### Completed Foundation

- [x] Initialize the project structure
- [x] Implement document loading
- [x] Implement document chunking
- [x] Add local embeddings
- [x] Build and save a FAISS index
- [x] Implement retrieval
- [x] Build a RAG pipeline
- [x] Add answer generation
- [x] Add source display
- [x] Add simple reranking
- [x] Add a fallback generation strategy
- [x] Add a Streamlit entrypoint

### In Progress

- [x] Reposition the app for e-commerce support
- [x] Build the V1 around a FAQ knowledge base
- [x] Adapt prompts to customer support use cases
- [ ] Test the assistant on delivery, return, and payment questions

### Next

- [ ] Add structured product data
- [ ] Implement product search
- [ ] Route questions by intent
- [ ] Add conversation memory
- [ ] Improve generation quality
- [ ] Add screenshots and deployment preparation

### V1 - Support Knowledge Assistant
- [x]  build a FAQ-based support assistant
- [x]  answer customer support questions
- [x]  display sources and relevant passages
- [x]  stabilize responses with fallback logic

### V2 - Product Catalog Search
- [ ]  add structured product data
- [ ]  search by category, size, color, and price
- [ ]  return product matches from tabular data

### V3 - Hybrid Assistant
- [ ]  detect support vs product questions
- [ ]  route requests to the right source
- [ ]  combine FAQ answers and product answers

### V4 - Conversational Experience
- [ ]  add conversation history
- [ ]  support follow-up questions
- [ ]  keep short-term conversational context

### V5 - Final version
- [ ]  improve UI and UX
- [ ]  strengthen generation quality
- [ ]  prepare a polished demo version

## Project Structure

```text
ecommerce-support-assistant/
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
|   |   `-- faq.txt
|   `-- processed/
|-- tests/
|-- streamlit_app.py
|-- README.md
`-- requirements.txt
```

## Run The App

Launch the application from the project root:

```powershell
python -m streamlit run streamlit_app.py
```

You can also run the backend tests:

```powershell
python -m tests.test_loader
python -m tests.test_splitter
python -m tests.test_faiss_store
python -m tests.test_retriever
python -m tests.test_rag_pipeline
```

## Why This Project Matters

This project is more than a simple chatbot. It is designed to demonstrate:

- modular Python engineering
- document-based retrieval systems
- applied NLP and RAG design
- debugging of retrieval and generation quality
- business-oriented AI product thinking

## Next Immediate Step

The next concrete step is to validate the V1 e-commerce support assistant on realistic support questions using the FAQ knowledge base in `data/raw/faq.txt`.
