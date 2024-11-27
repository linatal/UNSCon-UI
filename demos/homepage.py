import streamlit as st
from utils.helper import local_css
from utils.shared_sidebar import get_data, filter_dataframe, sidebar_navigation


# -- Set page config
apptitle = 'Conflicts in the UNSC'
st.set_page_config(
    page_title=apptitle,
    layout="wide",
    page_icon=":collision:")



# Render the main page
def render_homepage():
    # Apply CSS
    local_css("./style.css")
    st.write("# Welcome to UNSC Conflicts Corpus Multi-page App! 👋")

    st.write("""<p>
        This app visualizes the results of our annotated 86 speeches from the UN Security Council's Conflicts Corpus (in short: <i>UNSCon</i>).
    </p>""", unsafe_allow_html=True)

    st.markdown("""<p>You can choose between the following demos (left side):</p>
    <ul>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <i>Table and Labels Distribution</i>: Dataset in table format and boxplots showing distribution of labels</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <i>Sankeyflow</i>: Visualizing who is critisizing whom</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <i>Conflict Types Piechart</i>: Focussing on who is using which Conflict Type in the Corpus</li>
    </ul>
    """, unsafe_allow_html=True)

    st.subheader("""Info:""")

    st.write("""<p>In the UNSCon, we present a new framework for annotating expressions of Conflicts, used on examples of 
    debates on Ukraine crisis from 2014 and two debates on Women, Peace and Security Agenda. 
    We define Conflicts as a form of critique or distancing oneself from the positions or actions from another 
    country present at the Council. A Conflict in our guidelines is therefore not necessarily a report of a military conflict - 
    generally, this is a verbal Conflict expressing a negative evaluation. </p>
    <p>A Conflict consists of a <b>Target</b>, which is the entity being evaluated, and a negative evaluation toward that Target. 
    The holder of the evaluation is always the <b>Speaker</b>.</p>
    <p>Conflicts can be expressed by directly criticizing the country (<b>Direct Conflict</b>) or indirectly by addressing 
    the critique to a surrogate entity (<b>Indirect Conflict</b>). Next to Conflicts being defined as a negative 
    evaluation of a Target, we look at <b>Challenging</b> Statements accusing the Target of not telling the truth, as well as the 
    Correction of that allegedly false statement.</p>""", unsafe_allow_html=True)

    st.write(
        '<a title="Joowwww, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:UN_emblem_blue.svg"><img width="12" alt="UN emblem blue" class="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/512px-UN_emblem_blue.svg.png?20230920050537"></a>',
        unsafe_allow_html=True)















