import config
from aiogram import Dispatcher, Bot
from aiogram.utils import executor
from data_base import sqlite_db

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    sqlite_db.sql_start()


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True)
