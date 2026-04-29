import re


class CatalogQueryParser:
    """Extrait des filtres produits simples depuis une question utilisateur."""

    CATEGORIES = {
        "t-shirt": "t-shirt",
        "shirt": "shirt",
        "jeans": "jeans",
        "sneakers": "sneakers",
        "jacket": "jacket",
        "coat": "coat",
        "dress": "dress",
        "hoodie": "hoodie",
        "boots": "boots",
        "leggings": "leggings",
        "polo": "polo",
        "sweater": "sweater",
        "shorts": "shorts",
        "blouse": "blouse",
        "blazer": "blazer",
        "top": "top",
        "cardigan": "cardigan",
    }

    COLORS = {
        "black": "black",
        "white": "white",
        "blue": "blue",
        "red": "red",
        "green": "green",
        "grey": "grey",
        "beige": "beige",
        "brown": "brown",
        "navy": "navy",
        "cream": "cream",
    }

    GENDERS = {
        "homme": "men",
        "men": "men",
        "femme": "women",
        "women": "women",
        "unisex": "unisex",
    }

    def parse(self, query: str) -> dict:
        query_lower = query.lower()

        category = self._extract_match(query_lower, self.CATEGORIES)
        color = self._extract_match(query_lower, self.COLORS)
        gender = self._extract_match(query_lower, self.GENDERS)
        size = self._extract_size(query_lower)
        max_price = self._extract_max_price(query_lower)

        return {
            "category": category,
            "color": color,
            "gender": gender,
            "size": size,
            "max_price": max_price,
        }

    @staticmethod
    def _extract_match(query: str, mapping: dict) -> str | None:
        for keyword, value in mapping.items():
            if keyword in query:
                return value
        return None

    @staticmethod
    def _extract_size(query: str) -> str | None:
        size_patterns = [r"\b(2[0-9]|3[0-9]|4[0-9]|5[0-9])\b", r"\b(xs|s|m|l|xl)\b"]
        for pattern in size_patterns:
            match = re.search(pattern, query)
            if match:
                return match.group(1).upper()
        return None

    @staticmethod
    def _extract_max_price(query: str) -> float | None:
        match = re.search(r"(moins de|max|maximum)\s+(\d+)", query)
        if match:
            return float(match.group(2))
        return None
