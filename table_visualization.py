import pandas as pd


def color_conflicts(v):
    if v == 'Direct Critique':
        return f"color: white; background-color: #336600; "
    elif v == 'Proxy Critique':
        return f"color: white; background-color: #666600;"
    elif v == "Accusation Lie":
        return f"color: white; background-color: #990000;"
    elif v == "Accusation Lie and Correction":
        return f"color: white; background-color: #FF3333;"


def color_targets(v):
    if v == 'Speaker or Speech':
        return f"color: black; background-color: #FFE5CC; "
    elif v == 'Country':
        return f"color: black; background-color: #FFFFCC;"
    elif v == "Group of Countries":
        return f"color: black; background-color: #FFFF99;"
    elif v == "UNSC":
        return f"color: black; background-color: #CCE5FF;"
    elif v == "Self-targeting":
        return f"color: black; background-color: #CCFFFF;"
    elif v == "Underspecified":
        return f"color: black; background-color: #E0E0E0;"


def color_targets_interm(v):
    if v == 'Law or Policy':
        return f"color: black; background-color: #FFE5CC; "
    elif v == 'Person (Non-representative of Country)':
        return f"color: black; background-color: #FFFFCC;"
    elif v == "UN-Organization (other than UNSC)":
        return f"color: black; background-color: #FFFF99;"
    elif v == "Non-Governmental Group":
        return f"color: black; background-color: #CCE5FF;"
    elif v == "Other":
        return f"color: black; background-color: #CCFFFF;"


# rename values changing the df
rename_conflicts = {'Direct_NegEval': "Direct Critique", 'Indirect_NegEval': "Proxy Critique",
                    "Challenge": "Accusation Lie", "Correction": "Accusation Lie and Correction"}
rename_targets = {'Speaker_Speech': "Speaker or Speech", "Countries_Group": "Group of Countries"}
rename_targets_interm = {'Law_Policy': "Law or Policy", 'Person': "Person (Non-representative of Country)",
                         "UN-Organization": "UN-Organization (other than UNSC)",
                         "Non-Governm_Grp": "Non-Governmental Group"}
rename_UK = {"United Kingdom Of Great Britain And Northern Ireland": "United Kingdom"}

# rename columns for diplaying (without changing the source data)
colnames = {'sentence_text': "Text (Sentence-split)", 'Conflict_Type': 'Conflict Type',
            'Conflict_Target': 'Conflict Target', 'Conflict_Target_2': 'Conflict Target 2',
            'Conflict_Target_Intermediate': 'Conflict Proxy Target',
            'Target_Country': 'Country Target', 'Target_Country_2': 'Country Target 2',
            'country': 'Country Speaker',
            'filename': 'Speech-ID filename', 'speaker': 'Speaker Name',
            'participanttype': 'Participant-Type', 'date': 'Date of Debate',
            'speech_sentence_id': 'Sentence-ID', 'paragraph_id': 'Paragraph-ID', 'speech': 'Speech-Num. in Debate'}



# Function to apply the styling (format is not rendered in streamlit, need to change values directly in display_values())
def make_pretty(styler):
    # styler.format(rename_conflicts, subset="Conflict_Type")
    styler.map(color_conflicts, subset="Conflict_Type")
    # styler.format(rename_targets, subset="Conflict_Target")
    styler.map(color_targets, subset="Conflict_Target")
    # styler.format(rename_targets, subset="Conflict_Target_2")
    styler.map(color_targets, subset="Conflict_Target_2")
    # styler.format(rename_targets, subset="Conflict_Target_Intermediate")
    styler.map(color_targets_interm, subset="Conflict_Target_Intermediate")
    return styler


def define_dtypes(df):
    # define dtype for each column
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['Conflict_Type'] = df.Conflict_Type.astype('category')
    df['Conflict_Target'] = df.Conflict_Target.astype('category')
    df['Conflict_Target_2'] = df.Conflict_Target_2.astype('category')
    df['Conflict_Target_Intermediate'] = df.Conflict_Target_Intermediate.astype('category')
    df['Target_Country'] = df.Target_Country.astype('category')
    df['Target_Country_2'] = df.Target_Country_2.astype('category')
    df['participanttype'] = df.participanttype.astype('category')
    df['country'] = df.country.astype('category')
    return df


def display_values(df):
    # rename values more user friendly
    df_display = df.copy()
    df_display['Conflict_Type'] = df_display['Conflict_Type'].cat.rename_categories(rename_conflicts)
    df_display['Conflict_Target'] = df_display['Conflict_Target'].cat.rename_categories(rename_targets)
    df_display['Conflict_Target_2'] = df_display['Conflict_Target_2'].cat.rename_categories(rename_targets)
    df_display['Conflict_Target_Intermediate'] = df_display['Conflict_Target_Intermediate'].cat.rename_categories(
        rename_targets_interm)
    df_display['country'] = df_display['country'].cat.rename_categories(
        rename_UK)
    return df_display
