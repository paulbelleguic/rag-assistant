from pathlib import Path

import streamlit as st

from app.ingestion.pipeline import IngestionPipeline
from app.pipeline import RAGPipeline


APP_TITLE = "Academic RAG Assistant"
RAW_DATA_DIR = Path("data/raw")
SUPPORTED_EXTENSIONS = {".txt", ".pdf"}


@st.cache_resource
def get_rag_pipeline(index_version: int) -> RAGPipeline:
    """Charge la pipeline RAG a partir de l'index courant."""
    return RAGPipeline()


def save_uploaded_file(uploaded_file) -> Path:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_path = RAW_DATA_DIR / uploaded_file.name
    file_path.write_bytes(uploaded_file.getbuffer())
    return file_path


def handle_upload() -> None:
    uploaded_file = st.file_uploader(
        "Charge un document (.txt ou .pdf)",
        type=["txt", "pdf"],
    )

    if uploaded_file is None:
        return

    file_suffix = Path(uploaded_file.name).suffix.lower()
    if file_suffix not in SUPPORTED_EXTENSIONS:
        st.error("Format non supporte. Utilise un fichier .txt ou .pdf.")
        return

    if st.button("Indexer le document", type="primary"):
        try:
            file_path = save_uploaded_file(uploaded_file)
            ingestion_pipeline = IngestionPipeline()
            chunk_count = ingestion_pipeline.ingest_file(str(file_path))

            st.session_state["document_ready"] = True
            st.session_state["indexed_file"] = uploaded_file.name
            st.session_state["index_version"] = st.session_state.get("index_version", 0) + 1

            st.success(
                f"Document indexe avec succes : {uploaded_file.name} ({chunk_count} chunks)."
            )
        except Exception as exc:
            st.error(f"Erreur pendant l'indexation : {exc}")


def handle_question() -> None:
    st.subheader("Assistant academique")

    question = st.text_input(
        "Ta question",
        placeholder="Exemple : Explique la notion de RAG dans ce cours.",
    )
    show_passages = st.checkbox("Afficher les passages pertinents", value=False)
    action = st.radio(
        "Choisis une action",
        options=["Question / reponse", "Resume du document"],
        horizontal=True,
    )

    if action == "Resume du document":
        if st.button("Generer un resume"):
            if not st.session_state.get("document_ready", False):
                st.warning("Charge et indexe d'abord un document.")
                return

            try:
                rag_pipeline = get_rag_pipeline(st.session_state.get("index_version", 0))
                result = rag_pipeline.summarize_document(k=4)

                st.subheader("Resume")
                st.write(result["summary"])

                st.subheader("Sources")
                for source in result["sources"]:
                    st.write(f"- {source}")

                if show_passages:
                    with st.expander("Passages utilises pour le resume"):
                        for index, passage in enumerate(result["passages"], start=1):
                            st.markdown(
                                f"**Passage {index}**  \n"
                                f"Source : `{passage['source']}`  \n"
                                f"Score : `{passage['score']:.4f}`"
                            )
                            st.write(passage["content"])
            except Exception as exc:
                st.error(f"Erreur pendant la generation du resume : {exc}")
        return

    if st.button("Poser la question"):
        if not question.strip():
            st.warning("Entre une question avant de lancer la recherche.")
            return

        if not st.session_state.get("document_ready", False):
            st.warning("Charge et indexe d'abord un document.")
            return

        try:
            rag_pipeline = get_rag_pipeline(st.session_state.get("index_version", 0))
            result = rag_pipeline.ask(question=question, k=2)

            st.subheader("Reponse")
            st.write(result["answer"])

            st.subheader("Sources")
            for source in result["sources"]:
                st.write(f"- {source}")

            if show_passages:
                with st.expander("Passages pertinents"):
                    for index, passage in enumerate(result["passages"], start=1):
                        st.markdown(
                            f"**Passage {index}**  \n"
                            f"Source : `{passage['source']}`  \n"
                            f"Score : `{passage['score']:.4f}`"
                        )
                        st.write(passage["content"])
        except Exception as exc:
            st.error(f"Erreur pendant la generation de la reponse : {exc}")


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon=":books:", layout="wide")
    st.title(APP_TITLE)
    st.write(
        "Charge un cours PDF ou texte, indexe-le, puis pose une question ou genere un resume."
    )

    if "document_ready" not in st.session_state:
        st.session_state["document_ready"] = False
    if "index_version" not in st.session_state:
        st.session_state["index_version"] = 0

    handle_upload()

    indexed_file = st.session_state.get("indexed_file")
    if indexed_file:
        st.info(f"Document courant : {indexed_file}")

    handle_question()


if __name__ == "__main__":
    main()
