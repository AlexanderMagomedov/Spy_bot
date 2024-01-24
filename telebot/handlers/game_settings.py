from aiogram import F, Router
from aiogram.types import CallbackQuery
from asgiref.sync import sync_to_async
from telebot.handlers.user_handlers import db_save
from telebot.keyboards.keyboards import create_game_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU
from telebot.models import Game


router = Router()


@sync_to_async
def give_game(callback):
    return Game.objects.get(telegram=callback.from_user.id)


# Эт X срабатывает на нажатие инлайн-кнопки "-" уменьшает число мирных жителей
@router.callback_query(F.data == 'peaсe-1')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    if game.peace > 0:
        game.peace -= 1
        await db_save(game)
        await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "+" увеличивать число мирных жителей
@router.callback_query(F.data == 'peaсe+1')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    if game.peace < 10:
        game.peace += 1
        await db_save(game)
        await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "-" уменьшает число шпионов
@router.callback_query(F.data == 'spy-1')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    if game.spy > 0:
        game.spy -= 1
        await db_save(game)
        await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "+" увеличивать число шпионов
@router.callback_query(F.data == 'spy+1')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    if game.spy < 5:
        game.spy += 1
        await db_save(game)
        await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "-" уменьшает число забывчивых шпионов
@router.callback_query(F.data == 'undercover-1')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    if game.undercover > 0:
        game.undercover -= 1
        await db_save(game)
        await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()


# Эт X срабатывает на нажатие инлайн-кнопки "+" увеличивать число забывчивых шпионов
@router.callback_query(F.data == 'undercover+1')
async def process_about_me(callback: CallbackQuery):
    game = await give_game(callback)
    if game.undercover < 5:
        game.undercover += 1
        await db_save(game)
        await callback.message.edit_text(text=LEXICON_RU['/game'], reply_markup=create_game_keyboard(game))
    await callback.answer()

# Эт X срабатывает на нажатие инлайн-кнопки "None" и ничего не делать
@router.callback_query(F.data == 'None')
async def process_about_me(callback: CallbackQuery):
    await callback.answer()
