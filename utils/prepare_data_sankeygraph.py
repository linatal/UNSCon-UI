#---------- imports dataset df and prepares it for sankey display
import pandas as pd


def define_dtypes_sankey(df):
    # define dtype for each column
    for col in df.columns:
        df[col] = df[col].astype('category')
    return df
"""
# ---- rename values in Sankey
# to general df preprocessing
rename_conflicts = {'Direct_NegEval': "Direct Conflict", 'Indirect_NegEval': "Indirect Conflict",
                    "Challenge": "Challenge", "Correction": "Challenge and Correction"}
rename_targets = {'Speaker_Speech': "Speaker or Speech", "Countries_Group": "Group of Countries"}
rename_targets_interm = {'Law_Policy': "Law or Policy", 'Person': "Person (Non-representative of Country)",
                         "UN-Organization": "UN-Organization (other than UNSC)",
                         "Non-Governm_Grp": "Non-Governmental Group"}
rename_UK = {"United Kingdom Of Great Britain And Northern Ireland": "United Kingdom"}

# to general df preprocessing
def display_values_sankey(df):
    # rename values more user friendly
    df_display = df.copy()
    # Check if 'Conflict Type' is categorical
    if df_display['Conflict Type'].dtype.name == 'category':
        # Use rename_categories for categorical data
        df_display['Conflict Type'] = df_display['Conflict Type'].cat.rename_categories(rename_conflicts)
    else:
        # If not categorical, fallback to replace
        df_display['Conflict Type'] = df_display['Conflict Type'].replace(rename_conflicts)
    # Check if 'Conflict Type' is categorical
    if df_display['Conflict Target Group'].dtype.name == 'category':
        # Use rename_categories for categorical data
        df_display['Conflict Target Group'] = df_display['Conflict Target Group'].cat.rename_categories(rename_conflicts)
    else:
        # If not categorical, fallback to replace
        df_display['Conflict Target Group'] = df_display['Conflict Target Group'].replace(rename_targets)
    if df_display['Target Country'].dtype.name == 'category':
        # Use rename_categories for categorical data
        df_display['Target Country'] = df_display['Target Country'].cat.rename_categories(rename_UK, inplace=True)
    else:
        # If not categorical, fallback to replace
        df_display['Target Country'] = df_display['Target Country'].replace(rename_UK)
    return df_display

"""

def expand_colorlist(country_list, rgba_colors):
    # duplicates color list in case target list is bigger than available colors
    if len(country_list) > len(rgba_colors):
        rgba_colors = rgba_colors+rgba_colors
        return expand_colorlist(country_list, rgba_colors) # return the result of the recursive call
    else:
        return rgba_colors

def create_colors_column(num_rows, country_list, country_list_links):
    # map color to country
    # List of blue shades RGBA color values with alpha = 0.3
    #rgba_colors_blue = [(4, 59, 92, .3), (40, 67, 135, .3), (205, 209, 228, .3), (15, 10, 222, .3), (82, 78, 183, .3), (52, 45, 113, .3),
    #               (1, 1, 122, .3), (37, 41, 88, .3), (45, 85, 255, .3), (50, 50, 120, .3), (11, 127, 171, .3), (3, 138, 255, .3), (43, 44, 170, .3),
    #               (30, 81, 123, .3), (30, 139, 195, .3)]
    rgba_colors = [(213,94,0, .4), (204,121,167, .4), (0,114,178, .4), (240,228,66, .4), (0,158,115, .4)]
    rgba_colors = ["rgba"+str(x) for x in rgba_colors]
    # duplicate color list items in case there are more colors needed
    color_source = []
    rgba_colors_2 = expand_colorlist(country_list, rgba_colors)
    for i in range(len(country_list)):
        color_source.append(rgba_colors_2[i])

    color_links = []
    sourceid_color_dict = dict(zip(country_list, color_source))
    for i in country_list_links:
        color_links.append(sourceid_color_dict[i])
    assert num_rows == len(color_source)
    assert len(color_links) == len(country_list_links)
    return color_source, color_links

# for Sankey and Barchart
def prepare_columns(df):
    # merge columns Conflict Target
    df_ct1 = df.loc[df['Conflict Target Group'].notna()]
    df_ct2 = df.loc[df['Conflict Target Group 2'].notna()]
    df_ct1 = df_ct1.drop(['Conflict Target Group 2'], axis=1)
    df_ct2 = df_ct2.drop(['Conflict Target Group'], axis=1)
    df_ct2 = df_ct2.rename(columns={'Conflict Target Group 2':'Conflict Target Group'})
    df_ct_merged = pd.concat([df_ct2, df_ct1], axis=0)
    # merge columns Target Country, don't drop nans for Target_Country
    df_tc2 = df_ct_merged.loc[df['Target Country 2'].notna()]
    df_tc2 = df_tc2.drop(['Target Country'], axis=1)
    df_tc1 = df_ct_merged.drop(['Target Country 2'], axis=1)
    df_tc2 = df_tc2.rename(columns={'Target Country 2': 'Target Country'})

    df_merged = pd.concat([df_tc1, df_tc2], axis=0)

    return df_merged


def prepare_table_sankey(df):
    # prepare dfs for sankey
    df_val = df[['Country Speaker', 'Target Country']]

    df_val.loc[:, "Target Country"] = df_val["Target Country"].fillna("Underspecified")
    df_val.loc[:, "Target Country"] = df_val["Target Country"].replace("-None-", "Underspecified")
    df_val.loc[:, "Target Country"] = df_val["Target Country"].replace(" ", "Underspecified")
    df_count = df_val.groupby(by=['Country Speaker', "Target Country"], observed=False).size().reset_index(name="Count")

    # add speaker and target suffix
    df_count['Country Speaker'] = df_count['Country Speaker'].apply(lambda x: "{}{}".format(x, '_source'))
    df_count["Target Country"] = df_count["Target Country"].apply(lambda x: "{}{}".format(x, '_target'))

    all_links = df_count.copy()
    all_links.columns = ['source', 'target', 'value']

    # https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns
    unique_source_target = list(pd.unique(all_links[['source', 'target']].values.ravel('K')))
    # for assigning unique number to each source and target
    mapping_dict = {k: v for v, k in enumerate(unique_source_target)}

    # Lina new: create df_nodes
    df_nodes = pd.DataFrame(list(mapping_dict.items()), columns=["label", "ID"])
    df_nodes = df_nodes[["ID", "label"]]

    # return df_nodes as df_nodes and all_links as df_links
    # mapping of full data
    all_links['source'] = all_links['source'].map(mapping_dict)
    all_links['target'] = all_links['target'].map(mapping_dict)

    df_nodes['color'], all_links['link color'] = create_colors_column(df_nodes.shape[0], df_nodes['ID'].to_list(),
                                                                      all_links['source'].to_list())
    return all_links, df_nodes

