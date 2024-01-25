import time

from aiogram import F, Router
from aiogram.types import CallbackQuery
from asgiref.sync import sync_to_async

from telebot.handlers.game_settings import give_game
from telebot.handlers.user_handlers import db_save
from telebot.keyboards.keyboards import create_game_keyboard, create_game_process_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU
from telebot.models import Game


router = Router()

# Эт X срабатывает на нажатие инлайн-кнопки "Поехали" и запускает игру
@router.callback_query(F.data == 'start_game')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    massiv = await give_massiv(game)
    # Тут массив нужно перемешать.
    for i in range(len(massiv)):
        await callback.message.edit_text(text=f'Поздравляю игра началась!!!\n{massiv[i]}')
        time.sleep(5)
        await callback.message.edit_text(text=f'Передайте телефон следующему игроку.')
        time.sleep(5)
    await callback.message.edit_text(text=f'Все роли получены можете начинать обсуждение.')
    await callback.answer()


@sync_to_async
def give_massiv(game):
    massiv = []
    for i in range(1, game.peace+1):
        massiv.append(f'Ваше слово «{game.word.word1.upper()}».')
    for i in range(game.peace+1, game.peace + game.spy+1):
        massiv.append(f'У Вас нет слова, вы Шпион')
    for i in range(game.peace + game.spy+1, game.peace + game.spy + game.undercover+1):
        massiv.append(f'Ваше слово «{game.word.word2.upper()}».')
    return massiv