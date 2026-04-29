from app.catalog.loader import CatalogLoader
from app.catalog.search import CatalogSearch

loader = CatalogLoader()
products_df = loader.load_products()

search = CatalogSearch(products_df)

results = search.filter_products(
    category="sneakers",
    color="black",
    size="42",
    only_in_stock=True
)

print("=== Resultats filtres ===")
print(results)

print("\n=== Resultats formates ===")
print(search.format_results(results))
