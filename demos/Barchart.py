import streamlit as st
from utils.helper import merge_columns_targetgrp, merge_columns_targetcountry


def render_bars(df):
    st.title("Interactive Barchart Visualization")
    barcharts_types = ['Conflict Type', 'Conflict Target Group', 'Conflict Target Intermediate', 'Target Country', 'Country Speaker', 'Subject']
    selected = st.selectbox(r"$\textsf{\large Show the label distribution for: }$", barcharts_types)

    if selected == 'Conflict Type':
        st.write("Distribution of *Conflict Types* in selected sentences:")
        df = df.apply(lambda col: col.cat.add_categories('No Conflict').fillna(
            'No Conflict') if col.dtype.name == 'category' else col)
    elif selected == 'Conflict Target Group':
        st.write("Distribution of *Conflict Target Groups* in selected sentences (there are two targets per sentence possible):")
        df = merge_columns_targetgrp(df)
    elif selected == 'Conflict Target Intermediate':
        st.write("Distribution of *Intermediate Conflict Target Groups* in selected sentences:")
    elif selected == 'Target Country':
        st.write("Distribution of *Conflict Target Countries* in selected sentences (there are two targets per sentence possible):")
        df = merge_columns_targetcountry(df)

    chart_data = df[selected].value_counts()
    st.bar_chart(chart_data,  x_label=selected, y_label='num. sentences')

    num_rows = df.shape
    st.write(f"Number of sentences: {num_rows[0]} ")