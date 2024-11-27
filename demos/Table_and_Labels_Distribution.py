import streamlit as st
from utils.color_table import color_cells
from utils.create_bars import create_bars
from utils.helper import local_css



def render_table(filtered_df, df):
    # Apply CSS
    local_css("./style.css")

    # ---Text Body
    st.title("Interactive Table and Boxplot Visualization")
    st.subheader("""Speeches, Labels and Metadata of the UNSCon Corpus""")

    st.markdown("""<ul>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e">Choose the options below to filter data</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e">Both the table and the barchart below will adapt to the filters you choose</li>
    <li style="font-size: 18px; margin-bottom: 50px; color: #148f6e">Choose which labels distribution to display on barchart</li>
     </ul>
    """, unsafe_allow_html=True)

    df_display = filtered_df.style.pipe(color_cells)
    # ---print TABLE
    st.dataframe(df_display)
    # ---print Num. of Sentences
    num_rows = df.shape
    st.write(f"Number of sentences: {num_rows[0]}  ")
    st.markdown("----")
    create_bars(df)

# ---Sidebar
"""
st.sidebar.markdown('## Info:')
st.sidebar.markdown("""""" <h3><span class="notbold"> Filter dataframe on:
<ul>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Type</code> </li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Target Group</code></li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Target Intermediate Group </code></li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Target Country</code> (Target Country of the Conflict)</li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Speaker Country</code> (Country the Speaker is representing)</li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Subject Debate</code> (Currently the corpus includes debates from two topics: Ukraine, and Women, Peace and Security)</li>
</ul>
        </span></h3>"""""", unsafe_allow_html=True)

"""
