from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random
import matplotlib.pyplot as plt
import io
import ast
from bs4 import BeautifulSoup
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import link
import tokens

logging.basicConfig(
	filename='bot.log', filemode='w', level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

updater = Updater(tokens.telegram_token)


def roll(update: Update, context: CallbackContext):
	try:
		logging.info(f'Roll from {update.message.from_user}')
		message = update.message.text.split(' ', 1)[1].replace(' ', '')
		queries = message.split('+')
		result = 0
		for query in queries:
			parts = query.split('d')
			if len(parts) == 1:
				result += int(parts[0])
			if len(parts) == 2:
				if parts[0] == '':
					num = 1
					dice = int(parts[1])
				else:
					num, dice = int(parts[0]), int(parts[1])
				for _ in range(num):
					result += random.randint(1, dice)

		update.message.reply_text(str(result))
	except Exception as e:
		update.message.reply_text(str(e))
		logging.exception(e)


def alignment_chart(update: Update, context: CallbackContext):
	try:
		logging.info(f'Alignment Chart from {update.message.from_user}')
		chars = ast.literal_eval(update.message.text.split(' ', 1)[1])
		for char in chars:
			plt.scatter(*char[:2], label=char[2])
		plt.xlim(-1.5, 1.5)
		plt.ylim(-1.5, 1.5)
		plt.hlines([-0.5, 0.5], [-1.5, -1.5], [1.5, 1.5])
		plt.vlines([-0.5, 0.5], [-1.5, -1.5], [1.5, 1.5])
		plt.xticks([-1, 0, 1], ['Lawful', 'Neutral', 'Chaotic'])
		plt.yticks([-1, 0, 1], ['Evil', 'Neutral', 'Good'])
		plt.legend()

		with io.BytesIO() as b:
			plt.savefig(b, format='png')
			plt.close()
			b.seek(0)
			update.message.reply_photo(b.read())
	except Exception as e:
		update.message.reply_text(str(e))
		logging.exception(e)


def link_wrapper(update: Update, context: CallbackContext):
	try:
		update.message.reply_markdown(link.link(query=update.message.text.split(' ', 1)[1]))
	except Exception as e:
		update.message.reply_text(str(e))
		logging.exception(e)


updater.dispatcher.add_handler(CommandHandler('roll', roll))
updater.dispatcher.add_handler(CommandHandler('alignment_chart', alignment_chart))
updater.dispatcher.add_handler(CommandHandler('link', link_wrapper))

updater.start_polling()
