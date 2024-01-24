from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.lexicon.lexicon_ru import LEXICON_COMMANDS


# Функция создания инлайн кнопок главного меню
def create_menu_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON_COMMANDS['game'], callback_data='game'),
        InlineKeyboardButton(text=LEXICON_COMMANDS['rules'], callback_data='rules'),
        InlineKeyboardButton(text=LEXICON_COMMANDS['about_me'], callback_data='about_me'), width=1
    )
    return kb_builder.as_markup()