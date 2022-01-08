import numpy as np
import pandas as pd
import requests
import yfinance as yf
import datetime as dt
from configs import *
import math




def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + telegram_api_key + '/sendMessage?chat_id=' + chat_id + '&parse_mode=MarkdownV2&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    

# telegram_bot_sendtext("*Testing Telegram bot*")


lookback = dt.date.today() - dt.timedelta(days=5)
df = yf.download(tickers, lookback, interval='1d')['Adj Close']
change = round(100*df.pct_change(),2)


btc_price = str(round(df.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
usd_price = str(round(df.iloc[-1, 2],2)).replace('.', '\\.').replace('-', '\\-')
snp_price = str(round(df.iloc[-1, 3],2)).replace('.', '\\.').replace('-', '\\-')
eth_price = str(round(df.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')

btc_change = str(round(change.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
usd_change = str(round(change.iloc[-1, 2],2)).replace('.', '\\.').replace('-', '\\-')
snp_change = str(round(change.iloc[-1, 3],2)).replace('.', '\\.').replace('-', '\\-')
eth_change = str(round(change.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')

daily_message = f"*Daily Update:* \nBitcoin: ${btc_price}"

if change.iloc[-1, 0] > 0:
    daily_message += f"\nUp from yesterday by: {btc_change}%\n"
else:
    daily_message += f"\nDown from yesterday by: {btc_change}%\n"


daily_message += f"\nEthereum: ${eth_price}"

if change.iloc[-1, 1] > 0:
    daily_message += f"\nUp from yesterday by: {eth_change}%\n"
else:
    daily_message += f"\nDown from yesterday by: {eth_change}%\n"



if math.isnan(df.iloc[-1, 2]):
    daily_message += f"\nZAR/USD: Market Closed\n"
else:
    daily_message += f"\nZAR/USD: R{usd_price}"
    if change.iloc[-1, 2] > 0:
        daily_message += f"\nUp from yesterday by: {usd_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {usd_change}%\n"
    


if math.isnan(df.iloc[-1, 3]):
    daily_message += f"\nSP500: Market Closed\n"
else:
    daily_message += f"\nSP500: ${snp_price}"
    if change.iloc[-1, 3] > 0:
        daily_message += f"\nUp from yesterday by: {snp_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {snp_change}%\n"

FGurl = 'https://api.alternative.me/fng/?limit=1&format=json'

x = requests.get(FGurl)
index = x.json()
# print(index['data'][0]['value_classification'])

daily_message += f"\nFear and Greed Index: *{index['data'][0]['value']} \({index['data'][0]['value_classification']}\)*\n"
# daily_message += f"\nFear and Greed Classification: {index['data'][0]['value_classification']}\n"

t = telegram_bot_sendtext(daily_message)
print(t)
print('')

