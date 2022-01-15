from configs import *
import requests
import yfinance as yf
import datetime as dt
from datetime import datetime


def telegram_bot_sendtext(bot_message, chat_id):
    send_text = 'https://api.telegram.org/bot' + telegram_api_key + '/sendMessage?chat_id=' + chat_id + '&parse_mode=MarkdownV2&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def crypto_update(crypto_tickers):
    lookback = dt.date.today() - dt.timedelta(days=5)
    df = yf.download(crypto_tickers, lookback, interval='1d')['Adj Close']
    change = round(100*df.pct_change(),2)

    btc_price = str(round(df.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
    btc_change = str(round(change.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
    eth_price = str(round(df.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')
    eth_change = str(round(change.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')

    daily_message = f"*__Crypto Markets {datetime.today().strftime('%d %b %Y')}:__* \n\n*Bitcoin:* ${btc_price}"

    if change.iloc[-1, 0] > 0:
        daily_message += f"\nUp from yesterday by: {btc_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {btc_change}%\n"

    daily_message += f"\n*Ethereum:* ${eth_price}"

    if change.iloc[-1, 1] > 0:
        daily_message += f"\nUp from yesterday by: {eth_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {eth_change}%\n"

    FGurl = 'https://api.alternative.me/fng/?limit=1&format=json'
    x = requests.get(FGurl)
    index = x.json()
    v = index['data'][0]['value']
    vc = index['data'][0]['value_classification']


    daily_message += f"\n*Fear and Greed Index:* {v} \({vc}\)\n"

    return daily_message

def stock_update(stock_tickers):
    lookback = dt.date.today() - dt.timedelta(days=5)
    df = yf.download(stock_tickers, lookback, interval='1d')['Adj Close']
    change = round(100*df.pct_change(),2)

    bnd_price = str(round(df.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
    vnq_price = str(round(df.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')
    voo_price = str(round(df.iloc[-1, 2],2)).replace('.', '\\.').replace('-', '\\-')
    vti_price = str(round(df.iloc[-1, 3],2)).replace('.', '\\.').replace('-', '\\-')
    vwo_price = str(round(df.iloc[-1, 4],2)).replace('.', '\\.').replace('-', '\\-')
    zar_price = str(round(df.iloc[-1, 5],2)).replace('.', '\\.').replace('-', '\\-')

    bnd_change = str(round(change.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
    vnq_change = str(round(change.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')
    voo_change = str(round(change.iloc[-1, 2],2)).replace('.', '\\.').replace('-', '\\-')
    vti_change = str(round(change.iloc[-1, 3],2)).replace('.', '\\.').replace('-', '\\-')
    vwo_change = str(round(change.iloc[-1, 4],2)).replace('.', '\\.').replace('-', '\\-')
    zar_change = str(round(change.iloc[-1, 5],2)).replace('.', '\\.').replace('-', '\\-')

    daily_message = f"*__Global Markets {datetime.today().strftime('%d %b %Y')}:__* \n\n*ZAR/USD:* ${zar_price}"

    if change.iloc[-1, 5] > 0:
        daily_message += f"\nUp from yesterday by: {zar_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {zar_change}%\n"


    daily_message += f"\n*Top 500 \(VOO\):* ${voo_price}"

    if change.iloc[-1, 2] > 0:
        daily_message += f"\nUp from yesterday by: {voo_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {voo_change}%\n"

    
    
    daily_message += f"\n*Total Market \(VTI\):* ${vti_price}"

    if change.iloc[-1, 3] > 0:
        daily_message += f"\nUp from yesterday by: {vti_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {vti_change}%\n"


    daily_message += f"\n*Real Estate Market \(VNQ\):* ${vnq_price}"

    if change.iloc[-1, 3] > 0:
        daily_message += f"\nUp from yesterday by: {vnq_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {vnq_change}%\n"


    daily_message += f"\n*Emerging Markets \(VWO\):* ${vwo_price}"

    if change.iloc[-1, 1] > 0:
        daily_message += f"\nUp from yesterday by: {vwo_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {vwo_change}%\n"


    daily_message += f"\n*Bond Market \(BND\):* ${bnd_price}"

    if change.iloc[-1, 0] > 0:
        daily_message += f"\nUp from yesterday by: {bnd_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {bnd_change}%\n"

    FGurl = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"

    x = requests.get( FGurl, headers=keys)
    index = x.json()
    v = index['fgi']['now']['value']
    vc = index['fgi']['now']['valueText']

    daily_message += f"\n*Fear and Greed Index:* {v} \({vc}\)\n"

    return daily_message

