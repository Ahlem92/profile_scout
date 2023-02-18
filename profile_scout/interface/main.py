import sys
import numpy as np
import pandas as pd


from profile_scout.ml_logic.data import clean_data, get_data
from profile_scout.ml_logic.model import run_kmeans, apply_cosine, merge_cosinedf
from profile_scout.ml_logic.preprocessor import preprocess_features
from profile_scout.ml_logic.column_selector import select_columns

def main(player,number):
    df = get_data()
    df2 = clean_data(df)
    data_processed = preprocess_features(df2)
    df_with_cluster = run_kmeans(data_processed,80)
    df.drop_duplicates(inplace=True)
    df.set_index("Full Name",inplace=True)
    df_with_cluster.set_index(df.index,inplace=True)
    recommandation_df = apply_cosine(df_with_cluster, player)
    final_df = merge_cosinedf(recommandation_df, df, player,(number+1))
    final_df=select_columns(final_df)
    return final_df

if __name__ == '__main__':
    arg=sys.argv
    player=arg[1]
    number=int(arg[2])
    final_df=main(player,number)
    print(final_df)
