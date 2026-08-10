import streamlit as st

def display_resources():

    col1, col2 = st.columns([1, 1])

    with col1:
        with open("content/virus_of_variation.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())

        st.markdown(
            """
            <div class="store-button-wrapper">
                <a href="https://www.brokenquality.com/store/p/virus-of-variation-epub" target="_blank">
                    <button class="store-button">Get the Book</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image(
            "figures/virus_of_variation_cover.png",
            use_container_width=True
        )

    st.divider()

    col3, col4 = st.columns([1, 1])

    with col3:
        with open("content/taguchi_loss.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())

        st.markdown(
            """
            <div class="store-button-wrapper">
                <a href="https://taguchiloss.streamlit.app/" target="_blank">
                    <button class="store-button">Try the Taguchi Loss Calculator</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.image("figures/taguchi_loss_distribution.png")

    st.divider()

    col5, col6 = st.columns([1, 1])

    with col5:
        with open("content/understanding_process_cap.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())

        st.markdown(
            """
            <div class="store-button-wrapper">
                <a href="https://www.brokenquality.com/store/p/understanding-process-capability-epub" target="_blank">
                    <button class="store-button">Get the EPUB</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col6:
        st.image("figures/understand_process_cap.png")

    st.divider()

    col7, col8 = st.columns([1, 1])

    with col7:
        with open("content/characterization_flowchart.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())

        st.markdown(
            """
            <div class="store-button-wrapper">
                <a href="https://www.brokenquality.com/store/p/characterization-flowchart-pdf" target="_blank">
                    <button class="store-button">Get the PDF</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col8:
        st.image("figures/characterization_flowchart.png")
    
    st.divider()