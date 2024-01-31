import logging
from aiogram import Bot, Dispatcher, executor, types
from config import *
from api import *
from buttons import *


bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot)



logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Assalom alaykum valyuta tanlang", reply_markup = await gen_start())



@dp.callback_query_handler(lambda call: call.data != None)
async def send(call: types.CallbackQuery):

    text = f"USD uchun {call.data} almashtirish {exchange(call.data)} "
    
    await call.message.answer(text)
    



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)