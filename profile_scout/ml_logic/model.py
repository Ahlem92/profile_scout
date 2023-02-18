from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

def run_kmeans(X:pd.DataFrame,n_clusters=int):
    kmeans = KMeans(n_clusters=n_clusters, random_state =0)
    kmeans.fit(X)
    labels_kmeans = kmeans.predict(X)
    X['cluster_kmeans'] = labels_kmeans
    print("\n✅ kmeans labels assigned")
    return  X

def apply_cosine (data:pd.DataFrame, player_name = str):
    v1 = np.array(data.loc[player_name]).reshape(1, -1)
    sim1 = cosine_similarity(data, v1).reshape(-1)
    dictDf = {'Similar Players': sim1 }
    recommendation_df = pd.DataFrame(dictDf, index = data.index)
    recommendation_df.sort_values('Similar Players', ascending=False, inplace=True)
    print("\n✅ cosine applied")
    return recommendation_df

def merge_cosinedf (X:pd.DataFrame,df:pd.DataFrame,player_name= str,number_of_similar_profiles=int):
    results=pd.merge(X ,df,left_index=True, right_index=True).sort_values(by="Similar Players",ascending=False)
    bp=results.loc[player_name]["Best Position"]
    results=results[results["Best Position"]==bp]
    return results.head(number_of_similar_profiles)
