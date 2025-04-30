
################################### ПОДКЛЮЧАЕМ БИБЛИОТЕКИ ###################################

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

import requests; # Библиотека запросов
import _strptime
import time
import datetime;
from datetime import timedelta, date


import enum


#import logging # библиотека для хранения логов #logging.error(msg!!!, exc_info=True)

#############################################################################################

########   Настройка логера   #####

#logging.basicConfig(level=logging.INFO) 
   
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

