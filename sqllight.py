import sqlite3

class SQLighter:
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id,  car_model=None,  first_name=None, last_name=None, username=None, manufacture_date=None, status = True,):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`, car_model, first_name, last_name, username, manufacture_date) VALUES(?,?,?,?,?,?,?)", (user_id, status, car_model, first_name, last_name, username, manufacture_date))

    def update_car(self, user_id, car_model, manufacture_date=None ):
        """Обновляем модель машины"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `car_model` = ?, `manufacture_date`= ? WHERE `user_id` = ?", (car_model,  manufacture_date, user_id))
        
    def update_car_date(self, user_id, manufacture_date):
        """Обновляем даты производтсва машины"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `manufacture_date` = ? WHERE `user_id` = ?", (manufacture_date, user_id))
        
    def update_subscription(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ?  WHERE `user_id` = ?", (status, user_id))


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
