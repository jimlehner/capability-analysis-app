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

im = "🔬"
st.set_page_config(
    page_title="Honest Capability Analysis",
    page_icon=im,
    initial_sidebar_state='collapsed',
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

with st.expander("What makes capability analysis honest?"):
    st.write("The four standard indexes in common use today are the capability ratio (Cp), centered capability ratio (Cpk), performance ratio (Pp), and centered " \
    "performance ratio (Ppk). Collectively, these four indexes incorporate all of the information describing the relationship between the process and the specifications. " \
    "Over the years, additional numerical summaries have been created. They are unnecessary. If you want to perform an honest capability analysis, it will use only " \
    " these four indicies. Let me explain.")

    st.write("Many have been taught that the capability indexes only apply when a dataset is normally distributed. But nothing in the formulas makes any demand " \
    "upon the shape of the histogram (See [Does Capability Require Normality?](https://www.spcpress.com/pdf/2025/403Sep22DoesCapablityRequireNormality.pdf) by Donald J. Wheeler). " \
    "As functions of the data, the capability and " \
    "performance indexes have no preference for one probability model over the other. In fact, the uncertainties associated with different probability models make the " \
    "discussion of which model to use an argument over noise. Taking into account the inherent uncertainties of different models, they end up being indistingusihable "
    "(See [Converting Capabilities: What difference does the probability model make?](https://www.spcpress.com/pdf/DJW404.pdf) by Donald J. Wheeler).")

    st.write("So what makes a process capability analysis honest? The analysis is honest when it uses the four indexes listed above and does not assert that a specific " \
    "proabability model will produce more accurate results. All proabability models are unverified assumptions that allow for the computation of infinitesimal areas in " \
    "the extreme tails, but these computations do not represent reality.")

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
