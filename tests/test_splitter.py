from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter

loader = DocumentLoader()
documents = loader.load_documents("data/raw/mon_document.txt")

splitter = DocumentSplitter(chunk_size=80, chunk_overlap=20)
chunks = splitter.split_documents(documents)

print(f"Nombre de chunks : {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk.page_content)
    print(chunk.metadata)
