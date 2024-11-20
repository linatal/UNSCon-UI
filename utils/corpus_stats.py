# TODO: create barplot based on drodown menu
# TODO: barplot Conflict_Type, Conflict_Target + Conflict Target 2, Conflict_Target_Intermediate, Target_Country+Target_Country_2, country
# TODO: table with num of sentences
import streamlit as st
import pandas as pd

def get_stats(df):
    num_rows = df.shape
    st.write(f"Number of sentences: {num_rows[0]}  ")
    st.markdown("----")

def create_bars(df):
    barcharts_types = ['Conflict_Type', 'Conflict_Target', 'Conflict_Target_Intermediate', 'Target_Country', 'country', 'Subject']
    selected = st.selectbox(r"$\textsf{\Large Based on selected sentences above, create barchart: }$", barcharts_types)

    if selected == 'Conflict_Type':
        st.write("Distribution of *Conflict Types* in selected sentences:")
        df = df.apply(lambda col: col.cat.add_categories('No Conflict').fillna(
            'No Conflict') if col.dtype.name == 'category' else col)
    elif selected == 'Conflict_Target':
        st.write("Distribution of *Conflict Target Groups* in selected sentences (there are two targets per sentence possible):")
        df = merge_columns_targetgrp(df)
    elif selected == 'Conflict_Target_Intermediate':
        st.write("Distribution of *Intermediate Conflict Target Groups* in selected sentences:")
    elif selected == 'Target_Country':
        st.write("Distribution of *Conflict Target Countries* in selected sentences (there are two targets per sentence possible):")
        df = merge_columns_targetcountry(df)

    chart_data = df[selected].value_counts()
    st.bar_chart(chart_data,  x_label=selected, y_label='num. sentences')


def merge_columns_targetgrp(df):
    # merge columns Conflict Target
    df_ct1 = df.loc[df['Conflict_Target'].notna()]
    df_ct2 = df.loc[df['Conflict_Target_2'].notna()]
    df_ct1 = df_ct1.drop(['Conflict_Target_2'], axis=1)
    df_ct2 = df_ct2.drop(['Conflict_Target'], axis=1)
    df_ct2 = df_ct2.rename(columns={'Conflict_Target_2':'Conflict_Target'})

    df_merged = pd.concat([df_ct2, df_ct1], axis=0)
    return df_merged


def merge_columns_targetcountry(df):
    # merge columns Target Country
    df_tc1 = df.loc[df['Target_Country'].notna()]
    df_tc2 = df.loc[df['Target_Country_2'].notna()]
    df_tc1 = df_tc1.drop(['Target_Country_2'], axis=1)
    df_tc2 = df_tc2.drop(['Target_Country'], axis=1)
    df_tc2 = df_tc2.rename(columns={'Target_Country_2': 'Target_Country'})

    # TODO: check check!
    df_merged = pd.concat([df_tc1, df_tc2], axis=0)
    return df_merged