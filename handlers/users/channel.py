from aiogram.types import Message
from loader import dp

@dp.message_handler(text="✅ Channel")
async def kanal(message:
Message):
	msg = "<b>💡Bizning Rasmiy Kanalmiz!\n\n🛠 Quydagi kanalda biz yaratgan yangi turdagi botlarni joylan boramiz ➕Azo bo'lishni unutmang👇\n\n📡 Channel 👉 https://t.me/Python_Koderuz\n\n✅ @wikilotinbot</b>"
	photo_id = "AgACAgIAAxkBAANaYi78df1EHpnU73NvWbEcpy81hF4AAoS6MRsig3lJqLxpN1iAl7QBAAMCAAN5AAMjBA"
	await message.answer_photo(photo_id,caption=msg)
	
@dp.message_handler(text="❓")
async def help(message:
Message):
	msgi = "<b>🤖 Ushbu Botimiz haqida qisqacha malumot!\n\n📇 Ushbu Wikipedia botimiz orqali o'zingizni qiziqtirgan hohlagan savollarga javob topishingiz mumkin!\n\n💬 Savollar bo'lsa 👉 @SavoIborBot\n\n✅ @wikilotinbot</b>"
	photo = "AgACAgIAAxkBAANkYi8AAS6g3a-fLR6DY7ey7kdHAqOhAAKFujEbIoN5SaxoFFZ_jmwRAQADAgADeAADIwQ"
	await message.answer_photo(photo,caption=msgi)
