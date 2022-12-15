from aiogram import Bot, Dispatcher

# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import API_TOKEN, DB_URL
from sqlalchemy import create_engine

engine = create_engine(DB_URL)
# storage = RedisStorage2('localhost', 6379)
storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
