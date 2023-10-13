# Stock-News Project

## Overview
The Stock-News project aims to analyze the stock market and identify significant price changes in specified stocks. Whenever a stock price changes by more than 5% compared to the previous day, the system fetches the most relevant news regarding that stock to provide insights into what might have caused the price movement. This project leverages the Alpha Vantage API for stock price data and the NewsAPI for gathering news articles.

## Features
- Track specified stocks and identify significant price changes (more than 5%)
- Fetch and display relevant news articles for stocks with significant price changes
- Utilizes Alpha Vantage API for real-time and historical stock data
- Utilizes NewsAPI for fetching recent news articles related to the stocks of interest

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-news.git
   cd stock-news
   ```

2. Install the required dependencies:
   ```bash
   pip install python-dotenv
   ```

3. Set up your API keys:

   You'll need to get your own API keys from Alpha Vantage and NewsAPI. 

   Create a file named `config.py` in the project root, and add your API keys like so:
   ```python
   ALPHA_VANTAGE_API_KEY = 'your-alpha-vantage-api-key'
   NEWSAPI_API_KEY = 'your-newsapi-api-key'
   ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```

2. The script will check the specified stock prices for significant changes compared to the previous day. If a change of more than 5% is detected, it will fetch and display the most relevant news articles regarding that stock.
