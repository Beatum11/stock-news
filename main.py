from Services.stock_service import get_stock_prices
from Services.prices_comparison_service import count_difference
from Utils.date_utils import get_yesterday, day_before
from Services.news_service import get_three_articles
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
ALPHA_API_KEY = os.environ.get("ALPHA_VANT_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

symbol_for_check = input("What company you want to check: ")
try:
    # Get stock data
    data = get_stock_prices(symbol_for_check, ALPHA_API_KEY)

    # Check for 5% price difference
    differ = count_difference(yest_num=data[str(get_yesterday())], bef_yest_num=data[str(day_before())])

    # Fetch and display news if there's a 5% price difference
    if differ:
        articles = get_three_articles(symbol_for_check, from_date=str(day_before()),
                                      to_date=str(get_yesterday()),
                                      api_key=NEWS_API_KEY)
        print(articles)
    else:
        print("The difference is normal")

except Exception as e:
    print(f"An error occurred: {e}")





