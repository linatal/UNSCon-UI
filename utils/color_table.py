import pandas as pd

def color_conflicts(v):
    if v == 'Direct Conflict':
        return f"color: white; background-color: #336600; "
    elif v == 'Indirect Conflict':
        return f"color: white; background-color: #666600;"
    elif v == "Challenge":
        return f"color: white; background-color: #990000;"
    elif v == "Challenge and Correction":
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


def color_cells(styler):
    styler.map(color_conflicts, subset="Conflict Type")
    styler.map(color_targets, subset="Conflict Target Group")
    styler.map(color_targets, subset="Conflict Target Group 2")
    styler.map(color_targets_interm, subset="Conflict Target Intermediate")
    return styler


def change_nans_sankey(df):
    df = df.apply(lambda col: col.cat.add_categories('Underspecified').fillna('Underspecified') if col.dtype.name == 'category' else col)
    return df

