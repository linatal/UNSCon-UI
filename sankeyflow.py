import pandas as pd
import streamlit as st
import base64
import plotly.graph_objects as go
from prepare_data_sankeygraph import prepare_table_sankey
from dataframe_filtering import filter_dataframe


# TODO: Why filtering WPS only includes two sentences?
# TODO: make preprocesing smarter to have only one conflict target/country for filtering, also rename columns before.
# create a seperate function in prepare_data_sankeygraph.py, and only afterwards create df_links and df_source

# --------------------------------------------#
# ----TITLE----#
st.markdown('<h1 style="text-align:center;">Sankey diagram generator for UNSCon</h1>', unsafe_allow_html=True)
# -------------#
# import data for sankeygraph
df_input = pd.read_csv("./dataset/conflict_annotations4UI.csv", index_col=0)
df_input = df_input[df_input['sentence_text'].notna()]
df_input = df_input[['Conflict_Type', 'Conflict_Target', 'Conflict_Target_2', 'Target_Country', 'Target_Country_2', 'country', 'Subject']]

df = filter_dataframe(df_input)
df_links, df_nodes = prepare_table_sankey(df)


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
height = 800)
)


# Update the layout with a template
fig.update_layout(
    title_text="Sankey Diagram Conflict Annotations",
    template="plotly_white",
    font=dict(
        family="Helvetica",
        size=20,
        color="black"
    ),
    title=dict(
        font=dict(
            family="Helvetica",
            size=20,
            color="black"
        )
    )
)


#---DISPLAY SANKEY IN STREAMLIT-----#
st.plotly_chart(fig)

#fig.show()
  #------------------------------------#
#except:
#  st.markdown("""<h3 style="color:red;">set the height and width of your diagram. Thank you.</h3>""", unsafe_allow_html=True)


