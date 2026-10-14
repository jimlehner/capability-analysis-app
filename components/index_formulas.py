import streamlit as st

def load_markdown(filename):
    with open(f"content/{filename}", "r", encoding="utf-8") as f:
        return f.read()

def display_markdown_file(filename):
    content = load_markdown(filename)
    parts = content.split("\n\n")

    figures = {
        "[FIGURE_TOLERANCE]": "figures/EQ_tolerance.png",
        "[FIGURE_DNS]": "figures/EQ_DNS.png",
        "[FIGURE_SIGMAX]": "figures/EQ_sigmax.png",
        "[FIGURE_SD]": "figures/EQ_Global_SD.png",
    }

    for part in parts:
        if part in figures:
            _, col_mid, _ = st.columns([0.75, 2, 0.75])

            with col_mid:
                st.image(
                    figures[part],
                    use_container_width=True
                )
        else:
            st.markdown(part, unsafe_allow_html=True)

def display_index_formulas():
    with open("content/index_formulas.md", "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("\n\n")

    for part in parts:
        if part == "[FIGURE_1]":
            _, col_mid, _ = st.columns([0.75, 2, 0.75])
            with col_mid:
                st.image(
                    "figures/EQ_process_capability_formulas.png",
                    use_container_width=True,
                    caption=""
                )

        elif part == "[FORMULA_TABS]":
            tab1, tab2, tab3, tab4 = st.tabs([
                "Specified Tolerance",
                "DNS",
                "Sigma(X)",
                "Global Standard Deviation"
            ])

            with tab1:
                display_markdown_file("quantities_specified_tolerance.md")

            with tab2:
                display_markdown_file("quantities_dns.md")

            with tab3:
                display_markdown_file("quantities_sigmax.md")

            with tab4:
                display_markdown_file("quantities_standard_deviation.md")

        else:
            st.markdown(part)