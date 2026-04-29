from app.catalog.pipeline import CatalogPipeline

pipeline = CatalogPipeline()

result = pipeline.find_products(
    category="sneakers",
    color="black",
    size="42",
    only_in_stock=True
)

print(f"Nombre de produits trouves : {result['count']}")
print("\n=== Resultats formates ===")
print(result["formatted_results"])
