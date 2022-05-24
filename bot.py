import Constants as keys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import responses as R

print("Bot started...")

with open("keys.txt", "r") as f:
    TOKEN = f.read()


def start(update, context):
    update.message.reply_text("Hello there! Welcome to Amestarter bot")

def help(update, context):
    update.message.reply_text("Help yourself to a few commands if you're an Admin")

def contact(update, context):
    update.message.reply_text("Reach out to the Admins on Telegram or send us an email at business@amestarter.com")

def handle_message(update, context):
    text = str(update.message.text).lower()
    our_response = R.responses(text)

    update.message.reply_text(our_response)


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(CommandHandler("contact", contact))
    disp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()