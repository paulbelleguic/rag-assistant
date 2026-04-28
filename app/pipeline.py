import re

from app.llm.generator import AnswerGenerator
from app.retrieval.retriever import Retriever


class RAGPipeline:
    """Orchestre la recherche de contexte et la generation de reponse."""

    def __init__(self) -> None:
        self.retriever = Retriever()
        self.generator = AnswerGenerator()

    def ask(self, question: str, k: int = 2) -> dict:
        if not question.strip():
            raise ValueError("La question ne peut pas etre vide.")

        results = self.retriever.retrieve_with_scores(query=question, k=k)
        results = self._rerank_results(question=question, results=results)
        documents = [item["document"] for item in results]
        context = "\n\n".join(doc.page_content for doc in documents)
        answer = self.generator.generate(question=question, context=context)

        sources = list(dict.fromkeys(
            doc.metadata.get("source", "source inconnue") for doc in documents
        ))

        return {
            "question": question,
            "answer": answer,
            "context": context,
            "sources": sources,
            "passages": [
                {
                    "content": item["document"].page_content,
                    "source": item["document"].metadata.get("source", "source inconnue"),
                    "score": item["score"],
                }
                for item in results
            ],
        }

    def summarize_document(self, k: int = 4) -> dict:
        results = self.retriever.retrieve_with_scores(query="resume du document cours notions principales", k=k)
        documents = [item["document"] for item in results]
        context = "\n\n".join(doc.page_content for doc in documents)
        summary = self.generator.summarize(context=context)

        sources = list(dict.fromkeys(
            doc.metadata.get("source", "source inconnue") for doc in documents
        ))

        return {
            "summary": summary,
            "context": context,
            "sources": sources,
            "passages": [
                {
                    "content": item["document"].page_content,
                    "source": item["document"].metadata.get("source", "source inconnue"),
                    "score": item["score"],
                }
                for item in results
            ],
        }

    @staticmethod
    def _extract_keywords(question: str) -> list[str]:
        tokens = re.findall(r"\b\w+\b", question.lower())
        stopwords = {
            "qu", "que", "quoi", "qui", "de", "du", "des", "le", "la", "les",
            "un", "une", "est", "et", "a", "au", "aux", "en", "dans", "sur",
            "pour", "par", "comment", "pourquoi", "qu", "ce", "cette"
        }
        keywords = [token for token in tokens if token not in stopwords and len(token) > 2]
        return list(dict.fromkeys(keywords))

    def _rerank_results(self, question: str, results: list[dict]) -> list[dict]:
        keywords = self._extract_keywords(question)

        if not keywords:
            return results

        def ranking_key(item: dict) -> tuple[int, float]:
            content = item["document"].page_content.lower()
            keyword_hits = sum(1 for keyword in keywords if keyword in content)
            return (-keyword_hits, item["score"])

        return sorted(results, key=ranking_key)
