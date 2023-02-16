import pandas as pd

import os

from profile_scout.ml_logic.params import LOCAL_DATA_PATH

def get_data(path: str,
                     index: int,
                     chunk_size: int,
                     dtypes,
                     columns: list = None,
                     verbose=True) -> pd.DataFrame:
    """
    return the raw dataset from local disk
    """
    path = os.path.join(
        os.path.expanduser(LOCAL_DATA_PATH),
        "processed" if "processed" in path else "raw",
        f"{path}.csv")


    try:

        df = pd.read_csv(
                path,
                skiprows=index + 1,  # skip header
                nrows=chunk_size,
                dtype=dtypes,
                header=None)  # read all rows

        # read_csv(dtypes=...) will silently fail to convert data types, if column names do no match dictionnary key provided.
        if isinstance(dtypes, dict):
            assert dict(df.dtypes) == dtypes

        if columns is not None:
            df.columns = columns

    except pd.errors.EmptyDataError:

        return None  # end of data

    return df
