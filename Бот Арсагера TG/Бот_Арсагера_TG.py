from numpy import delete
import requests; # Библиотека запросов
import datetime;
from datetime import timedelta
import _strptime
import time
from datetime import date
from datetime import timedelta
import time

import config_reader
from config_reader import *

def reqWorldClock():
    print("Соединение - worldclock");
    req = requests.get('http://worldclockapi.com/api/json/utc/now')
    if (bool(req)): # Если соединение установлено 
        global reqDate;
        reqDate =  datetime.datetime.strptime(req.json()['currentDateTime'], "%Y-%m-%dT%H:%MZ"); #Парсим дату и время
        reqDate = reqDate + timedelta(hours=3) # Смещаем время до МСК
        reqDate = reqDate + timedelta(days=-1) # Смещаем дни на 1 Т.к Арсагера постит инфу за вчерашний предыдущий день

        reqDayOfTheWeek = req.json()['dayOfTheWeek']; # День недели
        global date_now;
        global time_now;
        date_now = reqDate.strftime("%Y-%m-%d") #Дата
        time_now = reqDate.strftime("%H:%M") #Время

        req.close();
        print("Разорвана связь - worldcloac");
    else:
        print("Что-то пошло не так - worldclock");
        exit();

def reqArsagera():
    print("Соединение - Arsagera");
    global requestNameMetrik
    requestNameMetrik= "fa"; # Метрика по акциям ФА

    req = requests.get(f"https://arsagera.ru/api/v1/funds/{requestNameMetrik}/fund-metrics/?date={date_now}"); #GET-запрос на сайт с арсагеры по метрике
    global valueMetrik;
    

    if ((req.status_code != 404 and 400 and 500)): #Если нет ошибки
        if not bool(req.json()['data']):
            print(f"За {date_now} данных по биржевым ориентирам нет!");
            valueMetrik = 0;
        else:
            
            valueMetrik = req.json()['data'][0]['nav_per_share'];
            print(f'Биржевые ориентиры Арсагера {requestNameMetrik.swapcase()}, на период {date_now}:', valueMetrik);
    else:
        print(req, "Что-то пошло не так - Arsagera");
    req.close();
    print("Разорвана связь - Arsagera");

def synCheckClock() -> bool:
    while(True):
        reqWorldClock();
        if(int(time_now.split(sep=':')[0]) >= 11 and int(time_now.split(sep=':')[0]) < 12): # Время публикации постов Первое значение на 1 час меньше
            time.sleep(3600-int(time_now.split(sep=':')[1])*60) # Отсчёт до 00 минут 
            return True
        else:
            time.sleep(3500)

async def sendInfoToChannel():
    global reqDate;
    global date_now;
    global time_now;
    global preValueMetrik;

    while(True):
        print("Вошли в цикл Арсагеры")
        
        date_now = reqDate.strftime("%Y-%m-%d") #Дата
        time_now = reqDate.strftime("%H:%M") #Время

        reqArsagera()

        print(f"Дата сегодня: {date_now}")

        if(valueMetrik!=0 and preValueMetrik!=0): # Если сегодня данные по арсагере есть
            smile = '↗️';
            diffMetrik = 0;

            if(valueMetrik/preValueMetrik > 1):
                diffMetrik = round((valueMetrik/preValueMetrik - 1)*100, 1);
                smile = '↗️';
            else:
                diffMetrik = -round((1-valueMetrik/preValueMetrik)*100, 1);
                smile = '↘️';

            preValueMetrik = valueMetrik;
            await bot.send_message(CHANNEL_ID, f'💰Биржевые ориентиры <b>Арсагера ФА</b>💰 \n\nСтоимость пая на дату <b>{date_now}</b> — <b><u>{valueMetrik}</u></b> рублей\n\nЦена за пай изменилась на <b>{diffMetrik}%</b>{smile} \n\n#Арсагера_ФА', parse_mode=ParseMode.HTML)
            

        elif(valueMetrik!=0):
            await bot.send_message(CHANNEL_ID, f'💰Биржевые ориентиры <b>Арсагера ФА</b>💰 \n\nСтоимость пая на дату <b>{date_now}</b> — <b><u>{valueMetrik}</u></b> рублей \n\n#Арсагера_ФА', parse_mode=ParseMode.HTML)
            preValueMetrik = valueMetrik;

        reqDate = reqDate + timedelta(days=1) # Смещаем день на 1 и засыпаем на 24 часа
        print(f"Завтрашняя дата: {reqDate.year}-{reqDate.day}-{reqDate.month}")
        time.sleep(86440) # засыпаем на 24 часа 


@disp.message() #Любая фраза вне контекста бота
async def any_message(message: Message):
    await message.delete()
    
#--------------------------------------------------------------------



# Запуск процесса поллинга  новых апдейтов (поиск обновлений от новых задач) // Polling, или опрос, – это процесс, при котором клиентский скрипт периодически отправляет запросы к серверу для проверки наличия новой инфы. 
async def main():
    
    print("Старт программы")

    #Тест
    # global reqDate;
    # global date_now;
    # global time_now;
    # global preValueMetrik;
    # preValueMetrik = 0;

    # reqDate = datetime.datetime.today();
    # reqDate = reqDate + timedelta(days=-7) # Смещаем время до МСК ##############################!!!!
    # date_now = reqDate.strftime("%Y-%m-%d") #Дата
    # time_now = reqDate.strftime("%H:%M") #Время

    synCheckClock() # Синхронизация с мировым временем до 12:00
    await sendInfoToChannel();

if __name__ == "__main__":
    asyncio.run(main())
