from aiogram import types, Dispatcher
from bot_telegram import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '...', reply_markup=kb_client)
        await message.delete()
    except:
        #test
        #await message.reply('Необходимо написать боту:\nhttps://t.me/Baltuszka_legnica_test_bot')

        #main
        await message.reply('Необходимо написать боту:\nhttps://t.me/Baltuszka_legnica_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def skola_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пишите в любое время')


# @dp.message_handler(commands=['Расположение'])
async def skola_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Wjazdowa 3/1A, 59-200 Legnica')


# @dp.message_handler(commands=['Цены'])
async def skola_price_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(skola_open_command, commands=['Режим_работы'])
    dp.register_message_handler(skola_place_command, commands=['Расположение'])
    dp.register_message_handler(skola_price_command, commands=['Цены'])
