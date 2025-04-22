
################################### ���������� ���������� ###################################

from asyncio.windows_events import NULL
import datetime
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

import enum
import logging # ���������� ��� �������� ����� #logging.error(msg!!!, exc_info=True)
import asyncio # ���������� ��� ������������ ����������������
from asyncio import Future
import aiogram #import aiogram # ������ ��� API Telegram Bot 
from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.filters import Command, StateFilter, BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, user
from aiogram.enums import ParseMode

#############################################################################################

########   ��������� ������   #####

logging.basicConfig(level=logging.INFO) 
   
# logger = logging.getLogger(__name__); # ��� ����� � �������
# logger.setLevel(logging.DEBUG); # LVL ��� ��������� � ������� (������� �����������)

# loggerHandler = logging.FileHandler(f'{__name__}.log', filemode="w"); # ��������� ����������� ��� logger
# loggerFormat = logging.Formatter("%(filename)s | %(asctime)s | %(levelname)s | %(message)s"); # ��������� ��������������

# loggerHandler.setFormatter(loggerFormat); # ���������� �������������� � �����������
# logger.addHandler(loggerHandler); # ���������� ����������� � �������


#############################################################################################

#��� ������
class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()

# id ������
file = open('channel_id.txt');
CHANNEL_ID = file.read();

global preValueMetrik;
preValueMetrik = 0;

bot = aiogram.Bot(token=config.bot_token.get_secret_value()) # ������ ����
disp = aiogram.Dispatcher() # ���������

