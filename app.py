import streamlit as st
from utils.shared_sidebar import get_data, filter_dataframe, sidebar_navigation
from demos.homepage import render_homepage
from demos.guidelines import render_guidelines
from demos.Piechart import render_piechart
from demos.Table import render_table
from demos.Barchart import render_bars
from demos.Sankeyflow import render_sankey

# TODO: Include Tortendiagramm

# -- Set page config
apptitle = 'Conflicts in the UNSC'
st.set_page_config(
    page_title=apptitle,
    layout="wide",
    page_icon=":collision:")

# Load the data
df = get_data()
# Sidebar navigation and filtering
selected_page = sidebar_navigation()
filtered_df = filter_dataframe(df)
#selected_page = "Barchart"

# Render the main page
if selected_page == "Homepage":
    render_homepage(filtered_df)
elif selected_page == "Table":
    render_table(filtered_df, df)
if selected_page == "Barchart":
    render_bars(filtered_df)
elif selected_page == "Sankeyflow":
    filtered_df = filtered_df[filtered_df["Text (Sentence-split)"].notna()]
    filtered_df = filtered_df[['Conflict Type', 'Conflict Target Group', 'Conflict Target Group 2', 'Target Country', 'Target Country 2',
             'Country Speaker']]  # , 'Subject'
    render_sankey(filtered_df)
elif selected_page == "Piechart":
    render_piechart(filtered_df)
elif selected_page == "Guidelines Filters":
    render_guidelines()

