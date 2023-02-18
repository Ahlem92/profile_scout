import os
import numpy as np

LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
PROJECT = os.environ.get("PROJECT")
DATASET = os.environ.get("DATASET")
BUCKET = os.environ.get("BUCKET")
BLOB = os.environ.get("BLOB")




################## VALIDATIONS #################

env_valid_options = dict(
    DATA_SOURCE=["local", "bigquery"],
)
