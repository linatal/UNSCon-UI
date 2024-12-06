import pandas as pd
from utils.helper import define_dtypes

def merge_frames(df_speaker, df_conflicts):
    # merge two dfs on filename, get metadata (countryname, etc.) from df_speaker and add it to df_conflicts
    df_new = df_conflicts.merge(df_speaker, left_on='filename', right_on='filename')
    print(f"shape of conflicts dataframe (sentences): {df_conflicts.shape};\nshape of new dataframe: {df_new.shape}", )
    assert df_conflicts.shape[0] == df_new.shape[0]
    return df_new


def rename_values_target_country(df):
    columns_target = ['Target Country', 'Target Country 2']
    df.loc[(df['Conflict Type'].notna()) & (df['Target Country'].isna()), 'Target Country'] = "Underspecified"
    for column in columns_target:
        df[column] = df[column].str.replace('_', ' ')
        df[column] = df[column].str.title()
        df[column] = df[column].str.replace("United Kingdom Of Great Britain And Northern Ireland", "United Kingdom")

    return df



def merge_columns(df_conflicts):
    df_conflicts['Conflict_Type'] = df_conflicts['A0_Negative_Evaluation'].fillna(df_conflicts['B1_ChallengeType'])
    df_conflicts['Conflict_Target'] = df_conflicts['A2_Target_Council'].fillna(df_conflicts['B2_Target_Challenge'])
    df_conflicts['Target_Country'] = df_conflicts['A4_Country_Name'].fillna(df_conflicts['B3_Country_Name'])
    return df_conflicts

def rename_columns(df):
    # rename columns for diplaying (without changing the source data)
    colnames = {'text': "Text (Sentence-split)", 'Conflict_Type': 'Conflict Type',
                'Conflict_Target': 'Conflict Target Group', 'A2_Target_Council_2': 'Conflict Target Group 2',
                'A3_Target_Intermediate' : 'Conflict Target Intermediate',
                'Target_Country': 'Target Country', 'A4_Country_Name_2': 'Target Country 2',
                'country': 'Country Speaker',
                'filename': 'Speech-ID filename', 'speaker': 'Speaker Name',
                'participanttype': 'Participant-Type', 'date': 'Date of Debate',
                'speech_sentence_id': 'Sentence-ID', 'paragraph_id': 'Paragraph-ID', 'speech': 'Speech-Num. in Debate'}
    df_renamed = df.rename(columns=colnames)
    return df_renamed


def rename_values(df):
    # rename values more user friendly
    rename_conflict_values = {'Direct_NegEval': "Direct Conflict", 'Indirect_NegEval': "Indirect Conflict",
                        "Challenge": "Challenge", "Correction": "Challenge and Correction"}
    rename_target_values = {'Speaker_Speech': "Speaker or Speech", "Countries_Group": "Group of Countries"}
    rename_target_interm_values = {'Law_Policy': "Law or Policy", 'Person': "Person (Non-representative of Country)",
                             "UN-Organization": "UN-Organization (other than UNSC)",
                             "Non-Governm_Grp": "Non-Governmental Group"}
    rename_UK_values = {"United Kingdom Of Great Britain And Northern Ireland": "United Kingdom"}

    df_display = df.copy()
    df_display['Conflict Type'] = df_display['Conflict Type'].cat.rename_categories(rename_conflict_values)
    df_display['Conflict Target Group'] = df_display['Conflict Target Group'].cat.rename_categories(rename_target_values)
    df_display['Conflict Target Group 2'] = df_display['Conflict Target Group 2'].cat.rename_categories(rename_target_values)
    df_display['Conflict Target Intermediate'] = df_display['Conflict Target Intermediate'].cat.rename_categories(rename_target_interm_values)
    df_display['Country Speaker'] = df_display['Country Speaker'].cat.rename_categories(rename_UK_values)
    return df_display

def add_topics(df):
    fileid_list = df['filename'].str[:18].to_list()
    listi = []
    for fileid in fileid_list:
        if fileid in{"UNSC_2016_SPV.7643", "UNSC_2016_SPV.7658"}:
            listi.append("WPS")
        elif fileid in {"UNSC_2014_SPV.7165", "UNSC_2014_SPV.7138", "UNSC_2014_SPV.7219", "UNSC_2014_SPV.7154"}:
            listi.append("Ukraine")
        else:
            listi.append(None)
            print("Warning, there is a row with no Subject entry, append None value.")
    if len(listi) == len(df):
        df = df.copy()
        df.loc[:, 'Subject'] = listi
    else:
        raise ValueError("The length of list must match the number of rows in the DataFrame.")
    return df

def prapare_and_merge_dataframe(df_conflicts, df_speaker):
    # prepare country names
    #target_country_columns = ["A4_Country_Name", "A4_Country_Name_2", "B3_Country_Name", "B3_Country_Name_2"]
    #df_conflicts = rename_target_country(df_conflicts, "A0_Negative_Evaluation", target_country_columns)
    # prepare filename column to enable merging with df_speaker
    df_conflicts['filename'] = df_conflicts['fileid'].astype(str) + '.txt'
    # replace '_' and '-NONE-' with None
    df_conflicts = df_conflicts.replace({"_": None, "-NONE-": None})

    df_conflicts = merge_columns(df_conflicts)
    # keep only necessary columns to merge in df_speaker
    df_speaker = df_speaker[['speech', 'country', 'speaker', 'participanttype', 'date', 'filename']]
    # merge dataframes
    df_conflicts_merged = merge_frames(df_speaker, df_conflicts)
    # include only rows where sentence_text is specifically a string
    df_conflicts_merged = df_conflicts_merged[df_conflicts_merged['text'].apply(lambda x: isinstance(x, str))]

    df_subj = add_topics(df_conflicts_merged)
    df_renamed = rename_columns(df_subj)
    # keep only interesting columns
    df_renamed = df_renamed[['Text (Sentence-split)',
                               "Conflict Type",
                               "Conflict Target Group", "Conflict Target Group 2",
                               "Conflict Target Intermediate",
                               "Target Country", "Target Country 2",
                               "Country Speaker", "Speaker Name", "Participant-Type", "Date of Debate",
                               "Sentence-ID", "Paragraph-ID", "Speech-ID filename", "Speech-Num. in Debate", "Subject"]]
    df_renamed_val = rename_values_target_country(df_renamed)
    df_dtypes = define_dtypes(df_renamed_val)
    df_renamed = rename_values(df_dtypes)
    return df_renamed



def main():
    speaker_csv_path = "./dataset/speaker.tsv"
    conflict_annotations_sentences_csv_path = "./dataset/main_conflicts_sents.csv"
    df_speaker = pd.read_csv(speaker_csv_path, delimiter="\t")
    df_conflicts = pd.read_csv(conflict_annotations_sentences_csv_path, delimiter=",", index_col=0)
    cleanup_frame = prapare_and_merge_dataframe(df_conflicts, df_speaker)

    cleanup_frame.to_csv("./dataset/conflict_annotations4UI.csv", sep=",")


if __name__ == "__main__":
    main()