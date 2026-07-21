import streamlit as st
from data.loader import safe_index


def render_upload_selectors(df):
    """Column pickers for a user-uploaded CSV. Returns (data_col, label_col, stage_col)."""
    col1, col2, col3 = st.columns(3)

    data_column = col1.selectbox(
        "Select the data column of the uploaded CSV",
        [None] + list(df.columns), index=0
    )
    label_column = col2.selectbox(
        "Select the label column of the uploaded CSV",
        [None, "Default (1 to n)"] + list(df.columns), index=0
    )
    stage_column = col3.selectbox(
        "Select the stage column of the uploaded CSV (if applicable)",
        ["Not Applicable"] + list(df.columns), index=0
    )

    stage_column = None if stage_column == "Not Applicable" else stage_column
    return data_column, label_column, stage_column


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
    label_column = col2.selectbox(
        "Select the label column", df.columns,
        index=safe_index(df.columns, cfg.get("label"))
    )
    stage_column = col3.selectbox(
        "Select the stage column", [None] + list(df.columns),
        index=safe_index([None] + list(df.columns), cfg.get("stage"), default=0)
    )

    return data_column, label_column, stage_column


def render_stage_customization(df, stage_column, tick_interval, selected_file):
    """Stage View & Customization expander. Returns (show_stages, show_stage_labels, custom_labels, stage_ticks, stages, unique_stages)."""
    if stage_column is None:
        return False, True, {}, {}, None, []

    stages = df[stage_column].reset_index(drop=True)
    unique_stages = stages.unique()
    custom_stage_labels = {}
    stage_tick_intervals = {}

    with st.expander("Stage View & Customization"):
        st.markdown(
            """
            A stage is a distinct period of time in which a process was operated under different conditions.
            This can be the result of an intentional or unintentional change to the underlying causal system.
            Evaluating a process in accordance with stages using XmR charts allows for direct visual comparison
            between the different stages. It reveals if and how much the variation has changed between stages
            as well as if there have been any shifts in the mean.
            """
        )

        col1, col2, col3, col4 = st.columns([1, 1, 3, 3])
        show_stages = col1.checkbox("Show Stages", value=False)
        show_stage_labels = col2.checkbox("Show Stage Labels", value=True)

        if show_stages:
            stage_cols = st.columns(len(unique_stages))
            for i, stage in enumerate(unique_stages):
                if show_stage_labels:
                    custom_stage_labels[stage] = stage_cols[i].text_input(
                        f"Stage {i+1} label",
                        value=str(stage),
                        key=f"stage_label_{selected_file}_{i}"
                    )
                stage_tick_intervals[stage] = stage_cols[i].number_input(
                    f"Stage {i+1} tick interval",
                    min_value=1, value=tick_interval, step=1,
                    key=f"stage_tick_{selected_file}_{i}"
                )

    return show_stages, show_stage_labels, custom_stage_labels, stage_tick_intervals, stages, unique_stages