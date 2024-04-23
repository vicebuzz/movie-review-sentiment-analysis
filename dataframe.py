import pandas as pd
import numpy as np

def replace_trailing_speech_marks(x):
    return x.replace('""', "'")

df = pd.read_csv('movie.csv')

df['text'] = df['text'].str.strip().str.replace('""', "'")

df.to_csv('movie_edited.csv', index=False)