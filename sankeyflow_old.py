import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import base64
import plotly.graph_objects as go
from prepare_data_sankeygraph import prepare_table_sankey



# import data for sankeygraph
df = pd.read_csv("./dataset/conflict_annotations4UI.csv", index_col=0)
unique_source_target, links_dict, df_links, df_nodes = prepare_table_sankey(df)


# TODO: Conflict Types
# TODO: Topics



# -------------------------------------------#
# set local image as background in streamlit
# decorator from Streamlit, used to optimize the performance of a Streamlit app by caching the output of a function
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
.stApp {
  background-image: url("data:image/png;base64,%s");
  background-size: cover;
}
</style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


set_png_as_page_bg('img/background1.png')

# --------------------------------------------#
# ----TITLE----#
st.markdown('<h1 style="text-align:center;">Sankey diagram generator for UNSCon</h1>', unsafe_allow_html=True)
# -------------#


#----PLOT SANKEY------#
#try:
data_trace = dict(
type='sankey',
domain = dict(
  x =  [0,1],
  y =  [0,1]
),
orientation = "h",
valueformat = ".0f",
valuesuffix = " sentences",
node = dict(
  pad = 15,
  thickness = 10,
  line = dict(
    #color = "blue",
    width = 0
  ),
  label =  df_nodes["label"].dropna(axis=0, how="any")
  #color = df_nodes['color']
),
link = dict(
  source = df_links["source"].dropna(axis=0, how="any"),
  target = df_links["target"].dropna(axis=0, how="any"),
  value = df_links["value"].dropna(axis=0, how="any"),
  color = df_links["link color"].dropna(axis=0, how="any"),
)
)

layout = dict(
#title = "This is the title diagram",
height = 800,
width = 700,
hovermode = "x",
plot_bgcolor= 'rgba(0,0,0,0)',
paper_bgcolor='rgba(0,0,0,0)',
#font = dict(
#  family="Helvetica", size = int(13), color= "pink", shadow="none")
    )


fig = go.Figure(data=[data_trace], layout=layout)

fig.update_layout(
    title=dict(
        text="Sankey Diagram Conflict Annotations",
        font=dict(
            family="Helvetica",
            size=20,
            color="black"
        )
    ),
    font=dict(
        family="Helvetica",
        size=15,
        color="black"
    )
)


#---DISPLAY SANKEY IN STREAMLIT-----#
st.plotly_chart(fig)

#fig.show()
  #------------------------------------#
#except:
#  st.markdown("""<h3 style="color:red;">set the height and width of your diagram. Thank you.</h3>""", unsafe_allow_html=True)


