from app.pipeline import RAGPipeline

pipeline = RAGPipeline()

result = pipeline.ask("Qu'est-ce que le RAG ?", k=2)

print(f"Question : {result['question']}")
print("\n--- Contexte recupere ---")
print(result["context"])
print("\n--- Reponse ---")
print(result["answer"])
print("\n--- Sources ---")
for source in result["sources"]:
    print(source)
print("\n--- Passages pertinents ---")
for i, passage in enumerate(result["passages"], start=1):
    print(f"{i}. score={passage['score']:.4f} | source={passage['source']}")
    print(passage["content"])
