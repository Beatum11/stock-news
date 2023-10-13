from Utils.fetch_news import fetch_news


def get_three_articles(theme, from_date, to_date, api_key):
    data = fetch_news(theme, from_date, to_date, api_key)

    final_articles = []
    for item in range(3):
        final_articles.append(data[item])

    return final_articles