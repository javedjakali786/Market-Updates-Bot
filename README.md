This script sends a daily update on various markets via telegram

Configs set up:
- Rename the example_configs.py file to "configs.py"
- Download Telegram and start a chat with @BotFather, send "/newbot" and follow the prompts to create your own bot
- Save the API token as telegram_api_key in the configs.py file
- To get chat_id, start a chat with @userinfobot and send it "/start" then save the ID as chat_id in the configs.py file
- To get channel_id, create a **public** channel on Telegram and assign the channel name to the channel_id variable in the configs.py file
- Add your bot to the Telegram channel and make it an admin
- To get the stock fear and greed index, create an account at https://rapidapi.com/rpi4gx/api/fear-and-greed-index/  to get a valid API key
- put this API key in the keys dictionary assigned to x-rapidapi-key in the configs.py file 
- Test the bot by running the crypto.py file for crypto updates and the stock.py file for stock updates
- If you are sending to specific chats, you should uncomment the commented lines in the crypto.py and stocks.py files and comment out the lines above them

***IMPORTANT: when sending messages directly to users (using chat_id instead of channel_id) the person recieving the message from the bot must first send the bot a message such as 'hello world' to grant permission for the bot to send messages. If you do not do this you will get the following: {'description': 'Bad Request: chat not found', 'error_code': 400, 'ok': False}. This is a saftey feature created by telegram to prevent bots from sending out unsolicited messages***

Tickers: 
All ticker data is sourced from yahoo finance. The fear and greed indexes are accessed via https://rapidapi.com/rpi4gx/api/fear-and-greed-index/ (stocks) and https://alternative.me/crypto/fear-and-greed-index/ (crypto)

automation suggestions: 
Run crypto.py or stocks.py on a task scheduler of your choice (cronjob/windows task scheduler are highly recommended)
