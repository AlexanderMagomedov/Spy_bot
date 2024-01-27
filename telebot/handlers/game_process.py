import time
import random

from aiogram import F, Router
from aiogram.types import CallbackQuery
from asgiref.sync import sync_to_async

from telebot.filters.filters import IsFinish
from telebot.handlers.game_settings import give_game
from telebot.handlers.user_handlers import give_words, db_save
from telebot.keyboards.keyboards import create_back_keyboard, create_finish_keyboard, create_game_keyboard, \
    create_double_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU
from telebot.models import Game

router = Router()


# Эт X срабатывает на нажатие инлайн-кнопки "Поехали" и запускает игру
@router.callback_query(F.data == 'start_game')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    massiv = await give_massiv(game)
    random.shuffle(massiv)
    text_all = str()
    for i in range(len(massiv)):
        text_all = text_all + f'Игрок №{i+1} - {massiv[i][0]} \n'
        await callback.message.edit_text(text=f'Поздравляю игра началась!!!\n'
                                              f'Вы Игрок № {i+1} 😉\n{massiv[i][1]}')
        time.sleep(5)
        if i != len(massiv)-1:
            await callback.message.edit_text(text=f'Передайте телефон следующему игроку. 📱 ➡ 🦾')
            time.sleep(5)
    game.rez = text_all
    await db_save(game)
    await callback.message.edit_text(
        text=f'🌟 Все роли распределены – наступило время великих приключений! '
             f'Начинайте обсуждение кто же из вас Шпион?!',
        reply_markup=create_finish_keyboard(game))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "Закончить игру" выводить слова и предлагать начать игру заново.
@router.callback_query(IsFinish())
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    await callback.message.edit_text(
        text=f'УРА!!!🔥🔥🔥 \nЗагаданное слово «{callback.data.split(":")[1]}».\n'
             f'Слово Забывчивого шпиона «{callback.data.split(":")[2]}».\n'
             f'{game.rez}'
             f'Давайте сыграем еще раз тем же составом❓❗',
        reply_markup=create_double_keyboard('/game'))
    await callback.answer()


@sync_to_async
def give_massiv(game):
    massiv = []
    for i in range(1, game.peace+1):
        massiv.append(['Мирный житель', f'Ваше слово «{game.word.word1.upper()}».'])
    for i in range(game.peace+1, game.peace + game.spy+1):
        massiv.append(['Шпион', f'У Вас нет слова, вы Шпион. 🕵️'])
    for i in range(game.peace + game.spy+1, game.peace + game.spy + game.undercover+1):
        massiv.append(['Забывчивый шпион', f'Ваше слово «{game.word.word2.upper()}».'])
    return massiv


# Эт X срабатывает на нажатие инлайн-кнопки "Новое слово" меняет слово для той же игры
@router.callback_query(F.data == '/new_word')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    game.word_id = await give_words()
    await db_save(game)
    await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()
