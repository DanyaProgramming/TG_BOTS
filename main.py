from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode

TOKEN = '7772231526:AAEV4JrEcBzmJ4Fuw81lUGV9RUvyJTShx00'  # ❗️ЗАМЕНИТЕ ТОКЕН ПОСЛЕ ПУБЛИКАЦИИ❗️
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Сдача вц"), KeyboardButton(text="Паки девушек")],
        [KeyboardButton(text="Обучение скама"), KeyboardButton(text="Реквизиты")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = """
    🌟 *Добро пожаловать в Nevna Tim!* 🌟
    
    Выберите категорию того, что вам нужно:
    """
    await message.reply(
        text=welcome_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard
    )

# Обработчики кнопок
@dp.message(F.text == "Сдача вц")
async def fruits_info(message: types.Message):
    text = """**@nevnarkotikax** НЕ СПАМИТЬ"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Паки девушек")
async def transport_info(message: types.Message):
    text = """[Пак1](https://t.me/+2ZF2Fgoa-MQ5OGQ6)
[Пак2](https://t.me/+ZipAG9ZnpmI1MGIy)
[Пак3](https://t.me/+H4mbXUlkIDI3NDgy)
[Пак4](https://t.me/+n5I0aiQ6HKY1MjYy)
[Пак5](https://t.me/+n5I0aiQ6HKY1MjYy)
[Пак5](https://t.me/+ipAgHmA34Xs5M2Zi)
[Жесты](https://t.me/+S1Oanqp5T5Q0OWYy)"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Обучение скама")
async def sports_info(message: types.Message):
    text = """*https://t.me/hehejdndnej*"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Реквизиты")
async def music_info(message: types.Message):
    text = """*2200701990347772*
Карта дроп, для проверки @nevnarkotikax"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    dp.run_polling(bot)
