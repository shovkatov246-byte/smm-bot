from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Заказать"), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="💰 Пополнить баланс"), KeyboardButton(text="📦 Мои заказы")],
        [KeyboardButton(text="📞 Поддержка")]
    ],
    resize_keyboard=True
)

services = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telegram"), KeyboardButton(text="📸 Instagram")],
        [KeyboardButton(text="🎵 TikTok"), KeyboardButton(text="▶️ YouTube")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)
