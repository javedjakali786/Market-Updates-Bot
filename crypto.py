from functions import *

def main():
    message = crypto_update(crypto_tickers)
    for i in crypto_send_list: 
        telegram_bot_sendtext(message, i)

if __name__ == '__main__':
    main()





