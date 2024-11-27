import streamlit as st
import pandas as pd
from utils.helper import define_dtypes

# ---DF input
def get_data():
    df_input = pd.read_csv("./dataset/conflict_annotations4UI.csv", index_col=0)
    df_input = define_dtypes(df_input) # achtung: including NaNs with dtype definition
    return df_input



def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns.

    Args:
        df (pd.DataFrame): Original dataframe.

    Returns:
        pd.DataFrame: Either the full dataframe (no filters applied or reset clicked),
                      or the filtered dataframe (filters applied).
    """
    # Make a copy of the pandas dataframe so user input doesn't modify the original data
    df_original = df.copy()

    # Sidebar section
    st.sidebar.success("Apply global filters for Tables and Sankeyflow 👇")

    # Initialize session state for filters and reset logic
    if "filters" not in st.session_state:
        st.session_state.filters = {}
    if "reset_clicked" not in st.session_state:
        st.session_state.reset_clicked = False

    # Reset Filters button
    if st.sidebar.button("Reset Filters"):
        st.session_state.filters = {}  # Clear all stored filters
        st.session_state.reset_clicked = True  # Mark reset button as clicked

    # Determine the working dataframe
    if st.session_state.reset_clicked:
        # If reset button clicked, use the full dataframe
        df_to_display = df_original
        st.session_state.reset_clicked = False  # Reset the flag for subsequent interactions
    else:
        # Apply filters to the dataframe
        df_to_display = df.copy()

    # List of columns to filter
    columns_df = ['Conflict Type', 'Conflict Target Group', 'Conflict Target Group 2',
                  'Conflict Target Intermediate', 'Target Country', 'Target Country 2', 'Country Speaker',
                  'Speech-ID filename', 'Speaker Country', 'Participant-Type', 'Date of Debate']

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in columns_df:
        if pd.api.types.is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col], format="%d %B %Y").dt.date
            except Exception:
                pass
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    # Filtering widgets
    with st.container():
        # Use st.multiselect to let the user select the columns to filter
        to_filter_columns = st.sidebar.multiselect("Filter dataframe on:", df.columns)

        for column in to_filter_columns:
            dtype = df[column].dtype

            if isinstance(dtype, pd.CategoricalDtype) or df[column].nunique() < 10:
                user_cat_input = st.sidebar.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=st.session_state.filters.get(column, list(df[column].unique())),
                )
                st.session_state.filters[column] = user_cat_input
                df_to_display = df_to_display[df_to_display[column].isin(user_cat_input)]

            elif pd.api.types.is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = st.sidebar.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=st.session_state.filters.get(column, (_min, _max)),
                    step=step,
                )
                st.session_state.filters[column] = user_num_input
                df_to_display = df_to_display[df_to_display[column].between(*user_num_input)]

            elif pd.api.types.is_datetime64_any_dtype(df[column]):
                user_date_input = st.sidebar.date_input(
                    f"Values for {column}",
                    value=st.session_state.filters.get(column, (df[column].min(), df[column].max())),
                )
                st.session_state.filters[column] = user_date_input
                if len(user_date_input) == 2:
                    start_date, end_date = tuple(pd.to_datetime(user_date_input).date)
                    df_to_display = df_to_display.loc[df_to_display[column].between(start_date, end_date)]

            else:
                user_text_input = st.sidebar.text_input(
                    f"Substring or regex in {column}",
                    value=st.session_state.filters.get(column, ""),
                )
                st.session_state.filters[column] = user_text_input
                if user_text_input:
                    df_to_display = df_to_display[df_to_display[column].astype(str).str.contains(user_text_input)]

    # If no filters are applied and reset wasn't clicked, return the original dataframe
    if df_to_display.equals(df_original):
        return df_original

    # Return the filtered dataframe (if filters applied)
    return df_to_display

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    st.sidebar.success("Use the navigation menu to switch between demos.👇")
    page = st.sidebar.selectbox(
        "Select a Demo Page",
        options=["Homepage", "Tables and Labels Distribution", "Sankeyflow"],
        key = "global_navigation_selectbox"
    )

    return page