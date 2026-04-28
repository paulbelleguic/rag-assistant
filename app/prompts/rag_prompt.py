def build_rag_prompt(question: str, context: str) -> str:
    return f"""
Reponds en francais en utilisant uniquement le contexte ci-dessous.

Si l'information n'est pas presente dans le contexte, dis clairement que tu ne sais pas.

Contexte :
{context}

Question :
{question}

Reponse:
""".strip()
