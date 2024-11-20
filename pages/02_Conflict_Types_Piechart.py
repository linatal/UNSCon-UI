import pandas as pd
import streamlit as st
from utils.dataframe_filtering import filter_dataframe
from utils.table_visualization import make_pretty, colnames, define_dtypes, display_values
from utils.corpus_stats import get_stats, create_bars


apptitle = 'Conflicts in the UNSC'
st.set_page_config(
    page_title=apptitle,
    layout="wide",
    page_icon=":collision:",
)
#st.write(notbold, unsafe_allow_html=True)
# ---Load CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS
local_css("style.css")

# ---Text Body
st.title("Interactive Pie Chart")
st.subheader("""Showing Conflict Types used by Countries the UNSCon Corpus""")

# ---DF input
df_input = pd.read_csv("./dataset/conflict_annotations4UI.csv", index_col=0)

# only rows with conflict
df_input = df_input.loc[df_input['Conflict_Type'].notna()]
df = df_input[['Conflict_Type', 'country','Target_Country']]
df = df.fillna('Underdefined')

# choose on country
sorted_speaker = sorted(set(df['country'].to_list()))
sorted_target = sorted(set(df['Target_Country'].to_list()))


st.pyplot(df["Conflict_Type"].value_counts().plot.pie())
