from Utils.fetch_stock_price import fetch_data
from Utils.date_utils import get_yesterday, day_before


WEEKEND_DAYS = {5, 6}
CLOSE_KEY = '4. close'
TIME_SERIES_KEY = "Time Series (Daily)"


# Here we're taking the closing price for a specific date
def get_closing_price(data, date):
    return float(data[TIME_SERIES_KEY][str(date)][CLOSE_KEY])


# Here we want to check whether it's a weekday or not
def is_weekend(date):
    return date.weekday() in WEEKEND_DAYS


def get_stock_prices(symbol, api_key):
    closing_price_dict = {}
    data = fetch_data(symbol, api_key)

    for day in [get_yesterday(), day_before()]:
        if not is_weekend(day):
            try:
                closing_price = get_closing_price(data, day)
                closing_price_dict[str(day)] = closing_price
            except KeyError:
                closing_price_dict[str(day)] = "Data not available"
        else:
            closing_price_dict[str(day)] = "Weekend"

    return closing_price_dict
