from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Заказать"), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="💰 Пополнить баланс"), KeyboardButton(text="📦 Мои заказы")],
        [KeyboardButton(text="📞 Поддержка")]
    ],
    resize_keyboard=True
)

# Меню выбора платформы
services = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telegram"), KeyboardButton(text="📸 Instagram")],
        [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🚀 Добро пожаловать в SMM Bot!\n\nВыберите нужный раздел:",
        reply_markup=menu
    )

@dp.message()
async def buttons(message: Message):
    if message.text == "👤 Профиль":
        await message.answer(
            f"👤 Ваш профиль\n\n🆔 ID: {message.from_user.id}\n💰 Баланс: 0 ₽"
        )

    elif message.text == "🛒 Заказать":
        await message.answer(
            "📦 Выберите платформу:",
            reply_markup=services
        )

    elif message.text == "📱 Telegram":
        await message.answer("📱 Скоро здесь появятся услуги Telegram.")

    elif message.text == "📸 Instagram":
        await message.answer("📸 Скоро здесь появятся услуги Instagram.")

    elif message.text == "🎵 TikTok":
        await message.answer("🎵 Скоро здесь появятся услуги TikTok.")

    elif message.text == "▶️ YouTube":
        await message.answer("▶️ Скоро здесь появятся услуги YouTube.")

    elif message.text == "🔙 Назад":
        await message.answer(
            "🏠 Главное меню",
            reply_markup=menu
        )

    elif message.text == "💰 Пополнить баланс":
        await message.answer("💳 Скоро здесь будет пополнение баланса.")

    elif message.text == "📦 Мои заказы":
        await message.answer("📦 У вас пока нет заказов.")

    elif message.text == "📞 Поддержка":
        await message.answer("📩 Напишите: @ВАШ_ЮЗЕРНЕЙМ")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
