import streamlit as st

from components.sidebar import display_sidebar
from components.xmr_chart_tab1 import render_tab1
from components.xmr_intro import display_xmr_intro
from components.additional_resources import display_resources
from components.limit_formulas import display_limit_formulas

from config.datasets import dataset_columns
from config.questions import dataset_questions

im = "📈"
st.set_page_config(
    page_title="XmR Chart-It",
    page_icon=im,
    initial_sidebar_state='auto',
    layout="wide"
)

# Css styling
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css("styles.css")


# --- HEADER ---
st.title("XmR Chart-It")

st.markdown("### A web app for generating XmR charts from [The Broken Quality Initiative](https://www.brokenquality.com/)")

# --- SIDEBAR ---
display_sidebar()

# --- TAB SELECTION ---
tab1, tab2, tab3, tab4 = st.tabs(["XmR Chart",
                                  "An Introduction to XmR Charts", 
                                  "Process Limit Formulas",
                                  "Additional Resources"])

# --- TAB1: XMR CHART ---
with tab1:
    render_tab1(dataset_columns, dataset_questions)

# --- TAB2: AN INTRO TO XMR CHARTS ---
with tab2:
    display_xmr_intro()

# --- TAB3: PROCESS LIMIT FORMULAS ---
with tab3:
    display_limit_formulas()

# --- TAB4: ADDITIONAL RESOURCES ---
with tab4:
    display_resources()
