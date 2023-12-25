from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard = [
         [
         KeyboardButton(text="🔎"),
         KeyboardButton(text="✅ Channel"),
         KeyboardButton(text="❓"),
         ],
       ],
       resize_keyboard=True
)

nazat = ReplyKeyboardMarkup(
    keyboard = [
         [
         KeyboardButton(text="◀️ Orqaga"),
         ],
       ],
       resize_keyboard=True
)
