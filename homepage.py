import streamlit as st
from css_styles.notbold import notbold

# TODO: Include Tortendiagramm
# TODO eine seite mit den guidelines in streamlit
# TODO: finish barcharts
# TODO: check check merging


# -- Set page config
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


st.write("# Welcome to UNSC Conflicts Corpus App! 👋")


st.write("""<p>
    This app visualizes the results of our annotated 86 speeches from the UN Security Council's Conflicts Corpus (in short: <i>UNSCon</i>).
</p>""", unsafe_allow_html=True)


st.markdown("""<p>You can choose between the following demos (left side):</p>
<ul>
<li style="font-size: 20px; margin-bottom: 8px; color: #148f6e">Dataset in Table format</li>
<li style="font-size: 20px; margin-bottom: 8px; color: #148f6e">Sankeyflow</li>
</ul>
""", unsafe_allow_html=True)

st.subheader("""Info:""")

st.write("""<p>In the UNSCon we present a new framework for annotating expressions of Conflicts, used on examples of 
debates on Ukraine crisis from 2014 and two debates on Women, Peace and Security Agenda. 
Conflicts are defined as a form of critique or distancing oneself from the positions or actions from another 
country present at the Council. A Conflict in our guidelines is therefore not necessarily a report of a military conflict - 
generally, this is a verbal Conflict expressing a negative evaluation. </p>
<p>A Conflict consists of a <b>Target</b>, which is the entity being evaluated, and a negative evaluation toward that Target. 
The holder of the evaluation is always the <b>Speaker</b>.</p>
<p>Conflicts can be expressed by directly criticizing the country (<b>Direct Conflict</b>) or indirectly by addressing 
the critique to a surrogate entity (<b>Indirect Conflict</b>). Next to Conflicts being defined as a negative 
evaluation of a Target, we look at <b>Challenging</b> Statements accusing the Target of not telling the truth, as well as the 
Correction of that allegedly false statement.</p>""", unsafe_allow_html=True)

st.sidebar.success("Select a demo above.")