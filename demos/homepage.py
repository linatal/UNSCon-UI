import streamlit as st
from utils.helper import local_css
from utils.shared_sidebar import get_data, filter_dataframe, sidebar_navigation



# Render the main page
def render_homepage(filtered_df):
    # Apply CSS
    local_css("./style.css")
    st.write("# Welcome to the UNSCon Multi-Page Demo 🇺🇳")
    #st.write('<a title="Joowwww, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:UN_emblem_blue.svg"><img width="10%" height=auto alt="UN emblem blue" class="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/512px-UN_emblem_blue.svg.png?20230920050537"></a>',unsafe_allow_html=True)
    st.write("""<p>
        This app visualizes the results of our annotated 86 speeches from the <b>UN Security Council's Conflicts Corpus (<i>UNSCon</i>)</b>.
        For more information on the corpus, please see our <a href="https://aclanthology.org/2024.lrec-main.716/">paper</a> and <a href="https://github.com/linatal/UNSCon">github page</a>.</p>
    """, unsafe_allow_html=True)

    st.markdown("""<p>You can choose between the following pages on the sidebar:</p>
    <ul>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <b>Table</b>: demo showing Dataset in table format</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <b>Barplot Labels Distribution</b>: boxplots showing distribution of labels</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <b>Sankeyflow</b>: demo visualizing who is critisizing whom</li>
    <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <b>Conflict Types Piechart</b>: demo focussing on who is using which Conflict Type in the Corpus</li>
        <li style="font-size: 18px; margin-bottom: 8px; color: #148f6e"> <b>Guidelines</b>: explains the Labels in the Dataset that appear in the Filter</li>
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
    st.write("#### Overview of the UNSCon:")
    st.write("Our UNSCon Corpus contains 87 speeches taken from six debates between 2014 and 2016 dealing with two main subjects, the *Ukraine conflict* (Ukraine) and *Women, Peace, and Security* (WPS).")
    st.write("""| Debate-ID       | #speeches in original Debate | #speeches in UNSCon | #sentences UNSCon | #tokens UNSCon |
|--------------|--------------|---------------|----------------|--------------|
| *Ukraine*    |              |               |                |              |
| S/PV.7138    | 21           | 17            | 345            | 8.797        |
| S/PV.7154    | 28           | 17            | 454            | 11.264       |
| S/PV.7165    | 22           | 13            | 501            | 12.270       |
| S/PV.7219    | 36           | 15            | 511            | 12.022       |
| *Sum Ukr.*   | *107*        | *62*          | *1.811*        | *44.353*     |
| *WPS*        |              |               |                |              |
| S/PV.7643    | 18           | 16            | 231            | 6.993        |
| S/PV.7658    | 75           | 9             | 395            | 10.985       |
| *Sum WPS*    | *93*         | *25*          | *626*          | *17.978*     |
| **Sum**      | **200**      | **87**        | **2.437**      | **62.331**   |
""")

















