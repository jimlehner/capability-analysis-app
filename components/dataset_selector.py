import streamlit as st
from data.loader import safe_index


def render_upload_selectors(df):
    """Column pickers for a user-uploaded CSV. Returns (data_col, label_col, stage_col)."""
    col1, col2, col3 = st.columns(3)

    data_column = col1.selectbox(
        "Select the data column of the uploaded CSV",
        [None] + list(df.columns), index=0
    )
    USL = col2.input(
        "Enter Upper Specification Limit (USL)",
        [None, "Default (1 to n)"] + list(df.columns), index=0
    )
    LSL = col3.number_input(
        "Enter Lower Specification Limit (LSL)",
        ["Not Applicable"] + list(df.columns), index=0
    )

    return data_column, USL, LSL


def render_sample_selectors(df, selected_file, dataset_columns):
    """Column pickers for a bundled sample dataset. Returns (data_col, label_col, stage_col)."""
    cfg = dataset_columns.get(selected_file, {})

    # Only reset tick_interval when the dataset selection actually changes —
    # prevents stomping the user's manual edits on every unrelated rerun.
    if st.session_state.get("last_selected_file") != selected_file:
        st.session_state.tick_interval = cfg.get("tick_interval", 5)
        st.session_state.last_selected_file = selected_file

    col1, col2, col3 = st.columns(3)

    data_column = col1.selectbox(
        "Select the data column", df.columns,
        index=safe_index(df.columns, cfg.get("data"), default=0)
    )
    USL = col2.number_input(
        "Enter Upper Specification Limit (USL)",
        value=float(cfg.get("USL", 0))
    )

    LSL = col3.number_input(
        "Enter Lower Specification Limit (LSL)",
        value=float(cfg.get("LSL", 0))
    )

    return data_column, USL, LSL