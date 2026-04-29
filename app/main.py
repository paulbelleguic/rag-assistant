import streamlit as st

from app.assistant.pipeline import EcommerceAssistantPipeline
from app.ingestion.pipeline import IngestionPipeline


APP_TITLE = "E-commerce Support Assistant"
DEFAULT_FAQ_PATH = "data/raw/faq.txt"


@st.cache_resource
def get_assistant_pipeline(index_version: int) -> EcommerceAssistantPipeline:
    """Charge la pipeline hybride a partir de l'index courant."""
    return EcommerceAssistantPipeline()


def initialize_knowledge_base() -> None:
    st.subheader("Base de connaissances")

    if st.session_state.get("document_ready", False):
        st.success("La FAQ e-commerce est chargee et prete a etre interrogee.")
        return

    try:
        ingestion_pipeline = IngestionPipeline()
        chunk_count = ingestion_pipeline.ingest_file(DEFAULT_FAQ_PATH)

        st.session_state["document_ready"] = True
        st.session_state["indexed_file"] = "faq.txt"
        st.session_state["index_version"] = st.session_state.get("index_version", 0) + 1

        st.success(f"FAQ e-commerce indexee avec succes ({chunk_count} chunks).")
    except Exception as exc:
        st.error(f"Erreur pendant l'indexation de la FAQ : {exc}")


def handle_question() -> None:
    st.subheader("Assistant support client")

    question = st.text_input(
        "Question client",
        placeholder="Exemple : Puis-je retourner un article solde ?",
    )
    show_passages = st.checkbox("Afficher les passages pertinents", value=False)

    if st.button("Poser la question"):
        if not question.strip():
            st.warning("Entre une question avant de lancer la recherche.")
            return

        if not st.session_state.get("document_ready", False):
            st.warning("Charge et indexe d'abord un document.")
            return

        try:
            assistant_pipeline = get_assistant_pipeline(st.session_state.get("index_version", 0))
            result = assistant_pipeline.ask(query=question)

            st.subheader("Reponse")
            st.write(result["answer"])

            st.caption(
                f"Routage : {result['route']} | "
                f"support_score={result['routing']['support_score']} | "
                f"product_score={result['routing']['product_score']}"
            )

            st.subheader("Sources")
            for source in result["sources"]:
                st.write(f"- {source}")

            if show_passages and result["route"] == "support":
                with st.expander("Passages pertinents"):
                    for index, passage in enumerate(result["details"]["passages"], start=1):
                        st.markdown(
                            f"**Passage {index}**  \n"
                            f"Source : `{passage['source']}`  \n"
                            f"Score : `{passage['score']:.4f}`"
                        )
                        st.write(passage["content"])
            elif show_passages and result["route"] == "catalog":
                with st.expander("Details catalogue"):
                    st.write("Filtres extraits :", result["details"]["filters"])
                    st.write(result["details"]["formatted_results"])
        except Exception as exc:
            st.error(f"Erreur pendant la generation de la reponse : {exc}")


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon=":books:", layout="wide")
    st.title(APP_TITLE)
    st.write(
        "Cette V1 repond aux questions clients a partir d'une FAQ e-commerce interne sur la livraison, les retours, le paiement, les remboursements et le suivi de commande."
    )

    if "document_ready" not in st.session_state:
        st.session_state["document_ready"] = False
    if "index_version" not in st.session_state:
        st.session_state["index_version"] = 0

    initialize_knowledge_base()

    indexed_file = st.session_state.get("indexed_file")
    if indexed_file:
        st.info(f"Base de connaissances courante : {indexed_file}")

    handle_question()


if __name__ == "__main__":
    main()
