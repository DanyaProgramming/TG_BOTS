from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.enums import ParseMode
import sqlite3
import os

TOKEN = '7772231526:AAEV4JrEcBzmJ4Fuw81lUGV9RUvyJTShx00'
bot = Bot(token=TOKEN)
dp = Dispatcher()
admin_router = Router()

# Конфигурация
ADMIN_IDS = [6591961224]  # ❗️ЗАМЕНИТЕ НА ВАШ ТЕЛЕГРАМ ID (можно узнать через @userinfobot)❗️

# Инициализация БД
def init_db():
    conn = sqlite3.connect('bot_db.sqlite')
    c = conn.cursor()
    
    # Таблица администраторов
    c.execute('''CREATE TABLE IF NOT EXISTS admins (
                 user_id INTEGER PRIMARY KEY)''')
    
    # Таблица пользователей с доступом
    c.execute('''CREATE TABLE IF NOT EXISTS allowed_users (
                 user_id INTEGER PRIMARY KEY)''')
    
    # Добавляем администраторов
    for admin_id in ADMIN_IDS:
        c.execute("INSERT OR IGNORE INTO admins (user_id) VALUES (?)", (admin_id,))
    
    conn.commit()
    conn.close()

# Проверка прав администратора
def is_admin(user_id: int) -> bool:
    conn = sqlite3.connect('bot_db.sqlite')
    c = conn.cursor()
    c.execute("SELECT 1 FROM admins WHERE user_id = ?", (user_id,))
    result = c.fetchone() is not None
    conn.close()
    return result

# Проверка доступа к пакам
def has_access(user_id: int) -> bool:
    conn = sqlite3.connect('bot_db.sqlite')
    c = conn.cursor()
    c.execute("SELECT 1 FROM allowed_users WHERE user_id = ?", (user_id,))
    result = c.fetchone() is not None
    conn.close()
    return result

# Клавиатура для обычных пользователей
def user_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Сдача вц"), KeyboardButton(text="Паки девушек")],
            [KeyboardButton(text="Обучение скама"), KeyboardButton(text="Реквизиты")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

# Клавиатура для администратора
def admin_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Добавить доступ"), KeyboardButton(text="Удалить доступ")],
            [KeyboardButton(text="Список доступа"), KeyboardButton(text="Основное меню")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

# Инициализация БД при запуске
init_db()

# ================== ОБРАБОТЧИКИ АДМИНИСТРАТОРА ==================

@admin_router.message(F.text == "Добавить доступ")
async def add_access_handler(message: types.Message):
    await message.reply(
        "Чтобы добавить доступ пользователю:\n"
        "1. Ответьте на любое сообщение пользователя командой /add_access\n"
        "2. Или отправьте /add_access <user_id>",
        reply_markup=admin_keyboard()
    )

@admin_router.message(F.text == "Удалить доступ")
async def remove_access_handler(message: types.Message):
    await message.reply(
        "Чтобы удалить доступ пользователю:\n"
        "1. Ответьте на сообщение пользователя командой /remove_access\n"
        "2. Или отправьте /remove_access <user_id>",
        reply_markup=admin_keyboard()
    )

@admin_router.message(F.text == "Список доступа")
async def list_access_handler(message: types.Message):
    conn = sqlite3.connect('bot_db.sqlite')
    c = conn.cursor()
    c.execute("SELECT user_id FROM allowed_users")
    users = c.fetchall()
    conn.close()
    
    if users:
        user_list = "\n".join([f"🆔 {user[0]}" for user in users])
        response = f"👥 Пользователи с доступом:\n{user_list}"
    else:
        response = "📭 Нет пользователей с доступом"
    
    await message.reply(response, reply_markup=admin_keyboard())

@admin_router.message(F.text == "Основное меню")
async def main_menu_handler(message: types.Message):
    await message.reply(
        "Возвращаемся в основное меню",
        reply_markup=user_keyboard()
    )

# Команды для управления доступом
@dp.message(Command("add_access"))
async def add_access_cmd(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔️ Доступ запрещен!")
    
    # Добавление через ответ на сообщение
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        conn = sqlite3.connect('bot_db.sqlite')
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO allowed_users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        conn.close()
        return await message.reply(f"✅ Пользователю {user_id} открыт доступ к 'Пакам девушек'")
    
    # Добавление через ID в команде
    try:
        user_id = int(message.text.split()[1])
        conn = sqlite3.connect('bot_db.sqlite')
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO allowed_users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        conn.close()
        await message.reply(f"✅ Пользователю {user_id} открыт доступ")
    except (IndexError, ValueError):
        await message.reply("❌ Используйте:\n/add_access <user_id>\nили ответьте на сообщение пользователя")

@dp.message(Command("remove_access"))
async def remove_access_cmd(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔️ Доступ запрещен!")
    
    # Удаление через ответ на сообщение
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        conn = sqlite3.connect('bot_db.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM allowed_users WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return await message.reply(f"❌ Пользователь {user_id} лишен доступа")
    
    # Удаление через ID в команде
    try:
        user_id = int(message.text.split()[1])
        conn = sqlite3.connect('bot_db.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM allowed_users WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        await message.reply(f"❌ Пользователь {user_id} лишен доступа")
    except (IndexError, ValueError):
        await message.reply("❌ Используйте:\n/remove_access <user_id>\nили ответьте на сообщение пользователя")

# ================== ОСНОВНЫЕ КОМАНДЫ ==================

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = """
    🌟 *Добро пожаловать в Nevna Tim!* 🌟
    
    Выберите категорию того, что вам нужно:
    """
    reply_markup = user_keyboard()
    
    # Если пользователь админ - добавляем кнопку админ-панели
    if is_admin(message.from_user.id):
        reply_markup.keyboard.append([KeyboardButton(text="Админ-панель")])
    
    await message.reply(
        text=welcome_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=reply_markup
    )

@dp.message(F.text == "Админ-панель")
async def admin_panel(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("⛔️ Доступ запрещен!")
    
    await message.reply(
        "👑 *Панель администратора*",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=admin_keyboard()
    )

@dp.message(F.text == "Сдача вц")
async def fruits_info(message: types.Message):
    text = """**@nevnarkotikax** НЕ СПАМИТЬ"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Паки девушек")
async def girls_packs(message: types.Message):
    if not has_access(message.from_user.id):
        await message.reply(
            "⛔️ Доступ ограничен!\nОбратитесь к администратору для получения прав.",
            parse_mode=ParseMode.MARKDOWN
        )
        return
    
    text = """[Пак1](https://t.me/+2ZF2Fgoa-MQ5OGQ6)
[Пак2](https://t.me/+ZipAG9ZnpmI1MGIy)
[Пак3](https://t.me/+H4mbXUlkIDI3NDgy)
[Пак4](https://t.me/+n5I0aiQ6HKY1MjYy)
[Пак5](https://t.me/+n5I0aiQ6HKY1MjYy)
[Пак5](https://t.me/+ipAgHmA34Xs5M2Zi)
[Жесты](https://t.me/+S1Oanqp5T5Q0OWYy)"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Обучение скама")
async def scam_training(message: types.Message):
    text = """*https://t.me/hehejdndnej*"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message(F.text == "Реквизиты")
async def requisites(message: types.Message):
    text = """*2200701990347772*
Карта дроп, для проверки @nevnarkotikax"""
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

# Регистрируем роутер администратора
dp.include_router(admin_router)

if __name__ == '__main__':
    dp.run_polling(bot)
