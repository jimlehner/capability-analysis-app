import streamlit as st

from components.sidebar import display_sidebar
from components.capability_analysis import display_capability_analysis
# from components.xmr_chart_tab1 import render_tab1
from components.capability_index_overview import display_index_overview
from components.additional_resources import display_resources
from components.index_formulas import display_index_formulas

from components.charts import build_process_histogram

from config.datasets import dataset_columns
from config.questions import dataset_questions

im = "📈"
st.set_page_config(
    page_title="Honest Capability Analysis",
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
st.title("Honest Process Capability Analysis")

st.markdown("### A web app for calculating the process capability indices from [The Math Matters](https://themathmatters.substack.com) and [The Broken Quality Initiative](https://www.brokenquality.com/)")

# --- SIDEBAR ---
display_sidebar()

# --- TAB SELECTION ---
tab1, tab2, tab3, tab4 = st.tabs(["Process Capability Analysis",
                                  "An Overview of the Indices", 
                                  "The Formulas",
                                  "Additional Resources"])

# --- TAB1: PROCESS CAPABILITY CALCULATIONS ---
with tab1:
    display_capability_analysis(dataset_columns)
    # render_tab1(dataset_columns, dataset_questions)

# --- TAB2: AN OVERVIEW OF THE INDICES ---
with tab2:
    display_index_overview()

# --- TAB3: THE PROCESS CAPABILITY INDEX FORMULAS ---
with tab3:
    display_index_formulas()

# --- TAB4: ADDITIONAL RESOURCES ---
with tab4:
    display_resources()
