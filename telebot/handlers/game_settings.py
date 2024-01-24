from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery
from asgiref.sync import sync_to_async

from telebot.keyboards.keyboards import create_menu_keyboard, create_back_keyboard, create_game_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU
from telebot.models import Game, User, Word
import sqlite3

router = Router()


# Эт X срабатывает на нажатие инлайн-кнопки "-" уменьшает число мирных жителей
@router.callback_query(F.data == 'peaсe-1')
async def process_about_me(callback: CallbackQuery):
    print(callback)
    # game = Game(
    #     peace=1,
    #     spy=1,
    #     undercover=1,
    #     user_id=User.objects.filter(name=callback.from_user.username),
    #     word_id=give_words
    # )
    # await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()
