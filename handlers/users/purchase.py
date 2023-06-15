from aiogram.dispatcher.filters import Command
from loader import dp, db
from aiogram.types import Message
from keyboards.choice_buttons import (select, mercedes,
                                      bmw, kia, hyundai, toyota,
                                      mercedes_a, mercedes_b, mercedes_c,
                                      mercedes_e, mercedes_s, mercedes_ml,
                                      mercedes_vita, car_date, chevrolet
                                      )
from aiogram.types.callback_query import CallbackQuery
from keyboards.callback_datas import select_callback
import logging
from aiogram import types
from turboazparser import TurboAz
import os

current_directory = os.getcwd()

log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)


# задаем уровень логов
#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
fh = logging.FileHandler(current_directory+'/'+log_folder+'/TurboBotLog.log')
fh.setFormatter(formatter)
fh.setLevel(logging.INFO) # or any level you want
logger.addHandler(fh)
# задаем уровень логов
logging.basicConfig(level=logging.INFO)
# инициализируем парсер
parser = TurboAz('lastkeyturboaz.txt')
# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    print(message)
    if(not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)
    await message.answer("Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые посты и вы узнаете о них первыми =)")

# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")

@dp.message_handler(Command("carlist"))
async def show_items(message: Message):
    print(message)
    await message.answer(text="Пожалуйста выберите машину.",
                         reply_markup=select )

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes"))
async def selecting_mercedes(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")

    await call.message.answer(f"Your choice is {car_model}. Please choose model",
                              reply_markup=mercedes)

@dp.callback_query_handler(select_callback.filter(item_name="BMW"))
async def selecting_bmw(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    await call.message.answer(f"Your choice is {car_model}. Please choose model.",
                              reply_markup=bmw)
@dp.callback_query_handler(select_callback.filter(item_name="Kia"))
async def selecting_kia(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    await call.message.answer(f"Your choice is {car_model}. Please choose model.",
                              reply_markup=kia)
@dp.callback_query_handler(select_callback.filter(item_name="Hyundai"))
async def selecting_hyundai(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    await call.message.answer(f"Your choice is {car_model}. Please choose model.",
                              reply_markup=hyundai)
@dp.callback_query_handler(select_callback.filter(item_name="Toyota"))
async def selecting_toyota(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    await call.message.answer(f"Your choice is {car_model}. Please choose model.",
                              reply_markup=toyota)
@dp.callback_query_handler(select_callback.filter(item_name="Chevrolet"))
async def selecting_chevrolet(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    await call.message.answer(f"Your choice is {car_model}. Please choose model.",
                              reply_markup=chevrolet)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes A"))
async def selecting_mers_a(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_a)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes B"))
async def selecting_mers_b(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_b)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes C"))
async def selecting_mers_c(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_c)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes E"))
async def selecting_mers_e(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_e)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes S"))
async def selecting_mers_s(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_s)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes ML"))
async def selecting_mers_ml(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_ml)

@dp.callback_query_handler(select_callback.filter(item_name="Mercedes Vito"))
async def selecting_mers_vita(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    print(callback_data.get("item_name"))
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if(not db.subscriber_exists(user_id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(user_id, car_model, first_name, last_name, username )
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_car(user_id,  car_model)
    await call.message.answer(f"Вы выбрали {car_model}. Пожалуйста выберите модель.",
                              reply_markup=mercedes_vita)










@dp.callback_query_handler(text_contains="cancel")
async def cancel_selecting(call: CallbackQuery):
    await call.answer("You canceled.")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(select_callback.filter())
async def selecting_model_date(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    print(callback_data)
    car_model = callback_data.get("item_name")
    user_id = call.message.chat.id
    first_name= call.message.chat.first_name
    last_name = call.message.chat.last_name
    username = call.message.chat.username
    if not car_model[0].isdigit():
        if(not db.subscriber_exists(user_id)):
            # если юзера нет в базе, добавляем его
            db.add_subscriber(user_id, car_model, first_name, last_name, username )
        else:
            # если он уже есть, то просто обновляем ему статус подписки
            db.update_car(user_id,  car_model)
        await call.message.answer(f"Ваша модель {car_model}. Выберите год выпуска.", reply_markup=car_date)
    else:
        user_id = call.message.chat.id
        manufac_date = callback_data.get("item_name")
        db.update_car_date(user_id,  manufac_date)
        await call.message.answer(f"Вы выбрали модель выпуска: {manufac_date} года.")

