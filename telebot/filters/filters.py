from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsGamer(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.split()[0] == 'Игрок'