from aiogram import F, Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery
from asgiref.sync import sync_to_async
from telebot.keyboards.keyboards import create_menu_keyboard, create_back_keyboard, create_game_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU
from telebot.models import Game, User, Word
import sqlite3

router = Router()


# Эт X срабатывает на команду "/start" отправлять приветственное сообщение показывая кнопки главного меню
@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    if str(message.from_user.id) not in give_all_telegram_id():
        user = User(
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            telegram_id=message.from_user.id)
        await db_save(user)
    await message.answer(LEXICON_RU[message.text], reply_markup=create_menu_keyboard())
    await message.delete()


@sync_to_async
def db_save(arg):
    arg.save()


# Функция возвращает полный список всех телеграм ид сотрудников
def give_all_telegram_id():
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    user_list_all = (list(map(lambda x: x[0], cursor.execute("SELECT telegram_id FROM telebot_user").fetchall())))
    connect.close()
    return user_list_all


# Эт X срабатывает на нажатие инлайн-кнопки "Назад" и возвращать в главное меню
@router.callback_query(F.data == '/start')
async def process_start(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=create_menu_keyboard())
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "Обо мне" в главном меню показывает сообщение и кнопку "назад"
@router.callback_query(F.data == '/about_me')
async def process_about_me(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/about_me'], reply_markup=create_back_keyboard('/start'))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "Правила игры" в главном меню показывает правила и кнопку "назад"
@router.callback_query(F.data == '/rules')
async def process_about_me(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/rules'], reply_markup=create_back_keyboard('/start'))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "Начало игры" в главном меню показывает клавиатуру настроек игры
@router.callback_query(F.data == '/game')
async def process_about_me(callback: CallbackQuery):
    game = Game(
        peace=1,
        spy=1,
        undercover=1,
        telegram=callback.from_user.id,
        word_id=await give_words(),
        rez=''
    )
    await db_save(game)
    await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()


@sync_to_async
def give_words():
    return str(Word.objects.order_by("?").first().id)
