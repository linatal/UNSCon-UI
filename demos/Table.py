import streamlit as st
from utils.color_table import color_cells
from utils.helper import local_css


def render_table(filtered_df, df):
    # Apply CSS
    local_css("./style.css")

    # ---Text Body
    st.title("Interactive Table Visualization")
    st.write("The table shows the speeches and metadata of the UNSCon. Please select a some filters on the sidebar to adjust the table.""")
    """
    st.markdown(""""""<ul>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e">Choose the options below to filter data</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e">Both the table and the barchart below will adapt to the filters you choose</li>
    <li style="font-size: 18px; margin-bottom: 50px; color: #148f6e">Choose which labels distribution to display on barchart</li>
     </ul>
    """""", unsafe_allow_html=True)"""

    df_display = filtered_df.style.pipe(color_cells)
    # ---print TABLE
    st.dataframe(df_display)
    # ---print Num. of Sentences
    num_rows = df.shape
    st.write(f"Number of sentences: {num_rows[0]}  ")


