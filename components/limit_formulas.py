import streamlit as st


def display_limit_formulas():
    with open("content/limit_formulas.md", "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("\n\n")

    for part in parts:
        if part == "[FIGURE_1]":
            _, col_mid, _ = st.columns([0.75, 2, 0.75])
            with col_mid:
                st.image(
                    "figures/EQ_UPL_LPL.png",
                    use_container_width=True,
                    caption=""
                )

        elif part == "[FIGURE_2]":
            _, col_mid, _ = st.columns([0.75, 2, 0.75])
            with col_mid:
                st.image(
                    "figures/EQ_URL.png",
                    use_container_width=True,
                    caption=""
                )

        elif part == "[BUTTON_1]":
            st.markdown(
                """
                <div class="store-button-wrapper">
                    <a href="https://www.brokenquality.com/bookshelf/p/how-to-build-an-xmr-chart-epub" target="_blank">
                        <button class="store-button">Click here to learn more!</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.markdown(part)
    
    st.divider()

        