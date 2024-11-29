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
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    # Make a copy of the pandas dataframe so the user input will not change the underlying data.
    df = df.copy()
    st.sidebar.title("Filter")
    st.sidebar.write("Apply global filters for Tables and Sankeyflow 👇")
    # customize
    columns_df = ['Conflict Type', 'Conflict Target Group', 'Conflict Target Group 2',
                  'Conflict Target Intermediate', 'Target Country', 'Target Country 2', 'Country Speaker',
                  'Speech-ID filename', 'Speaker Name', 'Participant-Type', 'Date of Debate']

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in columns_df:
        if pd.api.types.is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col], format="%d %B %Y").dt.date
            except Exception:
                pass
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)
    # Set up a container with st.container for your filtering widgets
    modification_container = st.container()

    with modification_container:
        # Use st.multiselect to let the user select the columns
        #to_filter_columns = st.sidebar.multiselect(r"$\textsf{\normalsize Filter dataframe on: }$", df.columns)
        to_filter_columns = st.sidebar.multiselect("Filter dataframe on:", df.columns)
        for column in to_filter_columns:
            # left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            dtype = df[column].dtype
            if isinstance(dtype, pd.CategoricalDtype) or df[column].nunique() < 10:
                # Display multiselect in the sidebar
                user_cat_input = st.sidebar.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif pd.api.types.is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = st.sidebar.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif pd.api.types.is_datetime64_any_dtype(df[column]):
                user_date_input = st.sidebar.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime.dt.date, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = st.sidebar.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    st.sidebar.markdown(
        '''Filter mechanism is adopted in a modified form from the blog [here]("https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/").''')
    return df

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    #st.sidebar.success("Use the navigation menu to switch between demos.👇")
    st.sidebar.write("Use the navigation menu to switch between demos.👇")
    page = st.sidebar.selectbox(
        "Select a Demo Page",
        options=["Homepage", "Table", "Barchart", "Sankeyflow", "Piechart", "Guidelines Filters"],
        key = "global_navigation_selectbox"
    )

    return page