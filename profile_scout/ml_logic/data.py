import os
import pandas as pd

#from profile_scout.ml_logic.params import LOCAL_DATA_PATH

def get_data(
                     columns: list = None,
                     verbose=True) -> pd.DataFrame:
    """
    return the raw dataset from local disk
    """
    path ='raw_data/Fifa23_data.csv'

    try:

        df = pd.read_csv(
                path)

        if columns is not None:
            df.columns = columns

    except pd.errors.EmptyDataError:

        return None  # end of data

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    clean raw data by removing  irrelevant columns from the raw data set
    """
    df=df.drop_duplicates()
    cols_todrop=[4,7,8,14,15,16,17,18,19,20,21,26,27,28,29]
    df2=df.drop(df.columns[cols_todrop],axis=1)
    df2[['Position 1','Position 2','Position 3']] = df2["Positions Played"].apply(lambda x: pd.Series(str(x).split(",")))
    map_position= {
    'GK': 'Goalkeeper',
    'CB': 'Defender',
    'RB': 'Defender',
    'LB': 'Defender',
    'RWB': 'Defender',
    'LWB': 'Defender',
    'CM': 'Midfielder',
    'CDM': 'Midfielder',
    'CAM': 'Midfielder',
    'RM': 'Midfielder',
    'LM': 'Midfielder',
    'ST': 'Forward',
    'CF': 'Forward',
    'RF': 'Forward',
    'LF': 'Forward',
    'RW': 'Forward',
    'LW': 'Forward'
}
    df2['Poste'] = df2['Best Position'].map(map_position)
    cols_todrop=[8,11,15,16,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76]
    df3=df2.drop(df2.columns[cols_todrop],axis=1)
    df3=df3.join(pd.get_dummies(df2['Poste'])).join(pd.get_dummies(df2['Best Position']))
    df3['Forward Rating'] = df2[['ST Rating','CF Rating','RF Rating','LF Rating','RW Rating','LW Rating']].mean(axis=1)
    df3['Midfielder Rating'] = df2[['CM Rating','CDM Rating','CAM Rating','RM Rating','LM Rating']].mean(axis=1)
    df3['Defender Rating'] = df2[['CB Rating','RB Rating','LB Rating','RWB Rating','LWB Rating']].mean(axis=1)
    df3['Goalkeeper Rating'] = df2['GK Rating']
    df3=df3.join(pd.get_dummies(df2['Preferred Foot']))
    df3=df3.join(pd.get_dummies(df2['Attacking Work Rate']))
    df3.rename(columns={'High':'HAWR','Low':'LAWR','Medium':'MAWR'},inplace=True)
    df3=df3.join(pd.get_dummies(df2['Defensive Work Rate']))
    df3.rename(columns={'High':'HDWR','Low':'LDWR','Medium':'MDWR'},inplace=True)
    df3.rename(columns={'Right':'Shooting Foot'},inplace=True)
    cols_todrop=[46,48,49,50,51,52,63,73,74,75,76,77]
    df3=df3.drop(df3.columns[cols_todrop],axis=1)
    cols_todrop=[*range(48,66)]
    data=df3.drop(df3.columns[cols_todrop],axis=1)
    data=data.set_index("Full Name")
    data.drop(columns=["Overall",  "Potential", "TotalStats", "BaseStats",'HAWR','LAWR','MAWR','HDWR','LDWR','MDWR',"Poste","Known As","Best Position","Positions Played"], inplace=True)

    print("\n✅ data cleaned")

    return data
