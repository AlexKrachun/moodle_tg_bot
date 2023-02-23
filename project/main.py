'''
Функцонал
    По запросу отправлять файл из n заданий(по кнопке) из указанного раздела(по кнопке) и указанного вида(по кнопке)

'''

from aiogram.utils import executor
from creat_bot import dp
from handlers import client, admin,  other

async def on_startup(_):
    print('Бот вышел в онлайн - и слава богу')



client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)