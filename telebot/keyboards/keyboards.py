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


# Функция создания инлайн кнопок настройки игры
def create_game_keyboard(game) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(InlineKeyboardButton(text=f'Мирные жители {game.peace}', callback_data='None'))
    kb_builder.row(InlineKeyboardButton(text='➖', callback_data='peaсe-1'),
                   InlineKeyboardButton(text='➕', callback_data='peaсe+1'), width=2)
    kb_builder.row(InlineKeyboardButton(text=f'Шпион {game.spy}', callback_data='None'))
    kb_builder.row(InlineKeyboardButton(text='➖', callback_data='spy-1'),
                   InlineKeyboardButton(text='➕', callback_data='spy+1'), width=2)
    kb_builder.row(InlineKeyboardButton(text=f'Забывчивый шпион {game.undercover}', callback_data='None'))
    kb_builder.row(InlineKeyboardButton(text='➖', callback_data='undercover-1'),
                   InlineKeyboardButton(text='➕', callback_data='undercover+1'), width=2)
    kb_builder.row(InlineKeyboardButton(
        text=f'🏎️ Итого {game.peace+game.spy+game.undercover}. Поехали?! ',
        callback_data='start_game'))
    kb_builder.row(InlineKeyboardButton(text=LEXICON_RU['/back'], callback_data='/start'))
    return kb_builder.as_markup()


# Функция создания инлайн кнопки "Закончить игру"
def create_finish_keyboard(game) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['/finish'],
        callback_data=f'finish:{game.word.word1.upper()}:{game.word.word2.upper()}'))
    return kb_builder.as_markup()


# Функция создания инлайн кнопок "Новое слово" "Назад"
def create_double_keyboard(arg) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['/new_word'],
        callback_data='/new_word'))
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['/back'],
        callback_data=arg))
    return kb_builder.as_markup()
