
################################### ПОДКЛЮЧАЕМ БИБЛИОТЕКИ ###################################

from asyncio.windows_events import NULL
import datetime
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

import enum
import logging # библиотека для хранения логов #logging.error(msg!!!, exc_info=True)
import asyncio # библиотека для асинхронного программирования
from asyncio import Future
import aiogram #import aiogram # Каркас для API Telegram Bot 
from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.filters import Command, StateFilter, BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, user
from aiogram.enums import ParseMode

#############################################################################################

########   Настройка логера   #####

logging.basicConfig(level=logging.INFO) 
   
# logger = logging.getLogger(__name__); # Имя файла в логгере
# logger.setLevel(logging.DEBUG); # LVL для обработки в логгере (Уровень логирования)

# loggerHandler = logging.FileHandler(f'{__name__}.log', filemode="w"); # настройка обработчика для logger
# loggerFormat = logging.Formatter("%(filename)s | %(asctime)s | %(levelname)s | %(message)s"); # настройка форматировщика

# loggerHandler.setFormatter(loggerFormat); # добавление форматировщика к обработчику
# logger.addHandler(loggerHandler); # добавление обработчика к логгеру


#############################################################################################

#Для токена
class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()

# id канала
file = open('channel_id.txt');
CHANNEL_ID = file.read();

global preValueMetrik;
preValueMetrik = 0;

bot = aiogram.Bot(token=config.bot_token.get_secret_value()) # Объект бота
disp = aiogram.Dispatcher() # Диспетчер

