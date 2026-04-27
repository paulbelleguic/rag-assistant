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
- [ ] Ajouter la configuration centralisee du projet
- [ ] Implementer les embeddings
- [ ] Construire et sauvegarder l'index FAISS
- [ ] Implementer la recherche de passages pertinents
- [ ] Connecter un LLM pour la generation de reponse
- [ ] Construire une pipeline RAG complete
- [ ] Afficher les sources utilisees dans la reponse
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
