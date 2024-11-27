import streamlit as st
from utils.shared_sidebar import get_data, filter_dataframe, sidebar_navigation
from demos.homepage import render_homepage
from demos.Table_and_Labels_Distribution import render_table
from demos.Sankeyflow import render_sankey


# TODO: Include Tortendiagramm
# TODO eine seite mit den guidelines in streamlit
# TODO: Table filter make columns/values pretty



# Load the data
df = get_data()
# Sidebar navigation and filtering
selected_page = sidebar_navigation()
filtered_df = filter_dataframe(df)
#selected_page = "Sankeyflow"

# Render the main page
if selected_page == "Homepage":
    render_homepage()
elif selected_page == "Tables and Labels Distribution":
    render_table(filtered_df, df)
elif selected_page == "Sankeyflow":
    df = df[df["Text (Sentence-split)"].notna()]
    df = df[['Conflict Type', 'Conflict Target Group', 'Conflict Target Group 2', 'Target Country', 'Target Country 2',
             'Country Speaker']]  # , 'Subject'
    render_sankey(filtered_df, df)

elif selected_page == "Piechart":
    print()

