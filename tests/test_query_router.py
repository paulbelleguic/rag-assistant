from app.routing.classifier import QueryRouter

router = QueryRouter()

queries = [
    "Quels sont les delais de livraison ?",
    "Puis-je retourner un article solde ?",
    "Avez-vous des sneakers black en 42 ?",
    "Je cherche un hoodie white",
]

for query in queries:
    result = router.route(query)
    print(f"\nQuestion : {query}")
    print(result)
