from aiogram import Bot, Dispatcher
import config
import asyncio
import logging
from turboazparser import TurboAz
from sqllight import SQLighter
import requests
import os

current_directory = os.getcwd()
log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# задаем уровень логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
fh = logging.FileHandler(current_directory+'/'+log_folder+'/ExceptParserLog.log')
fh.setFormatter(formatter)
fh.setLevel(logging.INFO) # or any level you want
logger.addHandler(fh)

# задаем уровень логов
logging.basicConfig(level=logging.INFO)
# инициализируем соединение с БД
db = SQLighter(current_directory+'/db.db')
# инициализируем парсер
parser = TurboAz(current_directory+'/lastkeyturboaz.txt')

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

async def scheduler(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        try:
            logger.info('Parsing !')
        # проверяем наличие новых машин
            new_cars = parser.new_car()
            if(new_cars):
                logger.info('Parsing afrer if statement!')
                print(new_cars)
                # если машины есть, переворачиваем список и итерируем
                new_cars.reverse()
                for newcar in new_cars:
                    # парсим инфу о новой машине
                    car = parser.car_info(newcar)

                    # получаем список подписчиков бота
                    users = db.get_subscriptions()
                    # отправляем всем новость
                    for subscriber in users:
                        user_car = subscriber[3]
                        car_date = subscriber[7]
                        if subscriber[2]:
                            if car_date:
                                if user_car in car['title']:
                                    if car_date in car['title']:
                                        with open(parser.download_image(car['image']), 'rb') as photo:
                                            await bot.send_photo(
                                                subscriber[1],
                                                photo,
                                                caption = car['title'] + "\n" + "Price: " + car['price']  + "\n\n" + car['link'],
                                                disable_notification = False
                                            )
                                            logger.info("{} - {}- {}".format(subscriber[4], subscriber[3], car['title']))
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                if user_car in car['title']:
                                    with open(parser.download_image(car['image']), 'rb') as photo:
                                        await bot.send_photo(
                                            subscriber[1],
                                            photo,
                                            caption = car['title'] + "\n" + "Price: " + car['price']  + "\n\n" + car['link'],
                                            disable_notification = False
                                        )
                                    logger.info("{} - {}- {}".format(subscriber[4], subscriber[3], car['title']))

        #                 photo.close()
                        # обновляем ключ
                        parser.update_lastdate(car['date'])
        except requests.exceptions.ConnectionError as e:
            logger.info(e)
            logger.info('turbo.az site is unreachable!!!!')
            pass
        except IndexError as e:
            logger.info(e)
            logger.info('We got index error in BeautifulSoup by parsing turboaz!!!!')
            pass
        except Exception as e :
            logger.info('We got some error!!!!' + str(e))
            pass
