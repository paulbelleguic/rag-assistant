from app.catalog.pipeline import CatalogPipeline
from app.pipeline import RAGPipeline
from app.routing.classifier import QueryRouter


class EcommerceAssistantPipeline:
    """Pipeline hybride qui route une question vers la FAQ ou le catalogue."""

    def __init__(self) -> None:
        self.router = QueryRouter()
        self.support_pipeline = RAGPipeline()
        self.catalog_pipeline = CatalogPipeline()

    def ask(self, query: str) -> dict:
        if not query.strip():
            raise ValueError("La question utilisateur ne peut pas etre vide.")

        routing = self.router.route(query)

        if routing["route"] == "catalog":
            catalog_result = self.catalog_pipeline.search_from_query(query)
            answer = self._build_catalog_answer(catalog_result["formatted_results"])

            return {
                "query": query,
                "route": "catalog",
                "answer": answer,
                "sources": ["data/raw/products.csv"],
                "details": {
                    "filters": catalog_result["filters"],
                    "count": catalog_result["count"],
                    "formatted_results": catalog_result["formatted_results"],
                },
                "routing": routing,
            }

        support_result = self.support_pipeline.ask(question=query, k=4)

        return {
            "query": query,
            "route": "support",
            "answer": support_result["answer"],
            "sources": support_result["sources"],
            "details": {
                "passages": support_result["passages"],
                "context": support_result["context"],
            },
            "routing": routing,
        }

    @staticmethod
    def _build_catalog_answer(formatted_results: str) -> str:
        if formatted_results == "Aucun produit correspondant n'a ete trouve.":
            return formatted_results

        return "J'ai trouve les produits suivants :\n" + formatted_results
