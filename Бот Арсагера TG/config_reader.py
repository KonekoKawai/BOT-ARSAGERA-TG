
################################### ���������� ���������� ###################################

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

import requests; # ���������� ��������
import _strptime
import time
import datetime;
from datetime import timedelta, date


import enum


#import logging # ���������� ��� �������� ����� #logging.error(msg!!!, exc_info=True)

#############################################################################################

########   ��������� ������   #####

#logging.basicConfig(level=logging.INFO) 
   
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

