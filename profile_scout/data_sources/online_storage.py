import pandas as pd

from profile_scout.ml_logic.params import BUCKET, BLOB

from google.cloud import storage


def get_data_online(verbose=True) -> pd.DataFrame:
    """
    return the datafram from bucket
    """

    # $CHA_BEGIN
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET)
    blob = bucket.blob(BLOB)
    with blob.open("r") as f:
       df=pd.read_csv(f)

    return df
