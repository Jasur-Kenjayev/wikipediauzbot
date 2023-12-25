from aiogram.types import Message
from loader import dp
import wikipedia
from keyboards.default.menu import nazat, Menu
from states.savol import PersonalData2
from aiogram.dispatcher import FSMContext
from aiogram import types

wikipedia.set_lang('uz')

@dp.message_handler(text= "◀️ Orqaga",state=PersonalData2.adss2)
async def cancel1(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🏠Bosh Menudasiz✅</b>",reply_markup=Menu)

@dp.message_handler(text="🔎")
async def savolb(message: Message):
	await message.answer("<b>✏️ Marhammat Savolingizni Kiriting!</b>",reply_markup=nazat)
	await PersonalData2.adss2.set()
	
@dp.message_handler(state=PersonalData2.adss2)
async def savol(message: types.Message, state: FSMContext):
    msg11 = await message.answer('<b>◾️ 10%</b>')
    await msg11.delete()
    msg = await message.answer('<b>◾️◾️ 20%</b>')
    await msg.delete()
    msg1 = await message.answer('<b>◾️◾️◾️ 30%</b>')
    await msg1.delete()
    msg2 = await message.answer('<b>◾️◾️◾️◾️ 40%</b>')
    await msg2.delete()
    msg3 = await message.answer("<b>◾️◾️◾️◾️◾️ 50%</b>")
    await msg3.delete()
    msg4 = await message.answer("<b>◾️◾️◾️◾️◾️◾️ 60%</b>")
    await msg4.delete()
    msg5 = await message.answer("<b>◾️◾️◾️◾️◾️◾️◾️ 70%</b>")
    await msg5.delete()
    msg6 = await message.answer('<b>◾️◾️◾️◾️◾️◾️◾️◾️ 80%</b>')
    await msg6.delete()
    msg7 = await message.answer("<b>◾️◾️◾️◾️◾️◾️◾️◾️◾️ 90%</b>")
    await msg7.delete()
    msg8 = await message.answer("<b>◾️◾️◾️◾️◾️◾️◾️◾️◾️ 100%</b>")
    await msg8.delete()
    
    await message.reply("<i>⏳iltimos Biroz Kuting....</i>")
    try:
    	respond = wikipedia.summary(message.text)
    	await message.reply(f"<b>{respond}\n\n✅ @wikilotinbot</b>")
    except:
    	await message.answer("<b>📝Bu mavzuga oid maqola topilmadi😔</b>")