This script sends a daily update on various markets via telegram

Configs set up:
- rename the example_configs.py file to "configs.py"
- download telegram
- start a chat with BotFather (telegram bot creator)
- type "/newbot" and follow the prompts
- you will be given an API token, paste this token in the configs.py file and assign the variable name "telegram_api_key"
- start a chat with userinfobot on telegram
- type "\start", this will return your telegram account info, save the ID in the configs.py file
- Assign the variable name "chat_id" to this ID
- Test the bot by running the script.py file

Tickers: 
Currently the bot only works for BTC, ETH, S&P500, and ZAR/USD.
The data comes from yahoo finance and thus, if you require any other tickers to be included in the messages you will need to check for 
its ticker symbol on yahoo finance

automation suggestions: 
for linux or mac users - cron job
for windows users -  windows task scheduler
