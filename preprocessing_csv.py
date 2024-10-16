import pandas as pd

def merge_frames(df_speaker, df_conflicts):
    # merge on filename
    df_new = df_conflicts.merge(df_speaker, left_on='filename', right_on='filename')
    print(f"shape of conflicts (sentence) dataframe: {df_conflicts.shape};\nshape of new dataframe: {df_new.shape}", )
    assert df_conflicts.shape[0] == df_new.shape[0]
    return df_new

def clean_up_dataframes(df_c, df_s):
    # delete uneccessary rows
    df_s = df_s[['country', 'speaker', 'participanttype', 'date', 'filename']]
    # delete Country column with incorrect values (we will use correct ones from speaker.tsv)
    df_c = df_c.drop(['country'], axis=1)
    # unify None annotations
    df_c = df_c.replace("_", None)
    df_c = df_c.replace("-NONE-", None)
    # merge conflict, target and target country annotations to one column respectively
    df_c['Conflict_Type'] = df_c['A0'].fillna(df_c['B1'])
    df_c['Conflict_Target'] = df_c['A2'].fillna(df_c['B2'])
    df_c['Target_Country'] = df_c['A4'].fillna(df_c['B3'])

    # rename target country values
    df_c['Target_Country'] = df_c['Target_Country'].str.replace('_', ' ')
    # capitalize
    df_c['Target_Country'] = df_c['Target_Country'].str.title()
    # add .txt ending to each value in filename column to enable merging with speaker.tsv
    df_c['filename'] = df_c['filename'].astype(str) + '.txt'
    # merge dataframes!
    df_c_merged = merge_frames(df_s, df_c)
    # keep only interesting columns
    df_c_merged = df_c_merged[['sentence_text', "Conflict_Type", "Conflict_Target", "Target_Country", 'speech_id', 'country',
             'speaker', 'participanttype', 'date']]

    return df_c_merged

def main():
    speaker_csv_path = "./dataset/speaker.tsv"
    conflict_annotations_sentences_csv_path = "./dataset/conflict_annotations_sentences.csv"
    df_speaker = pd.read_csv(speaker_csv_path, delimiter="\t")
    df_conflicts = pd.read_csv(conflict_annotations_sentences_csv_path, delimiter=",")

    new_frame = clean_up_dataframes(df_conflicts, df_speaker)

    new_frame.to_csv("./dataset/conflict_annotations4UI.csv", sep=",")


if __name__ == "__main__":
    main()