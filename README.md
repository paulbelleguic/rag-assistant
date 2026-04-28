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

### Checklist projet

- [x] Initialiser la structure du projet
- [x] Implementer le chargement de documents texte
- [x] Verifier le chargement avec un test simple
- [x] Implementer le chunking des documents
- [x] Verifier le chunking avec overlap
- [x] Ajouter la configuration centralisee du projet
- [x] Implementer les embeddings
- [x] Construire et sauvegarder l'index FAISS
- [x] Implementer la recherche de passages pertinents
- [x] Connecter un LLM pour la generation de reponse
- [x] Construire une pipeline RAG complete
- [x] Afficher les sources utilisees dans la reponse
- [x] Ajouter un reranking simple des passages
- [x] Ajouter un fallback de reponse plus robuste
- [ ] Ajouter une interface Streamlit
- [ ] Permettre l'upload de documents
- [ ] Ajouter un historique de conversation
- [ ] Ajouter des tests supplementaires
- [ ] Ameliorer le README avec captures et architecture finale
- [ ] Preparer le projet pour le deploiement

### Etape 1 - Chargement de documents

- creation de la structure du projet
- implementation de `DocumentLoader`
- test de chargement d'un fichier texte avec conservation de la source

### Etape 2 - Chunking

- implementation de `DocumentSplitter`
- test du decoupage en chunks avec overlap

### Etape 3 - Embeddings et indexation vectorielle

- implementation d'un gestionnaire d'index FAISS
- generation d'embeddings en local avec un modele Hugging Face
- creation et sauvegarde de l'index vectoriel pour les chunks

### Etape 4 - Retrieval et pipeline RAG

- implementation d'un retriever pour interroger FAISS avec une question
- construction d'une pipeline RAG unifiee
- affichage de la reponse, du contexte et des sources
- ajout d'un reranking simple par mots-cles
- ajout d'un fallback pour produire une reponse plus robuste en francais

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

- creer l'interface Streamlit
- permettre l'upload de documents
- ajouter un historique de conversation
- ameliorer la qualite de generation avec un modele plus performant
