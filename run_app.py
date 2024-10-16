import pandas.api.types
import pandas as pd
import streamlit as st
from dataframe_filtering import filter_dataframe
from table_visualization import make_pretty

df = pd.read_csv("./dataset/conflict_annotations4UI.csv",
                 index_col=0)

colnames = {'sentence_text': "Text (Sentence-split)", 'Conflict_Type':'Conflict Type',
            'Conflict_Target':'Conflict Target','Target_Country':'Target Country',
            'speech_id': 'Speech-ID', 'country': 'Country Speaker', 'speaker': 'Speaker Name',
            'participanttype': 'Participant-Type', 'date': 'Date of Debate'}

df['date'] = pd.to_datetime(df['date']).dt.date
df['Conflict_Type'] = df.Conflict_Type.astype('category')
df['Conflict_Target'] = df.Conflict_Target.astype('category')
df['Target_Country'] = df.Target_Country.astype('category')
df['participanttype'] = df.participanttype.astype('category')
df['country'] = df.country.astype('category')



st.set_page_config(layout="wide")
st.title("Conflicts in UNSC Speeches")
st.write(
    """This app accomodates the blog [here](<https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/>)
    and walks you through one example of how the Streamlit
    Data Science Team builds add-on functions to Streamlit.
    """
)

df = filter_dataframe(df)
df = df.style.pipe(make_pretty)
st.dataframe(df, column_config={old: st.column_config.Column(new) for old, new in colnames.items()})