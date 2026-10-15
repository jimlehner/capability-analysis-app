import streamlit as st

def read_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def display_sidebar():

    with st.sidebar:
        
        st.image(
            "figures/mathmatters_logo.png",
            use_container_width=True
        )
        
        st.markdown(read_markdown("content/sidebar_project.md"))

        st.markdown(read_markdown("content/sidebar_author.md"))
        st.markdown(read_markdown("content/sidebar_contact.md"))
        st.markdown(read_markdown("content/sidebar_socials.md"))
        st.markdown(read_markdown("content/sidebar_website.md"))