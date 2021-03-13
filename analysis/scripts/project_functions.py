import pandas as pd
import numpy as np

def read_and_process(url_or_path):
    df = (
        pd.read_csv(url_or_path)
        .rename(columns={"track":"Track", "artist":"Artist", "danceability":"Danceability", "energy":"Energy", "key":"Key", "loudness":"Loudness",      "mode":"Mode", "speechiness":"Speechiness", "acousticness":"Acousticness", "instrumentalness":"Instrumentalness", "liveness":"Liveness",   "valence":"Valence", "tempo":"Tempo", "time_signature":"Time Signature", "target":"Target"})
        .drop(axis =1, columns={'chorus_hit','sections','duration_ms','Speechiness','Acousticness','Instrumentalness','uri','Liveness'})
        .dropna()
        .sort_values(by = ['Track'])
    )
    
    return df