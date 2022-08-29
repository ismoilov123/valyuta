
import config
import telebot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton 
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
import requests
from bs4 import BeautifulSoup


#EURO KURSI:
link = "https://pokur.su/eur/uzs/1/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
eur=soup.find("article").text

#DOLLAR KURSI:
link = "https://pokur.su/usd/uzs/1/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
usd=soup.find("article").text

#RUBL KURSI:
link = "https://pokur.su/rub/uzs/1/"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
rub=soup.find("article").text

x=eur[30:100]
y=eur[120:1000]

a=usd[38:100]
b=usd[130:1000]

c=rub[30:100]
d=rub[120:1000]


def message_handler(update: Update,context: CallbackContext):
	tugmalar = ReplyKeyboardMarkup(
		keyboard = [
		    [
		    KeyboardButton("Valyutalar"),
		    KeyboardButton("Biz haqimizda"),
		    ]
		],
		resize_keyboard=True
		)
	
	valyuta = ReplyKeyboardMarkup(
	    keyboard = [
		    [
		    KeyboardButton("EURO 🇪🇺"),
		    KeyboardButton("USD 🇺🇸"),
		    KeyboardButton("RUB 🇷🇺")
		    ],
		    [
		    KeyboardButton("Orqaga qaytish  🔙"),
		    ]
		],
		resize_keyboard=True
		)

	info1 = ReplyKeyboardMarkup(
		keyboard = [
		    [
		    KeyboardButton("🇪🇺 EURO to'liqroq ma'lumot olish"),
		    ],
		    [
		    KeyboardButton("Orqaga qaytish 🔙"),
		    ]
		],
		resize_keyboard=True
		)

	info2 = ReplyKeyboardMarkup(
		keyboard = [
		    [
		    KeyboardButton("🇺🇸 USD to'liqroq ma'lumot olish"),
		    ],
		    [
		    KeyboardButton("Orqaga qaytish 🔙"),
		    ]
		],
		resize_keyboard=True
		)

	info3 = ReplyKeyboardMarkup(
		keyboard = [
		    [
		    KeyboardButton("🇷🇺 RUBL to'liqroq ma'lumot olish"),
		    ],
		    [
		    KeyboardButton("Orqaga qaytish 🔙"),
		    ]
		],
		resize_keyboard=True
		)


	text = update.message.text
	ism=update.message.from_user.first_name
	if text == "/start":
		update.message.reply_text(
			text=f"Assalomu alaykum {ism} botimizga xush kelibsiz!  Pastdagi tugmalarni bosib ma'lumot olishingiz mumkin 😉",
			reply_markup=tugmalar
			)


	elif text == "Biz haqimizda":
		update.message.reply_text(
			text="Bot yaratuvchisi O'ral Ismoilov tel:  +998909165969",
			reply_markup=tugmalar
			)
	elif text == "Valyutalar":
		update.message.reply_text(
			text="Valyutani tanlang 👇",
			reply_markup=valyuta
			)

	elif text == "EURO 🇪🇺":
		update.message.reply_text(
			text=x,
			reply_markup=info1
			)

	elif text == "USD 🇺🇸":
		update.message.reply_text(
			text=a,
			reply_markup=info2
			)

	elif text == "RUB 🇷🇺":
		update.message.reply_text(
			text=c,
			reply_markup=info3
			)

#INFO:


	elif text == "🇪🇺 EURO to'liqroq ma'lumot olish":
		update.message.reply_text(
			text=x+y,
			reply_markup=valyuta
			)

	elif text == "🇺🇸 USD to'liqroq ma'lumot olish":
		update.message.reply_text(
			text=a+b,
			reply_markup=valyuta
			)

	elif text == "🇷🇺 RUBL to'liqroq ma'lumot olish":
		update.message.reply_text(
			text=c+d,
			reply_markup=valyuta
			)

	elif text == "Orqaga qaytish  🔙":
		update.message.reply_text(
			text="🔙",
			reply_markup=tugmalar
			)

	elif text == "Orqaga qaytish 🔙":
		update.message.reply_text(
			text="🔙",
			reply_markup=valyuta
			)


	else:
		update.message.reply_text(
			text="siz bergan komanda menda yo'q\npastdagi tugmalardan birini tanlang 👇",
			reply_markup=tugmalar
			)

def main():
	print('Start')
	updater = Updater(
		token = config.TOKEN,
		use_context=True,
		)
	updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler)) 
	updater.start_polling()
	updater.idle()


if __name__=='__main__':
	main()