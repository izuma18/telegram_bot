from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/Режим_работы')
b4 = KeyboardButton('/Расположение')
b5 = KeyboardButton('/Цены')
b6 = KeyboardButton('Поделиться номером', request_contact=True)
b7 = KeyboardButton('Отправить где я',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1, b2, b3, b4, b5, b6, b7)
