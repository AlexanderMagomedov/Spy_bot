from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from telebot.keyboards.keyboards import create_menu_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU


router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять ему приветственное сообщение показывать кнопки главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU[message.text], reply_markup=create_menu_keyboard())
