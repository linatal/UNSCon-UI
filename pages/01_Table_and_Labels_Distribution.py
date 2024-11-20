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
st.title("Interactive Table and Boxplot Visualization")
st.subheader("""Speeches, Labels and Metadata of the UNSCon Corpus""")

st.markdown("""<ul>
<li style="font-size: 18px; margin-bottom: 8px; color: #148f6e">Choose the options below to filter data</li>
<li style="font-size: 18px; margin-bottom: 8px; color: #148f6e">Both the table and the barchart below will adapt to the filters you choose</li>
<li style="font-size: 18px; margin-bottom: 50px; color: #148f6e">Choose which labels distribution to display on barchart</li>
 </ul>
""", unsafe_allow_html=True)

# ---DF input
df_input = pd.read_csv("./dataset/conflict_annotations4UI.csv", index_col=0)
df_input = define_dtypes(df_input)
print()
df = filter_dataframe(df_input)
df = display_values(df)
df_display = df.style.pipe(make_pretty)

# ---print TABLE
st.dataframe(df_display, column_config={old: st.column_config.Column(new) for old, new in colnames.items()})

# ---print STATS
get_stats(df)
create_bars(df)
print()

# ---Sidebar
st.sidebar.markdown('## Info:')
st.sidebar.markdown(""" <h3><span class="notbold"> Filter dataframe on:
<ul>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Type</code> </li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Target Group</code></li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Target Intermediate Group </code></li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Target Country</code> (Target Country of the Conflict)</li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Speaker Country</code> (Country the Speaker is representing)</li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Subject Debate</code> (Currently the corpus includes debates from two topics: Ukraine, and Women, Peace and Security)</li>
</ul>
        </span></h3>""", unsafe_allow_html=True)
st.sidebar.markdown('''<h3>
        <span class="notbold">
            Filter mechanism is adopted in a modified form from the blog <a href="https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/"> here</a>.
        </span>
    </h3>''', unsafe_allow_html=True)
