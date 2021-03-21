from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):

    update.message.reply_text(
        text='Welcome to the Cypherlogix Trading Bot!',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Continue >>', callback_data='skip')],
            [InlineKeyboardButton(text='ℹ️ About Cypherlogix', url='https://www.google.com')]
        ])
    )

if __name__ == '__main__':

    updater = Updater(token='1727276725:AAGPdcPX2uGcw8EKWC9PfEGhlb-o8Sq2zkY', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
