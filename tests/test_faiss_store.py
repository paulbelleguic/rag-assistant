from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter
from app.vectorstore.faiss_store import VectorStoreManager

loader = DocumentLoader()
documents = loader.load_documents("data/raw/mon_document.txt")

splitter = DocumentSplitter(chunk_size=150, chunk_overlap=30)
chunks = splitter.split_documents(documents)

manager = VectorStoreManager()
vectorstore = manager.create_vectorstore(chunks)
manager.save_vectorstore(vectorstore)

print("Index FAISS cree et sauvegarde avec succes.")
