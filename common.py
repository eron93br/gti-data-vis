import time
from utils import _LOREM_IPSUM, DATASET_URL
import pandas as pd
import numpy as np
import plotly.express as px

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

def load_tips_dataset() -> pd.DataFrame:
    return pd.read_csv(DATASET_URL)

def make_visualization1(df):
    return px.histogram(df, x="tip")
