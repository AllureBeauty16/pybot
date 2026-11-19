import os
import telebot
from dotenv import load_dotenv
from db import add_item, list_item

load_dotenv()
tg_token = os.environ.get("TG_TOKEN")

bot = telebot.TeleBot(tg_token)

@bot.message_handler(commands=["start"])
def start_handler(message) :
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        print(f"Bot started for: {username}")
        bot.reply_to(message, "Привет!")


@bot.message_handler(commands=["add"])
def add_item_handler(message):
    parts = message.text.split(" ", 1)

    if len(parts) > 1 and parts[1].strip():
        item = parts[1].strip()
        add_item(item)
        bot.reply_to(message, "Элемент добавлен")
    else:
        bot.reply_to(message, "Напиши: /add название")
@bot.message_handler(commands=["list"])
def list_item_handler(message):
    items = list_item()

    if items:
        result = "\n".join(f"{key}: {name}" for key, name in items)
        bot.reply_to(message, result)
    else:
        bot.reply_to(message, "Список пуст")
@bot.message_handler(
    func=lambda mes: True,
    content_types=["text"]
)
def echo(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

