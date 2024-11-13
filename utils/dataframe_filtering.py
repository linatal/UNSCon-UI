import pandas.api.types
import pandas as pd
import streamlit as st
from css_styles.button import button
from css_styles.notbold import notbold



def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """

    '''for later when working with css: 
    if modify:
        st.write(button, unsafe_allow_html=True)
    if not modify:
        st.write(button, unsafe_allow_html=True)
        return df
    '''
    #modify = st.checkbox("Add filters")
    # Make a copy of the pandas dataframe so the user input will not change the underlying data.
    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if pandas.api.types.is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col], format="%d %B %Y").dt.date
            except Exception:
                pass
        if pandas.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)
    # Set up a container with st.container for your filtering widgets
    modification_container = st.container()

    with modification_container:
        # Use st.multiselect to let the user select the columns
        to_filter_columns = st.multiselect(r"$\textsf{\Large Filter dataframe on: }$", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            dtype = df[column].dtype
            if isinstance(dtype, pd.CategoricalDtype) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif pandas.api.types.is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif pandas.api.types.is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
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
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df