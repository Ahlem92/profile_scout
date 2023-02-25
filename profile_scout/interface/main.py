import sys
import numpy as np
import pandas as pd


from profile_scout.ml_logic.data import clean_data, get_data
from profile_scout.ml_logic.model import run_kmeans, apply_cosine, merge_cosinedf
from profile_scout.ml_logic.preprocessor import preprocess_features
from profile_scout.ml_logic.column_selector import select_columns

def load_model():
    df = get_data()
    df2 = clean_data(df)
    data_processed = preprocess_features(df2)
    df_with_cluster = run_kmeans(data_processed,80)
    df.drop_duplicates(inplace=True)
    df.set_index("Full Name",inplace=True)
    df_with_cluster.set_index(df.index,inplace=True)
    return df_with_cluster

def get_similar_profiles(player_name,number_of_similar_profiles,**kwargs):
    df = get_data()
    df.drop_duplicates(inplace=True)
    df.set_index("Full Name",inplace=True)
    recommandation_df = apply_cosine(df_with_cluster, player_name)
    final_df = merge_cosinedf(recommandation_df, df, player_name)
    final_df['Contract Until'].replace('-', '2023', inplace = True)
    final_df['Contract Until'].replace('2022', '2023', inplace = True)
    final_df['Contract Until']=final_df['Contract Until'].astype(int)
    final_df = select_columns(final_df)
    player=final_df.loc[player_name]
    similar_profiles=final_df.drop(index=player_name)
    if kwargs['age'] is not None:
        similar_profiles=similar_profiles[similar_profiles['Age'] <= int(kwargs['age'])]
    if kwargs['height'] is not None:
        similar_profiles=similar_profiles[similar_profiles['Height(in cm)'] >= int(kwargs['height'])]
    if kwargs['value_euro'] is not None:
        similar_profiles=similar_profiles[similar_profiles['Value(in Euro)'] <= int(kwargs['value_euro'])]
    if kwargs['contract_until'] is not None:
        similar_profiles=similar_profiles[(similar_profiles['Contract Until']) <= int(kwargs['contract_until'])]
    if kwargs['release_clause'] is not None:
        similar_profiles=similar_profiles[(similar_profiles['Release Clause']) <= int(kwargs['release_clause'])]
    if kwargs['nationality'] is not None:
        similar_profiles=similar_profiles[(similar_profiles['Nationality']) == (kwargs['nationality'])]

    similar_profiles=similar_profiles.head(number_of_similar_profiles)

    return player, similar_profiles

df_with_cluster = load_model()

if __name__ == '__main__':
    arg=sys.argv
    player_name=arg[1]
    number_of_similar_profiles=int(arg[2])
    final_df=get_similar_profiles(player_name,number_of_similar_profiles)
    print(final_df)
