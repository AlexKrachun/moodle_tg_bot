from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token='6263683643:AAGdvFkayZrYREiZagK2BQAcnZQyjUPgcYw')
dp = Dispatcher(bot, storage=storage)
