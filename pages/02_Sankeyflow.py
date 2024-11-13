import pandas as pd
import streamlit as st
import base64
import plotly.graph_objects as go
from utils.prepare_data_sankeygraph import prepare_table_sankey, prepare_columns, define_dtypes_sankey, display_values_sankey
from utils.dataframe_filtering import filter_dataframe


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

# Apply CSS
local_css("style.css")

# --------------------------------------------#
# ----TITLE----#
# Title the app
st.title('Interactive UNSCon Sankey visualizer')
st.subheader('*Who is criticized by whom and how often in the UNSCon?*')
st.markdown("""<ul>
<li style="font-size: 20px; margin-bottom: 8px; color: #148f6e">Use the menu below to select data and set plot parameters</li>
<li style="font-size: 20px; margin-bottom: 8px; color: #148f6e">Your plots will appear below</li>
 </ul>
""", unsafe_allow_html=True)
#st.markdown('<h1 style="text-align:center;">Sankey diagram generator for UNSCon</h1>', unsafe_allow_html=True)
#st.write(notbold, unsafe_allow_html=True)


# ------SIDEBAR-------#
st.sidebar.markdown('## Info:')
st.sidebar.markdown('''<h3>
        <span class="notbold">
            A <b>Sankey Diagram</b>  is a flow diagram, in which the width of arrows is proportional to the flow quantity.
            The <b>Sankey Diagram</b> here shows the number of sentences in which one country (left) criticizes another country (first Sankey).
        </span>
    </h3>''', unsafe_allow_html=True)

st.sidebar.markdown(""" <h3><span class="notbold">  Filter dataframe on:
<ul>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Type</code> </li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Conflict Target Group</code></li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Target Country</code> (Target Country of the Conflict)</li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Speaker Country</code> (Country the Speaker is representing)</li>
<li style="font-size: 18px; margin-bottom: 8px"><code>Subject Debate</code> (Currently the corpus includes debates from two topics: Ukraine, and Women, Peace and Security)</li>
</ul>
        </span></h3>""", unsafe_allow_html=True)

# -------------#
# import data for sankeygraph
df_input = pd.read_csv("./dataset/conflict_annotations4UI.csv", index_col=0)
df_input = df_input[df_input['sentence_text'].notna()]
df_input = df_input[['Conflict_Type', 'Conflict_Target', 'Conflict_Target_2', 'Target_Country', 'Target_Country_2', 'country', 'Subject']]


df_input_dtypes = define_dtypes_sankey(df_input)
df_input_columns = prepare_columns(df_input_dtypes)
print()
df_input_values = display_values_sankey(df_input_columns)
df = filter_dataframe(df_input_values)
df_links, df_nodes = prepare_table_sankey(df)






# Create the figure (example Sankey layout)
fig = go.Figure(data=[go.Sankey(
    node=dict( label=df_nodes["label"].dropna(axis=0, how="any"),
               color=df_nodes["color"].dropna(axis=0, how="any")),
    link=dict(
        source=df_links["source"].dropna(axis=0, how="any"),
        target=df_links["target"].dropna(axis=0, how="any"),
        value=df_links["value"].dropna(axis=0, how="any"),
        color=df_links["link color"].dropna(axis=0, how="any"),
),

valueformat = ".0f",
valuesuffix = " sentences")
],
layout = dict(
#title = "This is the title diagram",
height = 1000)
)


# Update the layout with a template
fig.update_layout(
    template="plotly_white",
    font=dict(
        family="Sans-Serif",
        size=20,
        color="black"
    ),


)


#---DISPLAY SANKEY IN STREAMLIT-----#
#---DISPLAY SANKEY IN STREAMLIT-----#
_left, mid, _right = st.columns([3, 15, 3])
with mid:
    st.plotly_chart(fig, width=1600)
with _left:
    st.markdown('''<br><br><br><H4 text-align="center">Speaker Country</H4>''', unsafe_allow_html=True)
with _right:
    st.markdown('''<br><br><br><H4 text-align="center">Target Country of Conflict</H4>''', unsafe_allow_html=True)

#fig.show()
  #------------------------------------#
#except:
#  st.markdown("""<h3 style="color:red;">set the height and width of your diagram. Thank you.</h3>""", unsafe_allow_html=True)


