from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
import logging
import tokens

import link
import roll
import alignment_chart


logging.basicConfig(
	filename='bot.log', filemode='w', level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

updater = Updater(tokens.telegram_token)


def roll_wrapper(update: Update, context: CallbackContext):
	try:
		logging.info(f'Roll from {update.message.from_user}')
		update.message.reply_text(str(roll.roll(message=update.message.text.split(' ', 1)[1])))
	except Exception as e:
		update.message.reply_text(str(e))
		logging.exception(e)


def alignment_chart_wrapper(update: Update, context: CallbackContext):
	try:
		logging.info(f'Alignment Chart from {update.message.from_user}')
		update.message.reply_photo(alignment_chart.alignment_chart(update.message.text.split(' ', 1)[1]))
	except Exception as e:
		update.message.reply_text(str(e))
		logging.exception(e)


def link_wrapper(update: Update, context: CallbackContext):
	try:
		logging.info(f'Link from {update.message.from_user}')
		update.message.reply_markdown(link.link(message=update.message.text.split(' ', 1)[1]))
	except Exception as e:
		update.message.reply_text(str(e))
		logging.exception(e)


updater.dispatcher.add_handler(CommandHandler('roll', roll_wrapper))
updater.dispatcher.add_handler(CommandHandler('alignment_chart', alignment_chart_wrapper))
updater.dispatcher.add_handler(CommandHandler('link', link_wrapper))

updater.start_polling()
