import pandas as pd

def merge_frames(df_speaker, df_conflicts):
    # merge two dfs on filename, get metadata (countryname, etc.) from df_speaker and add it to df_conflicts
    df_new = df_conflicts.merge(df_speaker, left_on='filename', right_on='filename')
    print(f"shape of conflicts dataframe (sentences): {df_conflicts.shape};\nshape of new dataframe: {df_new.shape}", )
    assert df_conflicts.shape[0] == df_new.shape[0]
    return df_new


def clean_up_dataframes(df_c, df_s):
    # delete uneccessary rows
    df_s = df_s[['speech', 'country', 'speaker', 'participanttype', 'date', 'filename']]
    # unify None annotations
    df_c = df_c.replace("_", None)
    df_c = df_c.replace("-NONE-", None)
    # merge conflict, target and target country annotations to one column respectively and rename
    # or, only rename column
    df_c['Conflict_Type'] = df_c['A0_Negative_Evaluation'].fillna(df_c['B1_ChallengeType'])
    df_c['Conflict_Target'] = df_c['A2_Target_Council'].fillna(df_c['B2_Target_Challenge'])
    df_c = df_c.rename(columns={'A2_Target_Council_2':'Conflict_Target_2'})

    df_c['Target_Country'] = df_c['A4_Country_Name'].fillna(df_c['B3_Country_Name'])

    df_c = df_c.rename(columns={'A3_Target_Intermediate':'Conflict_Target_Intermediate'})
    df_c = df_c.rename(columns={'A4_Country_Name_2': 'Target_Country_2'})
    df_c = df_c.rename(columns={'text': 'sentence_text'})
    # rename target country values
    df_c['Target_Country'] = df_c['Target_Country'].str.replace('_', ' ')
    df_c['Target_Country_2'] = df_c['Target_Country_2'].str.replace('_', ' ')
    # capitalize
    df_c['Target_Country'] = df_c['Target_Country'].str.title()
    df_c['Target_Country_2'] = df_c['Target_Country_2'].str.title()
    # add .txt ending to each value in filename column to enable merging with speaker.tsv
    df_c['filename'] = df_c['fileid'].astype(str) + '.txt'
    # merge dataframes
    df_c_merged = merge_frames(df_s, df_c)
    # keep only interesting columns
    df_c_merged = df_c_merged[['sentence_text',
                               "Conflict_Type",
                               "Conflict_Target", "Conflict_Target_2",
                               "Conflict_Target_Intermediate",
                               "Target_Country", "Target_Country_2",
                               "country", "speaker", "participanttype", "date",
                               "speech_sentence_id", "paragraph_id", 'filename', 'speech']]
    #include only rows where sentence_text is specifically a string
    df_c_merged_filtered = df_c_merged[df_c_merged['sentence_text'].apply(lambda x: isinstance(x, str))]
    return df_c_merged_filtered


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
    assert len(fileid_list) == len(listi)
    df['Subject'] = listi
    return df


def main():
    speaker_csv_path = "./dataset/speaker.tsv"
    conflict_annotations_sentences_csv_path = "./dataset/main_conflicts_sents.csv"
    df_speaker = pd.read_csv(speaker_csv_path, delimiter="\t")
    df_conflicts = pd.read_csv(conflict_annotations_sentences_csv_path, delimiter=",", index_col=0)

    cleanup_frame = clean_up_dataframes(df_conflicts, df_speaker)
    new_frame = add_topics(cleanup_frame)

    new_frame.to_csv("./dataset/conflict_annotations4UI.csv", sep=",")


if __name__ == "__main__":
    main()