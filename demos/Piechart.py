import pandas as pd
import seaborn as sns
import streamlit as st
from utils.helper import local_css


def render_piechart(df_filter, df):

    # Apply CSS
    local_css("style.css")

    # ---Text Body
    st.title("Interactive Pie Chart")
    st.subheader("""Showing Conflict Types used by Countries the UNSCon Corpus""")

    # ---prepare corpus

    # only rows with conflict
    df = df.loc[df['Conflict Type'].notna()]
    df = df[['Conflict_Type', 'country','Target_Country']]
    df = df.fillna('Underdefined')

    # choose on country
    sorted_speaker = sorted(set(df['country'].to_list()))
    sorted_target = sorted(set(df['Target_Country'].to_list()))


    st.pyplot(df["Conflict_Type"].value_counts().plot.pie())
    st.markdown("----")
    num_rows = df.shape
    st.write(f"Number of sentences: {num_rows[0]}  ")
