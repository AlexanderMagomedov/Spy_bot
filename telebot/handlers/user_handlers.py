from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery
from telebot.keyboards.keyboards import create_menu_keyboard, create_back_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU


router = Router()


# Эт X срабатывает на команду "/start" отправлять приветственное сообщение показывая кнопки главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU[message.text], reply_markup=create_menu_keyboard())


# Эт X срабатывает на нажатие инлайн-кнопки "Назад" и возвращать в главное меню
@router.callback_query(F.data == '/start')
async def process_start(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=create_menu_keyboard())
    await callback.answer()


# Эт X срабатывает на команду "/about_me" отправляет сообщение о нас и кнопку "назад"
@router.message(Command(commands='about_me'))
async def process_about_me_command(message: Message):
    await message.answer(LEXICON_RU[message.text], reply_markup=create_back_keyboard('/start'))


# Эт X срабатывает на нажатие инлайн-кнопки "Обо мне" в главном меню показывает сообщение и кнопку "назад"
@router.callback_query(F.data == '/about_me')
async def process_about_me(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/about_me'], reply_markup=create_back_keyboard('/start'))
    await callback.answer()
