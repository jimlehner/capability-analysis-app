import pandas as pd


def load_uploaded_dataset(uploaded_file):
    """Read an uploaded CSV once. Returns a DataFrame or None."""
    if uploaded_file is None:
        return None
    return pd.read_csv(uploaded_file)


def load_sample_dataset(selected_file, dataset_columns):
    """Read a bundled example CSV. Returns a DataFrame or None."""
    if selected_file == "None":
        return None
    return pd.read_csv(f"data/examples/{selected_file}")


def resolve_columns(df, data_column, label_column):
    """
    Validate + extract the data/label series from a DataFrame.
    Returns (data, label_data, is_valid). Never partially computes —
    if either column is missing, data/label_data are both None.
    """
    if data_column is None or label_column is None:
        return None, None, False

    data = df[data_column].dropna().reset_index(drop=True)

    if label_column == "Default (1 to n)":
        label_data = list(range(1, len(df) + 1))
    else:
        label_data = df[label_column].tolist()

    return data, label_data, True


def safe_index(options, value, default=None):
    """Find value's index in options, or fall back to default instead of crashing."""
    options = list(options)
    return options.index(value) if value in options else default

# import pandas as pd
# import streamlit as st


# def extract_dataset_columns(df, data_column, label_column, stage_column):
#     """
#     Extract data, labels, and stages from a dataframe based on user selections.
#     """

#     if data_column is None:
#         st.warning("Please select a data column.")
#         return None, None, None

#     # Extract measurement data
#     data = (
#         df[data_column]
#         .dropna()
#         .reset_index(drop=True)
#     )

#     # Extract labels
#     if label_column == "Default (1 to n)":
#         labels = list(range(1, len(data) + 1))

#     elif label_column is not None:
#         labels = df[label_column].tolist()

#     else:
#         labels = list(range(1, len(data) + 1))

#     # Extract stages
#     if stage_column in ["Not Applicable", None]:
#         stages = None

#     else:
#         stages = df[stage_column].tolist()

#     return data, labels, stages


# def load_uploaded_dataset(uploaded_file):
#     """
#     Load a user-uploaded CSV file.
#     """

#     df = pd.read_csv(uploaded_file)

#     col1, col2, col3 = st.columns(3)

#     data_column = col1.selectbox(
#         "Select the data column of the uploaded CSV",
#         [None] + list(df.columns)
#     )

#     label_column = col2.selectbox(
#         "Select the label column of the uploaded CSV",
#         [None, "Default (1 to n)"] + list(df.columns)
#     )

#     stage_column = col3.selectbox(
#         "Select the stage column of the uploaded CSV",
#         ["Not Applicable"] + list(df.columns)
#     )

#     data, labels, stages = extract_dataset_columns(
#         df,
#         data_column,
#         label_column,
#         stage_column
#     )

#     return {
#         "df": df,
#         "data": data,
#         "labels": labels,
#         "stages": stages,
#         "filename": None
#     }


# def load_sample_dataset(selected_file, dataset_columns):
#     """
#     Load one of the built-in example datasets.
#     """

#     df = pd.read_csv(f"data/examples/{selected_file}")

#     config = dataset_columns[selected_file]

#     # Display dataset description
#     description = config.get("description")

#     if description:

#         st.divider()

#         st.markdown(
#             f"### Selected dataset: "
#             f"<span style='color:#d72323'>{config['name']}</span>",
#             unsafe_allow_html=True
#         )

#         st.markdown(description)


#     col1, col2, col3 = st.columns(3)

#     default_data = config.get("data")
#     default_label = config.get("label")
#     default_stage = config.get("stage")


#     data_column = col1.selectbox(
#         "Select the data column",
#         df.columns,
#         index=df.columns.get_loc(default_data)
#         if default_data in df.columns
#         else 0
#     )

#     label_column = col2.selectbox(
#         "Select the label column",
#         df.columns,
#         index=df.columns.get_loc(default_label)
#         if default_label in df.columns
#         else 0
#     )

#     stage_options = [None] + list(df.columns)

#     stage_column = col3.selectbox(
#         "Select the stage column",
#         stage_options,
#         index=(
#             stage_options.index(default_stage)
#             if default_stage in stage_options
#             else 0
#         )
#     )


#     data, labels, stages = extract_dataset_columns(
#         df,
#         data_column,
#         label_column,
#         stage_column
#     )


#     return {
#         "df": df,
#         "data": data,
#         "labels": labels,
#         "stages": stages,
#         "filename": selected_file
#     }