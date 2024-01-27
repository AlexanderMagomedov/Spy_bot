from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsFinish(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.split(":")[0] == 'finish'