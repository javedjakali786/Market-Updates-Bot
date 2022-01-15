from functions import *

def main():
    message = stock_update(stock_tickers)
    for i in stock_send_list: 
        telegram_bot_sendtext(message, i)

if __name__ == '__main__':
    main()
