# E-commerce Support Assistant

E-commerce Support Assistant is a portfolio project focused on building a hybrid AI assistant for online retail. It combines:

- a FAQ-based support assistant for delivery, returns, refunds, payment, and order tracking
- a structured product search engine for catalog questions such as size, color, price, and stock

The application routes each user question to the right source and exposes the result through a modern Streamlit interface.

## Project Goal

Build a practical e-commerce assistant able to answer questions like:

- "Quels sont les delais de livraison ?"
- "Puis-je retourner un article solde ?"
- "Quels moyens de paiement acceptez-vous ?"
- "Avez-vous des sneakers noires en 42 ?"
- "Montre-moi des produits a moins de 60 euros."

## Current Product State

The current version already supports:

- support and policy questions from a FAQ knowledge base
- product and catalog questions from structured data
- automatic routing between FAQ support and catalog search
- simple conversational follow-ups such as product refinements
- a retail-inspired chatbot interface in Streamlit

## Product Versions

### V1 - Support Knowledge Assistant

Built a FAQ-based support assistant for:

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

### V2 - Product Catalog Search

Added a structured product catalog with natural-language filtering on:

- category
- gender
- color
- size
- max price
- stock availability

### V3 - Hybrid Assistant

Combined both systems with:

- question routing between support and catalog
- unified assistant pipeline
- support for short follow-up queries

### V4 - Conversational Experience

Improved the interaction layer with:

- chat history
- follow-up handling
- more natural support answers
- better routing and parsing behavior

### V5 - UI Showcase

Added a stronger product-facing presentation layer with:

- a modern retail-inspired layout
- a storefront-style left panel
- a rounded floating assistant panel
- scrollable in-panel chat history

## Current Features

- FAQ knowledge base indexing from `data/raw/faq.txt`
- chunking, embeddings, and FAISS retrieval
- support answer generation with fallback logic
- structured product catalog from `data/raw/products.csv`
- natural-language product query parsing
- catalog filtering with pandas
- automatic routing between support and product search
- simple conversational memory for follow-up requests
- modern Streamlit chatbot interface
- source display and optional technical details

## Tech Stack

- Python
- Streamlit
- Pandas
- LangChain
- FAISS
- Hugging Face embeddings
- Transformers
- PyPDF

## How It Works

### FAQ Support Flow

1. The FAQ knowledge base is loaded from `data/raw/faq.txt`.
2. The text is split into chunks.
3. Chunks are embedded locally.
4. Embeddings are stored in a FAISS index.
5. A support question retrieves the most relevant passages.
6. The assistant generates a grounded support answer from the retrieved context.

### Product Catalog Flow

1. Product data is loaded from `data/raw/products.csv`.
2. A user query is parsed into structured filters.
3. The catalog is filtered by category, gender, color, size, price, and stock.
4. Matching products are formatted into a readable answer.

### Hybrid Routing Flow

1. The user asks a question in the chat interface.
2. A router classifies the query as `support` or `catalog`.
3. The assistant calls the appropriate pipeline.
4. The result is returned in a single conversational interface.

## Example Questions

### Support FAQ

- "Quels sont les delais de livraison ?"
- "Quels sont les frais de livraison ?"
- "Puis-je retourner un article solde ?"
- "Sous combien de temps suis-je rembourse ?"
- "Comment suivre ma commande ?"

### Product Search

- "Avez-vous des sneakers noires en 42 ?"
- "Je cherche un hoodie blanc"
- "Montre-moi des jeans noirs pour femme"
- "Quels produits a moins de 60 euros ?"

### Conversational Follow-up

- "Avez-vous des sneakers noires en 42 ?"
- "et en 43 ?"

## Current Limitations

- the support assistant still relies on a single FAQ document
- the product query parser is rule-based and still limited
- follow-up memory is short-term and heuristic-based
- support answer generation quality depends on the local model and fallback logic
- the visual storefront is a presentation layer, not a real e-commerce backend

## Project Structure

```text
ecommerce-support-assistant/
|-- app/
|   |-- assistant/
|   |   `-- pipeline.py
|   |-- catalog/
|   |   |-- loader.py
|   |   |-- parser.py
|   |   |-- pipeline.py
|   |   `-- search.py
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
|   |-- routing/
|   |   `-- classifier.py
|   |-- vectorstore/
|   |   `-- faiss_store.py
|   |-- config.py
|   |-- main.py
|   `-- pipeline.py
|-- data/
|   |-- raw/
|   |   |-- faq.txt
|   |   `-- products.csv
|   `-- processed/
|-- tests/
|-- streamlit_app.py
|-- README.md
`-- requirements.txt
```

## Run The App

From the project root:

```powershell
python -m streamlit run streamlit_app.py
```

## Run Backend Tests

```powershell
python -m tests.test_loader
python -m tests.test_splitter
python -m tests.test_faiss_store
python -m tests.test_retriever
python -m tests.test_rag_pipeline
python -m tests.test_catalog_search
python -m tests.test_catalog_parser
python -m tests.test_catalog_pipeline
python -m tests.test_catalog_query_pipeline
python -m tests.test_query_router
python -m tests.test_ecommerce_assistant_pipeline
```

## Why This Project Matters

This project demonstrates:

- modular Python design
- retrieval-augmented generation on unstructured business content
- structured product search with pandas
- query parsing and routing logic
- conversational assistant design
- business-oriented AI product thinking

## Roadmap

### Completed

- [x] Build V1 FAQ-based support assistant
- [x] Build V2 product catalog search pipeline
- [x] Build V3 hybrid assistant routing
- [x] Add conversational follow-up handling
- [x] Build a retail-inspired Streamlit interface

### Next

- [ ] Improve support answer quality further
- [ ] Expand product query coverage
- [ ] Add stronger conversation memory
- [ ] Add more robust evaluation and testing
- [ ] Prepare a polished final demo and deployment
