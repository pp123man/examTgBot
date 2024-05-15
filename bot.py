import os 
import logging, asyncio, sys
from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from functions import count, add_message 
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum! Ushbu bot guruhda habarlar sonini sanaydi!")

#/msg commandasi va /msg username commandasi 
@dp.message(Command('msg')) 
async def command_msg(message: types.Message):
    a = len(message.text)
    if(a == 4):
        res = str(add_message(message.text))
    else: 
        res = str(count(message.from_user.id))
    await message.answer(res)

# Guruhda yozgilan barcha xabarlarni va ularni sonini redisga saqlash
@dp.message()
async def group_filter(message: types.Message):
    if message.chat.type == 'supergroup': 
        add_message(message.text)
       
async def main() -> None:    
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())