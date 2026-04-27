# RAG Assistant

Projet de portfolio Data / IA : construction d'un assistant IA de type RAG (Retrieval-Augmented Generation) capable de repondre a des questions en langage naturel a partir de documents.

## Objectif

Construire une application complete avec :

- chargement de documents
- extraction de texte
- chunking
- embeddings
- recherche vectorielle
- generation de reponses avec un LLM
- interface utilisateur avec Streamlit

## Stack technique

- Python
- LangChain
- FAISS
- OpenAI API
- Streamlit

## Avancement du projet

### Etape 1 - Chargement de documents

- creation de la structure du projet
- implementation de `DocumentLoader`
- test de chargement d'un fichier texte avec conservation de la source

### Etape 2 - Chunking

- implementation de `DocumentSplitter`
- test du decoupage en chunks avec overlap

## Structure du projet

```text
rag-assistant/
├── app/
│   ├── ingestion/
│   │   ├── loader.py
│   │   └── splitter.py
├── data/
│   └── raw/
├── notebooks/
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Lancer le projet

```powershell
python -m tests.test_loader
python -m tests.test_splitter
```

## Prochaines etapes

- creer les embeddings
- construire la base vectorielle FAISS
- implementer la recherche de contexte
- connecter un LLM pour generer la reponse
- creer l'interface Streamlit
