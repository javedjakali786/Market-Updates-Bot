from functions import *

def main():
    message = crypto_update(crypto_tickers)
    telegram_bot_sendtext(message, channel_id)
    # telegram_bot_sendtext(message, chat_id) uncomment to send to chats

if __name__ == '__main__':
    main()





