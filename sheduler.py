async def scheduler(wait_for):
    while True:
        await asyncio.sleep(wait_for)
 
        # проверяем наличие новых машин
        new_cars = parser.new_car()
 
        if(new_cars):
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
                    if user_car in car['title']:
                        with open(parser.download_image(car['image']), 'rb') as photo:
                            await bot.send_photo(
                                subscriber[1],
                                photo,
                                caption = car['title'] + "\n" + "Price: " + car['price']  + "\n\n" + car['link'],
                                disable_notification = False
                            )
                            print(subscriber[1])
#                 photo.close()      
                # обновляем ключ
                parser.update_lastdate(car['date'])