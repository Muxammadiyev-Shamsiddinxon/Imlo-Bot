import logging
from  transliterate import to_cyrillic,to_latin
from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
API_TOKEN = '5181641032:AAEnbdq26Mv70vJICtpNC6VDYhydXlcJWao'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Alaykum.✅✅\nImlo-Xato botiga Xush Kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = to_cyrillic(message.text)
    result = checkWord(word)
    if result['available']:
        response = f"😎☚@Hacker_Attacks1☛😎\n✅ {to_latin(word.capitalize())}"
    else:
        response = f"😎☚@Hacker_Attacks1☛😎\n❌{to_latin(word.capitalize())}\n"
        for text in result['matches']:
            response += f"✅ {to_latin(text.capitalize())}\n"
        response+="\nYana so'z kiriting! ✅✅"
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)