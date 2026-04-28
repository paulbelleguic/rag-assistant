from app.retrieval.retriever import Retriever

retriever = Retriever()

query = "Qu'est-ce que le RAG ?"
results = retriever.retrieve(query=query, k=2)

print(f"Question : {query}")
print(f"Nombre de resultats : {len(results)}")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Resultat {i} ---")
    print(doc.page_content)
    print(doc.metadata)
