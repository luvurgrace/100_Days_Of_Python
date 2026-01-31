import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
YESTERDAY = "2025-12-05"
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
PRICE_API_KEY = "A2UYMDAX4BY02CG7"
NEWS_API_KEY = "40129b61afd5471180e5901f185ab88a"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": PRICE_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()
daily_data = data["Time Series (Daily)"]
close_prices_daily = [value["4. close"] for (date, value) in daily_data.items()]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_close_prince = float(close_prices_daily[0])

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_close_prince = float(close_prices_daily[1])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
poss_difference = round(abs(yesterday_close_prince-before_yesterday_close_prince),2)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round(((yesterday_close_prince-before_yesterday_close_prince)/before_yesterday_close_prince)*100,2)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 0:
    sign = "🔺"
else:
    sign = "🔻"

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": YESTERDAY,
    "to": YESTERDAY
}
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_last_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
print(three_last_articles)
format_articles = [f"{STOCK_NAME}: {sign}{percentage_diff}%\nHeadline: {article["title"]}\nBrief: {article["description"]}." for article in three_last_articles]

#TODO 9. - Send each article as a separate message via Twilio.

client = Client(account_sid, auth_token)

for article in format_articles:
    message = client.messages.create(
        body= article,
        from_ = "+12707431240",
        to = "+375297584457"
    )
    print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

