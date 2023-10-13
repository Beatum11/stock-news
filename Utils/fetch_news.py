import requests


def fetch_news(theme, from_date, to_date, api_key):

    parameters = {
        "q": theme,
        "from": from_date,
        "to": to_date,
        "sortBy": "popularity",
        "apiKey": api_key
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    data = response.json()

    return data["articles"]

# Example of an article extraction
# article = data["articles"][0]