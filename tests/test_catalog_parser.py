from app.catalog.parser import CatalogQueryParser

parser = CatalogQueryParser()

queries = [
    "Avez-vous des sneakers black en 42 ?",
    "Je cherche un hoodie white",
    "Montre-moi des jeans black pour femme",
    "Quels produits a moins de 60 euros ?"
]

for query in queries:
    parsed = parser.parse(query)
    print(f"\nQuestion : {query}")
    print(parsed)
