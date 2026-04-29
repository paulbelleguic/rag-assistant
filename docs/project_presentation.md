# Project Presentation Kit

## CV Summary

Built a hybrid AI e-commerce assistant combining FAQ-based RAG for customer support and structured product search for catalog questions. Designed a modular Python architecture with FAISS retrieval, Hugging Face embeddings, query routing, conversational follow-up handling, and a Streamlit chatbot interface.

## LinkedIn Summary

Developed an end-to-end hybrid AI assistant for e-commerce support. The project combines a FAQ-based RAG pipeline for delivery, returns, refunds, and payment questions with a structured product search engine for catalog queries such as size, color, price, and stock. I implemented document ingestion, chunking, local embeddings, FAISS retrieval, rule-based query routing, product query parsing, follow-up handling, and a modern Streamlit interface.

## Interview Pitch

This project started as a FAQ support assistant and evolved into a hybrid e-commerce assistant. I separated the system into two pipelines: a RAG pipeline for support knowledge and a catalog pipeline for structured product search. Then I added a routing layer to decide which source should answer each user question. I also added simple conversational memory so short follow-up queries like "et en 43 ?" can reuse the previous product context.

## Architecture

- `ingestion`: load FAQ data, split it into chunks, build the FAISS index
- `retrieval`: search relevant FAQ passages for support questions
- `llm`: generate support answers with fallback logic
- `catalog`: load product CSV data, parse user filters, and search structured products
- `routing`: classify a query as support or catalog
- `assistant`: unify both pipelines behind a single interface
- `main.py`: expose the system through Streamlit

## Technical Choices

- RAG for support policies because they live naturally in documents
- Structured search for products because price, size, color, and stock need exact filtering
- Rule-based routing and parsing first because it is simple to debug and easy to explain
- Streamlit because it is fast for prototyping and portfolio demos

## Current Limitations

- support generation still depends on a lightweight local model
- the FAQ is limited to a single internal knowledge base
- product parsing is still rule-based
- follow-up memory is heuristic-based

## Possible Evolutions

- improve support answer quality with a stronger model
- expand product parsing with more French synonyms
- add stronger conversation memory
- support richer product metadata and more business intents

## Five Demo Questions

1. `Quels sont les delais de livraison ?`
2. `Puis-je retourner un article solde ?`
3. `Avez-vous des sneakers noires en 42 ?`
4. `et en 43 ?`
5. `Quels produits a moins de 60 euros ?`
