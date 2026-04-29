from app.assistant.pipeline import EcommerceAssistantPipeline

assistant = EcommerceAssistantPipeline()

queries = [
    "Quels sont les delais de livraison ?",
    "Puis-je retourner un article solde ?",
    "Avez-vous des sneakers black en 42 ?",
    "Quels produits a moins de 60 euros ?",
]

for query in queries:
    result = assistant.ask(query)

    print(f"\nQuestion : {query}")
    print("Route :", result["route"])
    print("Routing :", result["routing"])
    print("Reponse :")
    print(result["answer"])
    print("Sources :", result["sources"])
