This script sends a daily update on various markets via telegram

Configs set up:
- rename the example_configs.py file to "configs.py"
- download telegram
- start a chat with BotFather (telegram bot creator)
- type "/newbot" and follow the prompts
- you will be given an API token, paste this token in the configs.py file and assign the variable name "telegram_api_key"
- start a chat with userinfobot on telegram
- type "\start", this will return your telegram account info, save the ID(s) in the configs.py file
- Assign the list of IDs to the variable name "crypto_send_list" and "stock_send_list"
- create an account at https://rapidapi.com/rpi4gx/api/fear-and-greed-index/  to get a valid API key for the stock fear and greed index
- Test the bot by running the crypto.py file for crypto updates and the stock.py file for stock updates

***IMPORTANT: You must first send your bot a message such as 'hello world' before trying to send yourself or others a message with your bot. If you do not do this you will get the following: {'description': 'Bad Request: chat not found', 'error_code': 400, 'ok': False}. This is a saftey feature created by telegram to prevent bots from sending out unsolicited messages***

Tickers: 
All ticker data is sourced from yahoo finance. The fear and greed indexes are accessed via https://rapidapi.com/rpi4gx/api/fear-and-greed-index/ (stocks) and https://alternative.me/crypto/fear-and-greed-index/ (crypto)

automation suggestions: 
Run crypto.py or stocks.py on a task scheduler of your choice (cronjob/windows task scheduler are highly recommended)
