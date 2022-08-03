import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
from transliterate import to_cyrillic, to_latin
from .set_bot_commands import set_default_commands

API_TOKEN='5584667811:AAGdirz2SlyYjLLN7W_gDcgoyIkbB8TJMWk'

# configure logging
logging.basicConfig(level=logging.INFO)

# initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer("Uz Imlo botiga xush kelibsiz!\nBotdan foydalanish uchun so‘z yuboring.")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.answer("Buyruqlar:\n- /start - Botdan foydalinishni boshlash\n- /help - ushbu xabarni qayta chiqarish\n\nBotdan foydalanish uchun so‘z yuboring.\nDasturchi: @muhammadrizodev")

@dp.message_handler()
async def checkImlo(message: types.Message):
    msg = message.text
    if message.text.isascii():
        msg = to_cyrillic(message.text)
    words = msg.split()
    for word in words:
        result = checkWord(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        if message.text.isascii():
            await message.answer(to_latin(response))
        else:
            await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)