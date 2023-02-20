import pandas as pd

import os

from profile_scout.ml_logic.params import LOCAL_DATA_PATH

def get_data_local(
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
