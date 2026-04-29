import streamlit as st

from app.assistant.pipeline import EcommerceAssistantPipeline
from app.ingestion.pipeline import IngestionPipeline


APP_TITLE = "E-commerce Support Assistant"
DEFAULT_FAQ_PATH = "data/raw/faq.txt"
NAV_ITEMS = ["Long Sleeve", "Tees", "Beanies", "Polos", "Caps", "Shorts"]
FEATURED_PRODUCTS = [
    {"name": "Shadow Tee", "tag": "NEW IN", "price": "34 EUR"},
    {"name": "Core Hoodie", "tag": "NEW IN", "price": "79 EUR"},
    {"name": "Utility Shorts", "tag": "NEW IN", "price": "49 EUR"},
    {"name": "Steel Sneakers", "tag": "NEW IN", "price": "99 EUR"},
]


@st.cache_resource
def get_assistant_pipeline(index_version: int) -> EcommerceAssistantPipeline:
    """Charge la pipeline hybride a partir de l'index courant."""
    return EcommerceAssistantPipeline()


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(240,240,240,0.96), rgba(255,255,255,1) 38%),
                linear-gradient(135deg, #f8f8f5 0%, #ecece7 100%);
            color: #101010;
        }
        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 1.4rem;
        }
        .brand-shell {
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(16,16,16,0.08);
            border-radius: 28px;
            padding: 18px 22px;
            box-shadow: 0 18px 50px rgba(16,16,16,0.08);
            margin-bottom: 1rem;
        }
        .brand-topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }
        .brand-name {
            font-size: 1.05rem;
            font-weight: 900;
            letter-spacing: 0.25rem;
        }
        .brand-nav {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .brand-pill {
            border-radius: 999px;
            padding: 8px 14px;
            background: #f0f0eb;
            border: 1px solid rgba(16,16,16,0.08);
            font-size: 0.82rem;
        }
        .hero-card {
            position: relative;
            overflow: hidden;
            border-radius: 32px;
            min-height: 400px;
            padding: 34px;
            margin-bottom: 1rem;
            color: #fafaf7;
            background:
                linear-gradient(120deg, rgba(12,12,12,0.88), rgba(60,60,60,0.44)),
                radial-gradient(circle at 82% 22%, rgba(255,255,255,0.16), transparent 20%),
                linear-gradient(160deg, #9d9b94 0%, #d9d6cf 100%);
            box-shadow: 0 28px 70px rgba(16,16,16,0.18);
        }
        .hero-kicker {
            text-transform: uppercase;
            letter-spacing: 0.18rem;
            font-size: 0.72rem;
            opacity: 0.82;
        }
        .hero-title {
            max-width: 430px;
            margin: 0.45rem 0 1rem 0;
            font-size: 3rem;
            line-height: 0.95;
            letter-spacing: -0.05rem;
            font-weight: 900;
        }
        .hero-copy {
            max-width: 360px;
            color: rgba(250,250,247,0.84);
            font-size: 0.98rem;
        }
        .hero-shop {
            display: inline-block;
            margin-top: 1.2rem;
            border-radius: 999px;
            background: #fafaf7;
            color: #111111;
            padding: 12px 22px;
            font-weight: 900;
            font-size: 0.92rem;
        }
        .hero-model {
            position: absolute;
            right: 28px;
            bottom: -8px;
            width: 250px;
            height: 336px;
            border-radius: 36px 36px 22px 22px;
            background:
                radial-gradient(circle at 50% 18%, rgba(255,255,255,0.24), transparent 12%),
                linear-gradient(180deg, rgba(255,255,255,0.18), rgba(255,255,255,0)),
                linear-gradient(180deg, #272727 0%, #131313 100%);
            border: 1px solid rgba(255,255,255,0.14);
            transform: rotate(-6deg);
        }
        .section-title {
            font-size: 1.02rem;
            font-weight: 900;
            letter-spacing: 0.04rem;
            margin: 0.2rem 0 0.8rem 0;
        }
        .products-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
        }
        .product-card {
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(16,16,16,0.08);
            border-radius: 24px;
            padding: 16px;
            box-shadow: 0 10px 28px rgba(16,16,16,0.06);
        }
        .product-visual {
            height: 132px;
            border-radius: 18px;
            margin-bottom: 12px;
            background:
                radial-gradient(circle at 28% 18%, rgba(255,255,255,0.50), transparent 16%),
                linear-gradient(145deg, #222222 0%, #6f6f6b 100%);
        }
        .product-tag {
            display: inline-block;
            font-size: 0.70rem;
            font-weight: 900;
            letter-spacing: 0.08rem;
            background: #efefe9;
            border-radius: 999px;
            padding: 5px 10px;
            margin-bottom: 10px;
        }
        .product-name {
            font-size: 0.98rem;
            font-weight: 800;
            margin-bottom: 4px;
        }
        .product-price {
            font-size: 0.88rem;
            color: #50504c;
        }
        .assistant-panel {
            background: rgba(255,255,255,0.93);
            border: 1px solid rgba(16,16,16,0.08);
            border-radius: 32px;
            padding: 18px;
            box-shadow: 0 24px 70px rgba(16,16,16,0.10);
        }
        .assistant-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }
        .assistant-title {
            font-size: 1rem;
            font-weight: 900;
        }
        .assistant-status {
            border-radius: 999px;
            background: #eef3ee;
            color: #3d5240;
            padding: 7px 10px;
            font-size: 0.75rem;
        }
        .assistant-subcopy {
            font-size: 0.86rem;
            color: #5a5a55;
            margin-bottom: 12px;
        }
        .helper-card {
            border-radius: 18px;
            background: #f3f3ee;
            border: 1px solid rgba(16,16,16,0.06);
            padding: 12px 14px;
            font-size: 0.84rem;
            margin-bottom: 10px;
        }
        .helper-card strong {
            display: block;
            margin-bottom: 0.3rem;
        }
        .assistant-chat {
            background: linear-gradient(180deg, #fafaf8 0%, #f3f3ef 100%);
            border-radius: 24px;
            border: 1px solid rgba(16,16,16,0.06);
            padding: 14px 12px;
            min-height: 470px;
            max-height: 470px;
            overflow-y: auto;
            margin-bottom: 10px;
        }
        .message-row {
            display: flex;
            margin-bottom: 12px;
        }
        .message-row.user {
            justify-content: flex-end;
        }
        .message-bubble {
            max-width: 88%;
            border-radius: 20px;
            padding: 12px 14px;
            font-size: 0.92rem;
            line-height: 1.46;
            box-shadow: 0 8px 24px rgba(16,16,16,0.05);
        }
        .message-row.bot .message-bubble {
            background: #ffffff;
            border: 1px solid rgba(16,16,16,0.06);
            color: #111111;
            border-bottom-left-radius: 8px;
        }
        .message-row.user .message-bubble {
            background: #111111;
            color: #fafaf7;
            border-bottom-right-radius: 8px;
        }
        .message-meta {
            margin-top: 6px;
            color: #666660;
            font-size: 0.72rem;
        }
        .stTextInput input {
            border-radius: 999px !important;
            border: 1px solid rgba(16,16,16,0.10) !important;
            padding-left: 14px !important;
        }
        .stButton button {
            border-radius: 999px !important;
            background: #111111 !important;
            color: #fafaf7 !important;
            font-weight: 900 !important;
            border: 1px solid rgba(16,16,16,0.08) !important;
        }
        @media (max-width: 900px) {
            .hero-title { font-size: 2.3rem; }
            .products-grid { grid-template-columns: 1fr; }
            .assistant-chat { min-height: 360px; max-height: none; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_storefront() -> None:
    nav_html = "".join(f"<span class='brand-pill'>{item}</span>" for item in NAV_ITEMS)
    cards_html = "".join(
        f"""
        <div class="product-card">
            <div class="product-visual"></div>
            <span class="product-tag">{product['tag']}</span>
            <div class="product-name">{product['name']}</div>
            <div class="product-price">{product['price']}</div>
        </div>
        """
        for product in FEATURED_PRODUCTS
    )

    st.markdown(
        f"""
        <div class="brand-shell">
            <div class="brand-topbar">
                <div class="brand-name">COLDCULTURE</div>
                <div class="brand-nav">{nav_html}</div>
            </div>
        </div>
        <div class="hero-card">
            <div>
                <div class="hero-kicker">Streetwear / Assistant Experience</div>
                <div class="hero-title">A retail-inspired shell built to showcase the chatbot.</div>
                <div class="hero-copy">
                    The storefront gives context and atmosphere, but the core product remains the
                    hybrid assistant on the right.
                </div>
                <div class="hero-shop">SHOP</div>
            </div>
            <div class="hero-model"></div>
        </div>
        <div class="section-title">New In</div>
        <div class="products-grid">{cards_html}</div>
        """,
        unsafe_allow_html=True,
    )


def initialize_knowledge_base() -> None:
    if st.session_state.get("document_ready", False):
        return

    try:
        ingestion_pipeline = IngestionPipeline()
        chunk_count = ingestion_pipeline.ingest_file(DEFAULT_FAQ_PATH)

        st.session_state["document_ready"] = True
        st.session_state["indexed_file"] = "faq.txt"
        st.session_state["index_version"] = st.session_state.get("index_version", 0) + 1
        st.session_state["knowledge_status"] = (
            f"FAQ knowledge base ready ({chunk_count} chunks indexed)."
        )
    except Exception as exc:
        st.session_state["knowledge_status"] = f"Knowledge base error: {exc}"


def render_chat_history(show_passages: bool) -> None:
    st.markdown(
        """
        <div class="assistant-header">
            <div class="assistant-title">Shopping Assistant</div>
            <div class="assistant-status">Live FAQ + Catalog</div>
        </div>
        <div class="assistant-subcopy">Hello! How can I help you?</div>
        <div class="helper-card">
            <strong>Ask about anything</strong>
            Delivery, returns, refunds, sizes, colors, price filters, or stock availability.
        </div>
        """,
        unsafe_allow_html=True,
    )

    history = st.session_state.get("chat_history", [])
    chat_box = st.container(height=470)
    with chat_box:
        if not history:
            st.markdown(
                """
                <div class="message-row bot">
                    <div class="message-bubble">
                        Hello! How can I help you?
                        <div class="message-meta">
                            Try: "Avez-vous des sneakers noires en 42 ?"
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            for message in history:
                if message["role"] == "user":
                    st.markdown(
                        f"""
                        <div class="message-row user">
                            <div class="message-bubble">{message['content']}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    continue

                meta = (
                    f"Routing: {message['route']} | "
                    f"support={message['routing']['support_score']} | "
                    f"catalog={message['routing']['product_score']}"
                )
                assistant_content = message["content"].replace("\n", "<br>")
                st.markdown(
                    f"""
                    <div class="message-row bot">
                        <div class="message-bubble">
                            {assistant_content}
                            <div class="message-meta">{meta}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    if not history:
        return

    last_assistant_message = None
    for message in reversed(history):
        if message["role"] == "assistant":
            last_assistant_message = message
            break

    if not last_assistant_message or not show_passages:
        return

    if last_assistant_message["route"] == "support":
        with st.expander("Retrieved support passages"):
            for index, passage in enumerate(last_assistant_message["details"]["passages"], start=1):
                st.markdown(
                    f"**Passage {index}**  \n"
                    f"Source : `{passage['source']}`  \n"
                    f"Score : `{passage['score']:.4f}`"
                )
                st.write(passage["content"])
    else:
        with st.expander("Catalog details"):
            st.write("Filtres extraits :", last_assistant_message["details"]["filters"])
            st.write(last_assistant_message["details"]["formatted_results"])

    st.caption("Sources")
    for source in last_assistant_message["sources"]:
        st.write(f"- {source}")


def handle_question() -> None:
    show_passages = st.checkbox("Show technical details", value=False)
    render_chat_history(show_passages=show_passages)

    with st.form("chat_form", clear_on_submit=True):
        input_col, send_col = st.columns([5, 1])
        with input_col:
            question = st.text_input(
                "Message",
                label_visibility="collapsed",
                placeholder="Ask about delivery, returns, products, sizes, or pricing...",
            )
        with send_col:
            submitted = st.form_submit_button("➜", use_container_width=True)

    if not submitted:
        return

    if not question.strip():
        st.warning("Entre une question avant de lancer la recherche.")
        return

    if not st.session_state.get("document_ready", False):
        st.warning("La FAQ n'est pas prete.")
        return

    st.session_state["chat_history"].append({"role": "user", "content": question})

    try:
        assistant_pipeline = get_assistant_pipeline(st.session_state.get("index_version", 0))
        result = assistant_pipeline.ask(
            query=question,
            history=st.session_state["chat_history"][:-1],
        )

        st.session_state["chat_history"].append(
            {
                "role": "assistant",
                "content": result["answer"],
                "route": result["route"],
                "routing": result["routing"],
                "details": result["details"],
                "sources": result["sources"],
            }
        )
        st.rerun()
    except Exception as exc:
        st.error(f"Erreur pendant la generation de la reponse : {exc}")


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon=":speech_balloon:", layout="wide")
    inject_styles()

    if "document_ready" not in st.session_state:
        st.session_state["document_ready"] = False
    if "index_version" not in st.session_state:
        st.session_state["index_version"] = 0
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    initialize_knowledge_base()

    left_col, right_col = st.columns([1.65, 1], gap="large")

    with left_col:
        render_storefront()

    with right_col:
        st.markdown('<div class="assistant-panel">', unsafe_allow_html=True)
        knowledge_status = st.session_state.get("knowledge_status")
        if knowledge_status:
            st.caption(knowledge_status)
        handle_question()
        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
