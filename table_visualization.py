import streamlit as st
import pandas as pd

#df = pd.read_csv("./dataset/conflict_annotations4UI.csv",index_col=0)

def color_conflicts(v):
    if v == 'Direct_NegEval':
        return f"color: white; background-color: #336600; "
    elif v == 'Indirect_NegEval':
        return f"color: white; background-color: #666600;"
    elif v == "Challenge":
        return f"color: white; background-color: #990000;"
    elif v == "Correction":
        return f"color: white; background-color: #FF3333;"


def color_targets(v):
    if v == 'Speaker_Speech':
        return f"color: black; background-color: #FFE5CC; "
    elif v == 'Country':
        return f"color: black; background-color: #FFFFCC;"
    elif v == "Countries_Group":
        return f"color: black; background-color: #FFFF99;"
    elif v == "UNSC":
        return f"color: black; background-color: #CCE5FF;"
    elif v == "Self-targeting":
        return f"color: black; background-color: #CCFFFF;"
    elif v == "Underspecified":
        return f"color: black; background-color: #E0E0E0;"


def rename_conflicts(v):
    if v == 'Direct_NegEval':
        return f"Direct Critique"
    elif v == 'Indirect_NegEval':
        return f"Proxy Critique"
    elif v == "Challenge":
        return f"Accusation Lie"
    elif v == "Correction":
        return f"Correcting Lie"


def rename_targets(v):
    if v == 'Speaker_Speech':
        return f"Speaker or Speech"
    elif v == 'Country':
        return f"Country"
    elif v == "Countries_Group":
        return f"Group of Countries"
    elif v == "UNSC":
        return f"UNSC"
    elif v == "Self-targeting":
        return f"Self-targeting"
    elif v == "Underspecified":
        return f"Underspecified"


def make_pretty(styler):
    styler.format(rename_conflicts, subset="Conflict_Type")
    styler.map(color_conflicts, subset="Conflict_Type")
    styler.format(rename_targets, subset="Conflict_Target")
    styler.map(color_targets, subset="Conflict_Target")
    return styler








# TODO: filter Dataframe
# TODO: Circular Sankey
# TODO: fix and include preprocessing skript that converts edu-based main_conflicts.csv
#  to conflict_annotations_sentences.csv
