import streamlit as st

from data.loader import load_uploaded_dataset, load_sample_dataset, resolve_columns
from components.dataset_selector import (
    render_upload_selectors,
    render_sample_selectors,
    render_stage_customization
)
from components.charts import create_xmr_chart
from components.chart_annotations import add_process_limit_lines, add_process_limit_annotations
from components.chart_stages import add_stage_traces, add_stage_boundaries, add_stage_labels
from calculations.xmr_limits import calculate_xmr_limits


def render_tab1(dataset_columns, dataset_questions):
    st.markdown("### Select a dataset or upload a CSV file")

    if "default_tick_interval" not in st.session_state:
        st.session_state.default_tick_interval = 5

    name_to_file = {v["name"]: k for k, v in dataset_columns.items()}

    col1, col2 = st.columns(2)

    with col1:
        selected_name = st.selectbox(
            "**Select a sample dataset**",
            ["None"] + list(name_to_file.keys()),
            key="sample_dataset"
        )

    with col2:
        uploaded_file = st.file_uploader(
            "**Upload your own dataset (CSV)**",
            type="csv",
            key="uploaded_csv"
        )


    # Default value when using uploaded CSV
    selected_file = "None"


    # --- Warn if both sources are selected ---
    if uploaded_file is not None and selected_name != "None":
        st.warning(
            "A CSV file has already been uploaded. "
            "Please remove the uploaded file before selecting a sample dataset."
        )

        df = load_uploaded_dataset(uploaded_file)

    elif uploaded_file is not None:
        df = load_uploaded_dataset(uploaded_file)

    elif selected_name != "None":
        selected_file = name_to_file[selected_name]
        df = load_sample_dataset(selected_file, dataset_columns)

    else:
        df = None


    if df is None:
        st.info("To generate an XmR chart, select a dataset or upload a CSV.")
        return

    # --- COLUMN SELECTION ---
    if uploaded_file is not None:
        data_column, label_column, stage_column = render_upload_selectors(df)
    else:
        description = dataset_columns.get(selected_file, {}).get("description")
        st.divider()
        if description:
            st.markdown(
                f"### Selected dataset: <span style='color:#d72323'>{dataset_columns[selected_file]['name']}</span>",
                unsafe_allow_html=True
            )
            st.markdown(description)

        data_column, label_column, stage_column = render_sample_selectors(df, selected_file, dataset_columns)

    data, label_column_data, is_valid = resolve_columns(df, data_column, label_column)

    if not is_valid:
        st.warning("Please select both a data column and a label column.")
        return   
    
    st.divider()
    st.markdown("### XmR Chart")

    with st.expander("XmR Chart Display Controls"):
        col4, col5, col6 = st.columns(3)
        tick_interval = col4.number_input("Tick Interval (X)", min_value=1, step=1, key="tick_interval")
        round_value = col5.number_input("Number of Decimal Places", min_value=0, value=1, step=1, key="rounding_value")
        tick_angle = col6.number_input("X-Axis Tick Label Angle", min_value=0, value=0, step=15)

        col7, col8, col9, col10, col11 = st.columns(5)
        show_limits = col7.checkbox("Show Process Limits", value=True)
        show_annotations = col8.checkbox("Show Annotations", value=True)
        show_lines = col9.checkbox("Show Connecting Lines", value=True)
        bound_UPL = col10.checkbox("Bound UPL", value=False)
        bound_LPL = col11.checkbox("Bound LPL", value=True)

        col12, col13, col14, col15, spacer = st.columns([1,1,1,1,1])
        rule_2 = col12.checkbox("Apply Detection Rule #2", value=False)
        rule_3 = col13.checkbox("Apply Detection Rule #3", value=False)
        marker_size = col14.number_input(
            "Change marker size",
            min_value=0,
            max_value=15,
            value=8,
            step=1)
        figure_height = col15.number_input(
            "Change figure height",
            min_value=300,
            max_value=600,
            value=500,
            step=50
        )

    line_mode = "lines+markers" if show_lines else "markers"

    show_stages, show_stage_labels, custom_stage_labels, stage_tick_intervals, stages, unique_stages = (
        render_stage_customization(df, stage_column, tick_interval, selected_file)
    )

    if selected_file is not None and selected_file in dataset_questions:

        with st.expander("Questions to consider"):
            for q in dataset_questions[selected_file]:
                selected = st.radio(
                    q["question"],
                    index=None,
                    options=q["options"],
                    key=q["key"]
                )

                if selected == q["answer"]:
                    st.success(f"✅ Correct! {q['explanation']}")
                elif selected is not None:
                    st.error("❌ Not quite. Try again.")

    # --- CALCULATIONS ---
    limits = calculate_xmr_limits(data, bound_upl=bound_UPL, bound_lpl=bound_LPL)
    mean, moving_range, ave_mR, UPL, LPL, URL = (
        limits["mean"], limits["moving_range"], limits["ave_mr"],
        limits["UPL"], limits["LPL"], limits["URL"]
    )

    # --- CHART ---
    fig = create_xmr_chart(
        data=data, moving_range=moving_range, marker_size=marker_size,
        figure_height=figure_height, mean=mean, UPL=UPL, LPL=LPL, URL=URL, ave_mR=ave_mR,
        show_limits=show_limits, rule_2=rule_2, rule_3=rule_3, line_mode=line_mode
    )

    if not show_stages:
        fig = add_process_limit_lines(fig, mean, UPL, LPL, ave_mR, URL, show_limits)
        fig = add_process_limit_annotations(fig, mean, UPL, LPL, ave_mR, URL, round_value, show_annotations)
    elif stage_column is not None:
        fig = add_stage_traces(fig, data, stages, unique_stages, show_limits, rule_2, rule_3, line_mode)
        fig = add_stage_boundaries(fig, stages)
        fig = add_stage_labels(fig, stages, unique_stages, custom_stage_labels, show_stage_labels)

    st.plotly_chart(fig, use_container_width=True)