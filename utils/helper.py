import pandas as pd
import streamlit as st

def set_page_config():
    # -- Set page config
    apptitle = 'Conflicts in the UNSC'
    st.set_page_config(
        page_title=apptitle,
        layout="wide",
        page_icon=":collision:",
    )

# ---Load CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def define_dtypes(df):
    df = df.copy()
    # define dtype for each column
    for column in df.columns:
        if column == "Sentence-ID" or column == "Paragraph-ID" or column == "Speech-Num. in Debate":
            df[column] = df[column].astype('int64') # Convert columns to integer
        elif column == "date":
            df[column] = pd.to_datetime(df['Date of Debate'], format="%d %B %Y").dt.date # Convert 'date' to datetime
        elif column == "Text (Sentence-split)" or column == "Speaker Name":
            df[column] = df[column].astype('object')
        else:
            df[column] = df[column].astype('category')
    return df


def merge_columns_targetgrp(df):
    # merge columns Conflict Target
    df_ct1 = df.loc[df['Conflict Target Group'].notna()]
    df_ct2 = df.loc[df['Conflict Target Group 2'].notna()]
    df_ct1 = df_ct1.drop(['Conflict Target Group 2'], axis=1)
    df_ct2 = df_ct2.drop(['Conflict Target Group'], axis=1)
    df_ct2 = df_ct2.rename(columns={'Conflict Target Group 2': 'Conflict Target Group'})
    df_merged = pd.concat([df_ct2, df_ct1], axis=0)
    df_merged = df_merged['Conflict Target Group'].astype('category')
    return df_merged


def merge_columns_targetcountry(df):
    # merge columns Target Country
    df_tc1 = df.loc[df['Target Country'].notna()]
    df_tc2 = df.loc[df['Target Country 2'].notna()]
    df_tc1 = df_tc1.drop(['Target Country 2'], axis=1)
    df_tc2 = df_tc2.drop(['Target Country'], axis=1)
    df_tc2 = df_tc2.rename(columns={'Target Country 2': 'Target Country'})
    df_merged = pd.concat([df_tc1, df_tc2], axis=0)
    df_merged['Target Country'] = df_merged['Target Country'].astype('category')
    return df_merged
