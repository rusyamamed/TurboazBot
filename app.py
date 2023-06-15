import asyncio
from loader import scheduler
# 
# 
# from aiogram import Bot, Dispatcher, executor
# from config import BOT_TOKEN
# 
# loop = asyncio.get_event_loop()
# bot = Bot(BOT_TOKEN, parse_mode='HTML')
# dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp
#     
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler(60))
    executor.start_polling(dp)