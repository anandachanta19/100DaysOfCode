import datetime as dt
import os
import requests
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client


STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
TODAY = dt.datetime.now().date()
YESTERDAY = TODAY - dt.timedelta(days=1)
DAY_BEFORE_YESTERDAY = YESTERDAY - dt.timedelta(days=1)

load_dotenv(find_dotenv(".env"))

STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("STOCK_API_KEY")
}

NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "from": DAY_BEFORE_YESTERDAY,
    "sortBy": "popularity",
    "apikey": os.getenv("NEWS_API_KEY")
}


def get_news():
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    print(news_response.url)
    data = news_response.json()
    if data["totalResults"] > 0:
        headline = data["articles"][0]["title"]
        brief = data["articles"][0]["description"]
        return headline, brief
    else:
        return None


def send_news(head, content, percent):
    symbol = None
    if percent > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body=f"{STOCK}: {symbol}{percent}%\n"
                     f"Headline: {head}\n"
                     f"Brief: {content} ", from_=os.getenv("TWILIO_PHONE_NUMBER"),
                to=os.getenv("MY_PHONE_NUMBER"))


# Getting Stock Details
stock_response = requests.get(url="https://www.alphavantage.co/query", params=STOCK_PARAMETERS)
stock_response.raise_for_status()

yesterday_details = int(
    stock_response.json()["Time Series (Daily)"][YESTERDAY]["4. close"]
)

day_before_yesterday_details = int(
    stock_response.json()["Time Series (Daily)"][DAY_BEFORE_YESTERDAY]["4. close"]
)

profit = yesterday_details - day_before_yesterday_details
change_percent = profit / max(yesterday_details, day_before_yesterday_details)
if abs(change_percent) > 5:
    headLine, Brief = get_news()
    if headLine is not None and Brief is not None:
        send_news(headLine, Brief, change_percent)


