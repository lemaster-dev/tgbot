from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer('Привіт! Я ваш вірний помічник в Телеграмі. За допомогою мене ви можете зробити заказ новорічних іграшок! Інструкція проста, вписуйте /start, за допомогою відкритої кнопки вводіть дані і подальша інструкція буде дана! Приємного користування!🎅')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Надати інформацію', web_app=WebAppInfo(url='https://lemaster-dev.github.io/tgbot/')))
    await message.answer('Вітаю, натисніть на кнопку та надайте інформацію для заказу', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Ваші дані: Імʼя: {res ["name"]}. Email: {res["email"]}. Телефон: {res["phone"]}.Тепер введіть команду "/pay" для оплати')


@dp.message_handler(commands=['pay'])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Ваш заказ', 'Новорічні іграшки', 'invoice', config.PAYMENT_TOKEN, 'USD', [types.LabeledPrice('Заказ', 1 * 100)])


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer(f'Успішно: {message.successful_payment.order_info}')


executor.start_polling(dp)
