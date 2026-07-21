import streamlit as st


def display_xmr_intro():
    with open("content/xmr_intro.md", "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("\n\n")

    for part in parts:
        if part == "[FIGURE_1]":
            _, col_mid, _ = st.columns([0.75, 2, 0.75])
            with col_mid:
                st.image(
                    "figures/Fig_xmr_chart_app_figure_1.png",
                    use_container_width=True,
                    caption="Figure 1. What do you want to accomplish?"
                )

        elif part == "[FIGURE_2]":
            _, col_mid, _ = st.columns([0.75, 2, 0.75])
            with col_mid:
                st.image(
                    "figures/Fig_xmr_chart_example.png",
                    use_container_width=True,
                    caption="Figure 2. A simple XmR chart."
                )

        elif part == "[FIGURE_3]":
            _, col_mid, _ = st.columns([0.5, 2, 0.5])
            with col_mid:
                st.image(
                    "figures/Fig_is_all_the_data_within_limits.png",
                    use_container_width=True,
                    caption="Figure 3. When one or more values fall outside the process limits, a process is characterized as unpredictable."
                )
        
        elif part == "[BUTTON_1]":
            st.markdown(
                """
                <div class="store-button-wrapper">
                    <a href="https://www.brokenquality.com/" target="_blank">
                        <button class="store-button">Click here to learn more!</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.markdown(part)
    
    st.divider()