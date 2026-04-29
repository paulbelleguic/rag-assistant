from app.catalog.pipeline import CatalogPipeline

pipeline = CatalogPipeline()

queries = [
    "Avez-vous des sneakers black en 42 ?",
    "Je cherche un hoodie white",
    "Montre-moi des jeans black pour femme",
    "Quels produits a moins de 60 euros ?"
]

for query in queries:
    result = pipeline.search_from_query(query)

    print(f"\nQuestion : {result['query']}")
    print("Filtres extraits :", result["filters"])
    print("Nombre de produits trouves :", result["count"])
    print(result["formatted_results"])
