# E-commerce Support Assistant

E-commerce Support Assistant is a portfolio project focused on building an AI assistant for online retail. The project combines two complementary capabilities:

- a FAQ-based support assistant for delivery, returns, refunds, and payment questions
- a structured product search engine for catalog questions such as size, color, price, and stock

The goal is to evolve this into a hybrid assistant able to route each user question to the right data source.

## Project Goal

Build a practical e-commerce assistant that can handle questions like:

- "Quels sont les delais de livraison ?"
- "Puis-je retourner un article solde ?"
- "Quels moyens de paiement acceptez-vous ?"
- "Avez-vous des sneakers black en 42 ?"
- "Montre-moi des produits a moins de 60 euros."

## Product Versions

### V1 - Support Knowledge Assistant

The assistant answers customer support questions from an internal FAQ knowledge base.

Covered topics:

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

The assistant can now search a structured product catalog using parsed filters extracted from natural language queries.

Covered filters:

- category
- gender
- color
- size
- max price
- stock availability

### V3 - Hybrid Assistant

The next step is to combine both systems through a routing layer:

- support and policy questions -> FAQ RAG pipeline
- product and catalog questions -> catalog pipeline

## Current Features

- FAQ knowledge base indexing
- text chunking and local embeddings
- FAISS vector search
- FAQ question answering with fallback response logic
- structured product catalog in CSV
- natural-language product query parsing
- product filtering with pandas
- formatted product search results
- Streamlit application entrypoint

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
6. The assistant generates a grounded response from the retrieved context.

### Product Catalog Flow

1. Product data is loaded from `data/raw/products.csv`.
2. A user query is parsed into structured filters.
3. The catalog is filtered by category, gender, color, size, price, and stock.
4. Matching products are formatted into a readable answer.

## Example Questions

### Support FAQ

- "Quels sont les delais de livraison ?"
- "Quels sont les frais de livraison ?"
- "Puis-je retourner un article solde ?"
- "Sous combien de temps suis-je rembourse ?"
- "Comment suivre ma commande ?"

### Product Search

- "Avez-vous des sneakers black en 42 ?"
- "Je cherche un hoodie white"
- "Montre-moi des jeans black pour femme"
- "Quels produits a moins de 60 euros ?"

## Current Limitations

- the support assistant works from a single FAQ knowledge base
- the product query parser is rule-based and still simple
- the FAQ and product search are not fully unified yet
- generation quality is limited by the local model

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
```

## Why This Project Matters

This project demonstrates:

- modular Python design
- retrieval-augmented generation on unstructured business content
- structured product search with pandas
- query parsing and routing logic
- business-oriented AI product thinking

## Roadmap

### Done

- [x] Build V1 FAQ-based support assistant
- [x] Build V2 product catalog search pipeline
- [ ] Build V3 hybrid assistant routing

### Next

- [ ] Combine FAQ and catalog handling in one assistant pipeline
- [ ] Improve the Streamlit interface
- [ ] Add conversation memory
- [ ] Improve product query parsing
- [ ] Prepare a polished demo version
