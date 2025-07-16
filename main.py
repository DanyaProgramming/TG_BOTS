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
    text = """
    Навигация по каналу

📁Общие вопросы:

  • Словарь воркера [ОБЯЗАТЕЛЬНО к прочтению перед ознакомлением] (https://t.me/c/2224786128/31)
  • Что нужно для начала работы? (https://t.me/c/2224786128/3)
  • В чём отличие виртуального и физического номера? (https://t.me/c/2224786128/4)
  • Как прогреть номер перед началом работы? (https://t.me/c/2224786128/5)
  • Где искать трафик для работы? (https://t.me/c/2224786128/6)
  • Где взять женские голосовые сообщения? (https://t.me/c/2224786128/7)
 (https://t.me/+P0pduxzX2HwyOThi)  • Где взять материалы(фото/видео) для работы? (https://t.me/c/2224786128/8)
  • Куда мамонт должен кидать деньги? (https://t.me/c/2224786128/9)
  • Где взять бесплатный прокси? (https://t.me/c/2224786128/10)
 
📁 [Нарко/Эскорт/ФБ] Вопросы по ворку:

  • Как завести мамонта в бота? (https://t.me/c/2224786128/11)
  • (https://t.me/c/2224786128/13) Где взять реферальную ссылку? (https://t.me/c/2224786128/13)
  • Как скрыть реферальную ссылку? (https://t.me/c/2224786128/15)
  • Как изменить город в боте эскорт? (https://t.me/c/2224786128/16)
  • Что делать после первого депа? (https://t.me/c/2224786128/18)
  • Как завести мамонта в ТП и что такое иксы? (https://t.me/c/2224786128/19)
  • Что будет если мамонт выберет другую модель в боте эскорта? (https://t.me/c/2224786128/20)
  • Что такое история заказов в нарко боте и как её создать? (https://t.me/c/2224786128/21)
  • Как создать свою анкету в эскорт боте? (https://t.me/c/2224786128/22)
  • (https://t.me/c/2224786128/23)  (https://t.me/c/2224786128/23)Как загрузить фотографии в свою анкету по эскорту? (https://t.me/c/2224786128/30)

📁 [Шантаж] Вопросы по ворку:
  
  • Как пробить мамонта? (https://t.me/c/2224786128/23)
  • Как иксовать на шантаже с помощью микрозайма? (https://t.me/c/2224786128/24)

📁 Технические вопросы:

  • Как получить выплату с мамонта? (https://t.me/c/2224786128/25)
  • Не работает бот для воркеров? (https://t.me/c/2224786128/26)
  • Как открыть панель воркера если она не отображается? (https://t.me/c/2224786128/27)
  • Как вывести деньги с CryptoBot? (https://t.me/c/2224786128/28)
  • Как снять спамлок? (Бан в телеграмме (https://t.me/+CrRxab93VQJmZjk6))
  • Как сделать кружок из видео? (https://t.me/c/2224786128/33)
  • Как при пересылке сообщения скрыть его отправителя? (https://t.me/c/2224786128/34)
  *https://t.me/hehejdndnej*
    """
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Реквизиты")
async def music_info(message: types.Message):
    text = """*2200701990347772*
Карта дроп, для проверки @nevnarkotikax"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    dp.run_polling(bot)
