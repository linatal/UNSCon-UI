import streamlit as st
from utils.helper import local_css

def render_guidelines():
    local_css("./style.css")
    st.write("# Labels for the UN Security Council Conflicts Corpus (UNSCon) ")
    st.write('In the UNSCon demo, it is possible to filter the corpus based on various features. The document aims to explains each filter in more detail.')

    st.write("### 1. Text (Sentence-split)")
    st.write("The UNSCon as displayed here was automatically sentence-split using SpaCy library. "
             "To search for sentences containing a substring, write the substring into the field. The search is case-sensitive.")

    st.write("### 2. Conflict Type")
    st.write("Conflict are a form of critique or distancing oneself from the positions or actions from another country present at the Council. "
             "Generally, this is done via expressing a negative evaluation. "
             "A Conflict consists of a Target, which is the entity being evaluated, and a negative evaluation toward that Target. "
             "The holder of the evaluation is always the speaker. ")
    st.write("""
    | Conflict Type            | Explanation |
    |--------------------------|-------------|
    | Direct Conflict          | Conflicts that are directly criticizing the target country. |
    | Indirect Conflict        | Conflicts that are indirectly criticizing the target country by addressing the critique to a surrogate entity.|
    | Challenge                | Conflicts accusing the Target of not telling the truth. |
    | Challenge and Correction | Conflicts accusing the Target of not telling the truth and correcting that allegedly untrue statement.|
    | nan          | No Conflict. |
    """)

    st.write("### 3. Conflict Target Group / Conflict Intermediate") # TODO change name for Conflict Intermediate
    st.write("For Direct Conflicts and Indirect Conflicts, there are different Groups of Targets the Annotators had to define.")
    st.write("#### 3.1 Conflict Target Group / Conflict Target Group 2")
    st.write("One sentence can have one and optionally a sencond *Conflict Target Group* label. These labels describe a more general group of Conflict Tagets (Countries are annotated in *3.3 Target Country*).")
    st.write("""
    | Conflict Target Group            | Explanation |
    |--------------------------|-------------|
    | Speaker or Speech        | Conflict that targets a previous or upcoming speaker or a speech. |
    | Country                  | Conflict targeting a Country.|
    | Countries_Group          | Conflict targeting a group of Countries. |
    | UNSC                     | Targeting the UNSC, often called “the Council”. Speakers also often refer to the Council via self-referring formulations using 3rd person plural (“We” meant as “the Council).|
    | Self-targeting           | Often diplomats refer to themselves or the country they are representing using self-references using 3rd person plural (“We”) or 1st Person singular pronouns (“I”).|
    | Underspecified           | There are cases where there is evaluative language and there is a target that could potentially fit into one of the labels, but there is no mention  one sentence before or after the Conflict span. |
    | nan          | No Conflict Target Group. |
    """)
    st.write("#### 3.2 Conflict Intermediate")
    st.write("""
    | Conflict Target Intermediate            | Explanation |
    |--------------------------|-------------|
    | Law or Policy | Conflict that targets a law or policy is something that should be implemented or is currently in force in the UNSC or other UN Organizations (like setting up a new Expert Group, new structural reforms, resolutions, or amendments to resolutions). |
    | Person | Targeting a Person which is not clearly connected as representative of a Country or group of Countries.|
    | UN-Organizations | Targeting UN-Organizations other than the Council (the Council, the World Bank, World Health Organization, International Monetary Fund, etc.). |
    | Non-Governmental Groups | Targeting groups (allegedly) working on behalf of the Target country, such as societal organizations, activists, guerrilla groups, and others.|
    | Other | This label serves for all intermediate Targets, which do not fit into one of the predefined classes.|
    | nan          | No Conflict Intermediate. |
    """)
    st.write("#### 3.3 Target Country / Target Country 2")
    st.write("Lists all Countries having a speech during the debate. Per sentence, there can be optionally two countries labeled.")
    st.write("#### 3.4 Speaker Name")
    st.write("All Speakers holding a speech during the debate. For searching write the substring into the field. The search is case-sensitive.")

    st.write("#### 3.5 Participant-Type")
    st.write(""" Taken from the original UNSC Debates Corpus (Schönfeld et al. 2019 ([url](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KGVSYH))).  
    Labels: Mentioned, The President, Guest. """)

    st.write("#### 3.6 Sentence-ID / Paragraph-ID / Speech-ID filename")
    st.write("Sentence-ID and paragraph-ID and filename of the sentence in the UNSC Conflicts corpus.")

    st.write("#### 3.7 Subject")
    st.write("Our UNSCon Corpus contains speeches taken from six debates between 2014 and 2016 dealing with two main subjects.")
    st.write("""
     | Subject            | Explanation |
     |--------------------------|-------------|
     | Ukraine | Debates concerning the Ukraine conflict in 2014 after the annexation of Crimea and before the Minsk II agreement. |
     | Women, Peace, and Security (WPS) | Debates dealing with the impacts that conflict had on women and girls and the question, how to systematically include women in peacebuilding efforts.|
     """)

    st.write("---------------")
    st.write("*Info:*")
    st.write("*Author: Karolina Zaczynska, Applied CL Discourse Lab, University of Potsdam*")
    st.write("*This document is a simplified version of the annotation guidelines, for a more detailed version, please see our [github](https://github.com/linatal/UNSCon).*")

