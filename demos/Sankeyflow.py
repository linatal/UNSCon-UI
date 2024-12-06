import streamlit as st
import plotly.graph_objects as go
from utils.prepare_data_sankeygraph import prepare_table_sankey, prepare_columns
from utils.helper import local_css



def render_sankey(filtered_df):
    # Apply CSS
    local_css("./style.css")
    st.title('Interactive Sankeyflow Visualizer')
    st.subheader('Who is criticized by whom and how often in the UNSCon?')
    st.markdown("""<ul>
    <li style="font-size: 20px; margin-bottom: 8px; color: #148f6e">Use the menu below to select data and set plot parameters</li>
    <li style="font-size: 20px; margin-bottom: 8px; color: #148f6e">Your plots will appear below</li>
     </ul>
    """, unsafe_allow_html=True)

    st.markdown('''A Sankey Diagram  is a flow diagram, in which the width of arrows is proportional to the flow quantity.
                The Sankey Diagram here shows the number of sentences in which one country (left) criticizes another country.''')

    df_input_columns = prepare_columns(filtered_df)
    df_links, df_nodes = prepare_table_sankey(df_input_columns)
    # Create the figure (example Sankey layout)
    fig = go.Figure(data=[go.Sankey(
        node=dict(label=df_nodes["label"].dropna(axis=0, how="any"),
                  color=df_nodes["color"].dropna(axis=0, how="any")),
        link=dict(
            source=df_links["source"].dropna(axis=0, how="any"),
            target=df_links["target"].dropna(axis=0, how="any"),
            value=df_links["value"].dropna(axis=0, how="any"),
            color=df_links["link color"].dropna(axis=0, how="any"),
        ),
        valueformat=".0f",
        valuesuffix=" sentences")
    ],
        layout=dict(
            # title = "This is the title diagram",
            height=1000)
    )
    # Update the layout with a template
    fig.update_layout(
        template="plotly_white",
        font=dict(
            family="Sans-Serif",
            size=20,
            color="black"
        ), )

    # ---DISPLAY SANKEY IN STREAMLIT-----#
    _left, mid, _right = st.columns([3, 15, 3])
    with mid:
        st.plotly_chart(fig, width=1600)
    with _left:
        st.markdown('''<br><br><br><H4 text-align="center">Speaker Country</H4>''', unsafe_allow_html=True)
    with _right:
        st.markdown('''<br><br><br><H4 text-align="center">Target Country of Conflict</H4>''', unsafe_allow_html=True)
    # ---print Num. of Sentences
    num_rows = filtered_df.shape
    st.write(f"Number of sentences: {num_rows[0]}  ")











