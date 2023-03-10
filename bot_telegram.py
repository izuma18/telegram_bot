import os
import config

from aiogram import Dispatcher, Bot
from aiogram.utils import executor
from data_base import sqlite_db

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    sqlite_db.sql_start()
    await bot.set_webhook(config.URL_APP)


async def on_shutdown(dp):
    await bot.delete_webhook()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

#executor.start_polling(dp, skip_updates=True)
executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    skip_updates=True,
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000)))
