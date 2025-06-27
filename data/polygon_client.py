import requests
import pandas as pd
from config import POLYGON_API_KEY

def get_ohlc(ticker: str, multiplier: int, timespan: str, from_date: str, to_date: str):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    params = {
        "adjusted": "true",
        "sort": "asc",
        "limit": 5000,
        "apiKey": POLYGON_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        raise ValueError(f"No data for {ticker}: {data}")

    df = pd.DataFrame(data["results"])
    df["timestamp"] = pd.to_datetime(df["t"], unit="ms")
    df = df.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"})
    return df[["timestamp", "open", "high", "low", "close", "volume"]]
