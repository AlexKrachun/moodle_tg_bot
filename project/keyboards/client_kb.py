from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def create_kb_client():
    b1 = KeyboardButton('/start')
    b2 = KeyboardButton('/help')
    b3 = KeyboardButton('/Составить_файл')
    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_client.row(b1, b2).row(b3)
    return kb_client


def create_kb_topics():
    b1 = KeyboardButton('/кубические')
    b2 = KeyboardButton('/показательные')
    b3 = KeyboardButton('/иррациональные')
    b4 = KeyboardButton('/логарифмические')
    b5 = KeyboardButton('/отмена')

    kb_topics = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_topics.row(b1, b2).row(b3, b4).row(b5)
    return kb_topics

def create_kb_kinds():
    b1 = KeyboardButton('/уравнения')
    b2 = KeyboardButton('/неравенства')
    b3 = KeyboardButton('/выражения')
    b4 = KeyboardButton('/отмена')
    kb_kinds = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_kinds.row(b1, b2).row(b3).row(b4)
    return kb_kinds

def create_kb_amount():
    b1 = KeyboardButton('/10')
    b2 = KeyboardButton('/100')
    b3 = KeyboardButton('/500')
    b4 = KeyboardButton('/1000')
    b5 = KeyboardButton('/отмена')

    kb_amount = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_amount.row(b1, b2).row(b3, b4).row(b5)
    return kb_amount
    

kb_client = create_kb_client()
kb_topics = create_kb_topics()
kb_kinds = create_kb_kinds()
kb_amount = create_kb_amount()
