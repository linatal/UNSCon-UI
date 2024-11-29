import pandas as pd
import seaborn as sns
import streamlit as st
from utils.helper import local_css
import plotly.express as px


def render_piechart(df):

    # Apply CSS
    local_css("style.css")

    # ---Text Body
    st.title("Interactive Pie Chart")
    st.subheader("""Showing Conflict Types used by Countries the UNSCon Corpus""")
    countries = list(set(df["Country Speaker"].to_list()))
    selected_country = st.multiselect(r"$\textsf{\large Show the label distribution for: }$", countries)
    if not selected_country:
        st.write("Please select a Country to display the Conflict Type distribution.")
    else:
        for country in selected_country:
            df = df.loc[df['Conflict Type'].notna()]
            df_sliced = df[['Conflict Type', 'Country Speaker']]
            df_sliced = df_sliced.loc[df['Country Speaker'] == country]
            if df_sliced.shape[0] == 0:
                st.write("*No sentences containing a Conflicts in the UNSCon for:*", country)
            else:
                counting_dict = df_sliced.groupby('Conflict Type', observed=True).count().to_dict()['Country Speaker']
                counting_list = list(counting_dict.values())
                conflicttype_list = list(counting_dict.keys())

                # Create the pie chart
                fig = px.pie(
                    values=counting_list,
                    names=conflicttype_list,
                    title=country)
                fig.update_traces(
                    hovertemplate="<b>%{label}</b><br>Value: %{value} sentences<extra></extra>"
                )

                st.plotly_chart(fig)
    st.markdown("----")
    num_rows = df.shape
    st.write(f"Number of sentences: {num_rows[0]}  ")
