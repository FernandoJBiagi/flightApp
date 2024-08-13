import asyncio
from telegram import Bot

bot_token = "7053501697:AAFJoTqQ7lq2sXp4ikzfuDAwTxUcy9DIqhg"
chat_id = "-4237083945"

async def send_message():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text="Teste de mensagem via Telegram!")

asyncio.run(send_message())
