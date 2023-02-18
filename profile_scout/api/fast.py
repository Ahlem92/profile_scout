import pytz
import pandas as pd

from profile_scout.interface.main import get_similar_profiles


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/get_profiles")
def get_profiles(player_name: str,
            number_of_similar_profiles: int):

    df=get_similar_profiles(player_name,number_of_similar_profiles)

    return df
