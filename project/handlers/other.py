from aiogram import types, Dispatcher
from time import sleep
import string, json


from creat_bot import bot, dp



@dp.message_handler()
async def echo_send(message: types.Message):
    # Обработка мата в бcеде
    mat = {slovo.lower().translate(str.maketrans('', '', string.punctuation))\
        for slovo in message.text.split()} & set(json.load(open('cenz.json')))
    if mat:
        await message.answer('Ругательства приветствуются')
        for i in mat:
            for _ in range(10):
                await message.answer(i)
                sleep(0.5)
        await message.answer('.')
    else:
        await message.answer('Не знаю таких команд\n' + message.text)
        # await message.reply(message.text)
        # await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)

