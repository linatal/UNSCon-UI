import pandas as pd
import streamlit as st
from dataframe_filtering import filter_dataframe
from table_visualization import make_pretty, colnames, define_dtypes, display_values

df_input = pd.read_csv("./dataset/conflict_annotations4UI.csv",
                 index_col=0)
#df = df[df['sentence_text'].notna()]

st.set_page_config(layout="wide")
st.title("Conflicts in UNSC Speeches")
st.subheader("""Visualizing the UNSCon Corpus""")

st.write("""In the UNSC Conflicts Corpus (UNSCon) we present a new framework for annotating expressions of Conflicts 
used in a diplomacy setting, focusing on recordings of English UN Security Council (UNSC) speeches. 

We provide an analysis framwork of Conflict defined as a form of critique or distancing oneself from the positions or actions from another 
country present at the Council. Generally, this is done via expressing a negative evaluation. A Conflict in our 
guidelines is therefore not necessarily a report of a military conflict. A Conflict consists of a Target, which is the 
entity being evaluated, and a negative evaluation toward that Target. The holder of the evaluation is always the speaker.

Conflicts can be expressed by directly criticizing the country (Direct Negative Evaluation) or indirectly by addressing 
the critique to a surrogate entity (Indirect Negative Evaluation). Next to Conflicts being defined as a negative 
evaluation of a Target, we look at Challenging Statements accusing the Target of not telling the truth, as well as the 
Correction of that allegedly false statement.
""")

df_input = define_dtypes(df_input)
df = filter_dataframe(df_input)
df = display_values(df)
df_display = df.style.pipe(make_pretty)
st.dataframe(df_display, column_config={old: st.column_config.Column(new) for old, new in colnames.items()})



st.write(
    """Filter mechanism is adopted in a modified form from the blog [here](<https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/>)
    """
)