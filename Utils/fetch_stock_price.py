import requests


def fetch_data(symbol, api_key):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key
    }
    r = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    return r.json()


