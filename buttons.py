from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




start = {
    "So'm" : "UZS",
    'Tenge':'KZT',
    'Angliya puli':'GBP',
    'Xitoy':'CNY',
    'Arab':'AED',
}

async def gen_start():
    btn = InlineKeyboardMarkup(row_width=3)
    for key, value in start.items():
        btn.insert(InlineKeyboardButton(text=key, callback_data=value))
    return btn