from telegram import Bot

def send_telegram_message(chat_id, message):
    bot_token = '7053501697:AAFJoTqQ7lq2sXp4ikzfuDAwTxUcy9DIqhg'  # Substitua pelo token do seu bot
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)
