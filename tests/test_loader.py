from app.ingestion.loader import DocumentLoader

loader = DocumentLoader()
documents = loader.load_documents("data/raw/mon_document.txt")

print(f"Nombre de documents chargés : {len(documents)}")
print(documents[0].page_content[:1000])
print(documents[0].metadata)
