from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON

def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    """
    Функция `create_pagination_keyboard` генерирует встроенную клавиатуру с кнопками для пагинации.

:param: Функция `create_pagination_keyboard` принимает переменное количество надписей кнопок в качестве
аргументов и создаёт разметку встроенной клавиатуры для пагинации. Каждая подпись кнопки преобразуется в
объект `InlineKeyboardButton` с соответствующими данными обратного вызова.
:type: str
:return: Возвращается объект InlineKeyboardMarkup.
    """
    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(
        *[
            InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            )
            for button in buttons
        ]
    )
    return kb_builder.as_markup()