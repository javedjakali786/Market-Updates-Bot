from configs import *
import requests
import yfinance as yf
import datetime as dt
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image


def telegram_bot_sendtext(bot_message, chat_id, path):
    files = {'photo':open(path,'rb')}
    send_text = 'https://api.telegram.org/bot' + telegram_api_key + '/sendPhoto?chat_id=' + chat_id  + '&parse_mode=MarkdownV2&caption=' + bot_message
    response = requests.post(send_text, files=files)
    return response.json()

'''not in use'''
def crypto_update(crypto_tickers):
    lookback = dt.date.today() - dt.timedelta(days=5)
    df = yf.download(crypto_tickers, lookback, interval='1d')['Open']
    change = round(100*df.pct_change(),2)

    btc_price = str(round(df.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
    btc_change = str(round(change.iloc[-1, 0],2)).replace('.', '\\.').replace('-', '\\-')
    eth_price = str(round(df.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')
    eth_change = str(round(change.iloc[-1, 1],2)).replace('.', '\\.').replace('-', '\\-')

    daily_message = f"*__Crypto Markets {datetime.today().strftime('%d %b %Y')}:__* \n\n*Bitcoin Open:* ${btc_price}"

    if change.iloc[-1, 0] > 0:
        daily_message += f"\nUp by: {btc_change}%\n"
    else:
        daily_message += f"\nDown by: {btc_change}%\n"

    daily_message += f"\n*Ethereum Open:* ${eth_price}"

    if change.iloc[-1, 1] > 0:
        daily_message += f"\nUp by: {eth_change}%\n"
    else:
        daily_message += f"\nDown by: {eth_change}%\n"


    response = requests.get("https://alternative.me/crypto/fear-and-greed-index.png")

    file = open("Fg.png", "wb")
    file.write(response.content)
    file.close()

    return daily_message


'''not in use'''
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

    daily_message = f"*__Global Markets {datetime.today().strftime('%d %b %Y')}:__* \n\n*ZAR/USD:* R{zar_price}"

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

    if change.iloc[-1, 1] > 0:
        daily_message += f"\nUp from yesterday by: {vnq_change}%\n"
    else:
        daily_message += f"\nDown from yesterday by: {vnq_change}%\n"


    daily_message += f"\n*Emerging Markets \(VWO\):* ${vwo_price}"

    if change.iloc[-1, 4] > 0:
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


def grab_images():

    #fear and greed
    response = requests.get("https://alternative.me/crypto/fear-and-greed-index.png")
    file = open("fear_greed.png", "wb")
    file.write(response.content)
    file.close()

    #heat map
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(800, 740)
    path = "file:///Users/connormcdonald/Desktop/GitHub/News-bot/heat_map.html"
    driver.get(path)
    driver.save_screenshot("heat_map.png")

    return None

def send_image (chat_id, path):
    files = {'photo':open(path,'rb')}
    send_text = 'https://api.telegram.org/bot' + telegram_api_key + '/sendPhoto?chat_id=' + chat_id
    response = requests.post(send_text, files=files)
    return response.json()