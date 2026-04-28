import re

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from app.prompts.rag_prompt import build_rag_prompt


class AnswerGenerator:
    """Genere une reponse a partir du contexte recupere."""

    def __init__(self) -> None:
        model_name = "google/flan-t5-base"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate(self, question: str, context: str, max_new_tokens: int = 150) -> str:
        if not question.strip():
            raise ValueError("La question ne peut pas etre vide.")

        if not context.strip():
            return "Je ne dispose pas de contexte suffisant pour repondre."

        prompt = build_rag_prompt(question=question, context=context)
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False
        )
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        if self._should_fallback(answer):
            return self._build_fallback_answer(context)

        return answer

    def summarize(self, context: str, max_new_tokens: int = 180) -> str:
        if not context.strip():
            return "Je ne dispose pas de contenu suffisant pour produire un resume."

        prompt = (
            "Resume le document suivant en francais de maniere claire et concise.\n\n"
            f"Document :\n{context}\n\n"
            "Resume :"
        )
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False
        )
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        if self._should_fallback(summary):
            return self._build_fallback_summary(context)

        return summary

    @staticmethod
    def _should_fallback(answer: str) -> bool:
        cleaned = answer.strip().lower()

        if not cleaned:
            return True

        if len(cleaned.split()) < 6:
            return True

        prompt_leak_patterns = [
            "reponds en francais",
            "using only the contexte",
            "if information is not present",
            "dis clairement que tu ne sais pas",
            "contexte ci-dessous",
        ]

        if any(pattern in cleaned for pattern in prompt_leak_patterns):
            return True

        if " and " in cleaned or "research" in cleaned:
            return True

        return False


    @staticmethod
    def _build_fallback_answer(context: str) -> str:
        sentences = [
            sentence.strip()
            for sentence in re.split(r"(?<=[.!?])\s+", context.strip())
            if sentence.strip()
        ]

        if not sentences:
            return "Je ne dispose pas de contexte suffisant pour repondre."

        if len(sentences) == 1:
            return f"D'apres le document, {sentences[0]}"

        return f"D'apres le document, {sentences[0]} {sentences[1]}"

    @staticmethod
    def _build_fallback_summary(context: str) -> str:
        sentences = [
            sentence.strip()
            for sentence in re.split(r"(?<=[.!?])\s+", context.strip())
            if sentence.strip()
        ]

        if not sentences:
            return "Je ne dispose pas de contenu suffisant pour produire un resume."

        selected = sentences[:3]
        return "Resume du document : " + " ".join(selected)
