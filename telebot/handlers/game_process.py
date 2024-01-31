import time
import random

from aiogram import F, Router
from aiogram.types import CallbackQuery
from asgiref.sync import sync_to_async

from telebot.filters.filters import IsGamer
from telebot.handlers.game_settings import give_game
from telebot.handlers.user_handlers import give_words, db_save
from telebot.keyboards.keyboards import create_finish_keyboard, create_game_keyboard, create_double_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU


router = Router()


# Эт X срабатывает на нажатие инлайн-кнопки "Поехали" и запускает игру
@router.callback_query(F.data == 'start_game')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    massiv = await give_massiv(game)
    random.shuffle(massiv)
    text_all = '_'.join(str(i[0]) for i in massiv)
    text_after = '_'.join(f'Игрок № {i+1}' for i in range(len(massiv)))
    for i in range(len(massiv)):
        await callback.message.edit_text(text=f'Поздравляю игра началась!!!\n'
                                              f'Вы Игрок № {i+1} 😉\n{massiv[i][1]}')
        time.sleep(5)
        if i != len(massiv)-1:
            await callback.message.edit_text(text=f'Передайте телефон следующему игроку. 📱 ➡ 🦾')
            time.sleep(5)
    game.rez = text_all
    game.after = text_after
    await db_save(game)
    await callback.message.edit_text(
        text=f'🌟 Все роли распределены – наступило время великих приключений! '
             f'Начинайте обсуждение кто же из вас Шпион?!',
        reply_markup=create_finish_keyboard(text_after))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "Закончить игру" выводить слова и предлагать начать игру заново.
@router.callback_query(F.data == 'finish')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    word = await give_word1_word2(game)
    game_rez = str()
    game_list = [i for i in game.rez.split('_')]
    for i in range(len(game_list)):
        game_rez += f'Игрок №{i+1} - {game_list[i]}\n'

    await callback.message.edit_text(
        text=f'УРА!!!🔥🔥🔥 \nЗагаданное слово «{word[0].upper()}».\n'
             f'Слово Забывчивого шпиона «{word[1].upper()}».\n' 
             f'{game_rez}'
             f'Давайте сыграем еще раз тем же составом❓❗',
        reply_markup=create_double_keyboard('/game'))
    await callback.answer()


@sync_to_async
def give_word1_word2(game):
    return [game.word.word1, game.word.word2]


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


#Этот хендлер будер раскрывать роль игрока
@router.callback_query(IsGamer())
async def process_show_gamer_press(callback: CallbackQuery):
    game = await give_game(callback)
    game_list_rez = [i for i in game.rez.split('_')]
    game_list_after = [i for i in game.after.split('_')]
    game_list_after[int(callback.data.split()[2])-1] = game_list_rez[int(callback.data.split()[2])-1]
    text_after = '_'.join(i for i in game_list_after)
    game.after = text_after
    await db_save(game)
    await callback.message.edit_text(
        text=f'🌟 Все роли распределены – наступило время великих приключений! '
             f'Начинайте обсуждение кто же из вас Шпион?!\n'
             f'Вы решили избавиться от игрока № {callback.data.split()[2]} 💔 🔫',
        reply_markup=create_finish_keyboard(text_after))
    await callback.answer()
