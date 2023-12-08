from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('6423433010:AAHauahUuDBeG7viGWE4vKGV-6nGRFI7WGM')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('otkrit webs', web_app=WebAppInfo(url='https://lemaster-dev.github.io/tgbot/')))
    await message.answer('privet', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res ["name"]}. Email: {res["email"]}. Phone: {res["phone"]}.')


executor.start_polling(dp)
