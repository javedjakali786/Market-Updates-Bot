from functions import *

def main():
    daily_message = build_text(tickers)
    for i in send_list: 
        telegram_bot_sendtext(daily_message, i)

if __name__ == '__main__':
    main()





