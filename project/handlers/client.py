from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from creat_bot import dp, bot
from keyboards import kb_client, kb_topics, kb_kinds, kb_amount
from handlers.create_task import create_task_file


class FSMtask(StatesGroup):
    topic = State()
    kind = State()
    amount = State()


@dp.message_handler(commands=['Составить_файл'], state=None)
async def cm_start(message: types.Message):
    await FSMtask.topic.set()
    await message.answer('Выберете тему задания', reply_markup=kb_topics)


@dp.message_handler(state="*", commands=['отмена'])
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancle_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK', reply_markup=kb_client)


@dp.message_handler(state=FSMtask.topic)
async def load_topic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['topic'] = message.text
    await FSMtask.next()
    await message.answer('Теперь выберите вид задания', reply_markup=kb_kinds)


@dp.message_handler(state=FSMtask.kind)
async def load_kind(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['kind'] = message.text
    await FSMtask.next()
    await message.answer('И наконец количество заданий в файле', reply_markup=kb_amount)


@dp.message_handler(state=FSMtask.amount)
async def load_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
    try:
        async with state.proxy() as data:
            create_task_file(data)
        await message.answer('Вот ваш файл', reply_markup=kb_client)
        await bot.send_document(message.from_user.id, open('task_file.txt'))
    except:
        await message.answer('Некорректные данные были введены', reply_markup=kb_client)
    await state.finish()




@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.text == '/help':
        await message.answer('Если вы поняли, что вам не нужен файл, пока вы его создавали - нажмите /отмена.', reply_markup=kb_client)
    else:
        await message.answer('Все готово к работе', reply_markup=kb_client)
    # await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'], )
    dp.register_message_handler(cm_start, commands=['Составить_файл'], state=None)
    dp.register_message_handler(cancle_handler, state="*", commands=['отмена'])
    dp.register_message_handler(cancle_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_topic, state=FSMtask.topic)
    dp.register_message_handler(load_kind, state=FSMtask.kind)
    dp.register_message_handler(load_amount, state=FSMtask.amount)
