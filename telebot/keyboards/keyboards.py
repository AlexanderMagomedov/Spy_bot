from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.lexicon.lexicon_ru import LEXICON_COMMANDS, LEXICON_RU


# Функция создания инлайн кнопок главного меню
def create_menu_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON_COMMANDS['/game'], callback_data='/game'),
        InlineKeyboardButton(text=LEXICON_COMMANDS['/rules'], callback_data='/rules'),
        InlineKeyboardButton(text=LEXICON_COMMANDS['/about_me'], callback_data='/about_me'), width=1
    )
    return kb_builder.as_markup()


# Функция создания инлайн кнопки "Назад"
def create_back_keyboard(arg) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['/back'],
        callback_data=arg))
    return kb_builder.as_markup()


# Функция создания инлайн кнопок главного меню
def create_game_keyboard(game) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(
        InlineKeyboardButton(text='Left', callback_data='pease_left'),
        InlineKeyboardButton(text=f'Мирные жители {game.peace}', callback_data=''),
        InlineKeyboardButton(text='Right', callback_data='pease_right'), width=3
    )
    return kb_builder.as_markup()