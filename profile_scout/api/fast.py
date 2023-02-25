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
            number_of_similar_profiles: int,
            age = None, height = None, value_euro = None, contract_until = None,
            release_clause = None,
            nationality= None):
    player,similar_profiles=get_similar_profiles(player_name,
                                                 number_of_similar_profiles,
                                                 age = age,
                                                 height = height,
                                                 value_euro = value_euro,
                                                 contract_until = contract_until,
                                                 release_clause = release_clause,
                                                 nationality = nationality)
    return player.to_dict(),similar_profiles.to_dict()


@app.get("/")
def root():
    return dict(greeting="Hello")
