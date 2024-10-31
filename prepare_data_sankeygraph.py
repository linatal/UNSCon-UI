# imports dataset df and prepares it for sankey display
import pandas as pd
import matplotlib.colors as mcolors
import random


def expand_colorlist(country_list, rgba_colors):
    # doubles color list in case target list is bigger than available colors
    if len(country_list) > len(rgba_colors):
        rgba_colors = rgba_colors+rgba_colors
        return expand_colorlist(country_list, rgba_colors) # return the result of the recursive call
    else:
        print()
        return rgba_colors

def create_colors_column(num_rows, country_list, num_rows_links, country_list_links):
    # map color to country
    # Generate 100 RGBA color values with alpha = 0.3
    #rgba_colors = [(random.randint(0, 0), random.randint(0, 255), random.randint(0, 255), .3) for _ in range(100)]
    # list of blue shades
    rgba_colors = [(4, 59, 92, .3), (40, 67, 135, .3), (205, 209, 228, .3), (15, 10, 222, .3), (82, 78, 183, .3), (52, 45, 113, .3),
                   (1, 1, 122, .3), (37, 41, 88, .3), (45, 85, 255, .3), (50, 50, 120, .3), (11, 127, 171, .3), (3, 138, 255, .3), (43, 44, 170, .3),
                   (30, 81, 123, .3), (30, 139, 195, .3)]
    rgba_colors = ["rgba"+str(x) for x in rgba_colors]

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


def prepare_table_sankey(df):
    # prepare dfs for sankey


    df_val_1 = df[["country", "Target_Country"]]
    df_val_1 = df_val_1[df_val_1["Target_Country"].notna()]

    df_val_2 = df[["country", "Target_Country_2"]]
    df_val_2 = df_val_2[df_val_2["Target_Country_2"].notna()]
    df_val_2 = df_val_2.rename(columns={"Target_Country_2": "Target_Country"})

    df_val = pd.concat([df_val_1, df_val_2], ignore_index=True, sort=False)

    df_count = df_val.groupby(by=["country", "Target_Country"]).size().reset_index(name="Count")

    # shorten UK name
    rename_UK = {"United Kingdom Of Great Britain And Northern Ireland": "United Kingdom"}
    df_count['country'] = df_count['country'].replace(rename_UK)
    df_count['Target_Country'] = df_count['Target_Country'].replace(rename_UK)

    # add speaker and target suffix
    df_count["country"] = df_count["country"].apply(lambda x: "{}{}".format(x, '_speaker'))
    df_count["Target_Country"] = df_count["Target_Country"].apply(lambda x: "{}{}".format(x, '_target'))

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

    df_nodes['color'], all_links['link color'] = create_colors_column(df_nodes.shape[0], df_nodes['ID'].to_list(), all_links.shape[0], all_links['source'].to_list())
    #all_links['link color'] = create_colors_column(all_links.shape[0], all_links['target'])

    # converting full dataframe as list for using with in plotly
    links_dict = all_links.to_dict(orient='list')

    return all_links, df_nodes

