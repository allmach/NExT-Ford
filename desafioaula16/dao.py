#DAO "Data Access Object", é um padrão de objeto utilizado para isolar os códigos relacionados à lógica do banco de dados e o código da aplicação.

from models import Restaurant, User

SQL_DELETE_RESTAURANT = 'delete from restaurant where id = %s'
SQL_RESTAURANT_PER_ID = 'SELECT id, plate, category, price from restaurant where id = %s'
SQL_USER_PER_ID = 'SELECT id, name, password from user where id = %s'
SQL_UPDATE_RESTAURANT = 'UPDATE restaurant SET plate=%s, category=%s, price=%s where id = %s'
SQL_SEARCH_RESTAURANT = 'SELECT id, plate, category, price from restaurant'
SQL_CREATE_RESTAURANT = 'INSERT into restaurant (plate, category, price) values (%s, %s, %s)'


class RestaurantDao:
    def __init__(self, db):
        self.__db = db

    def save(self, restaurant):
        cursor = self.__db.connection.cursor()

        if (restaurant.id):
            cursor.execute(SQL_UPDATE_RESTAURANT, (restaurant.plate, restaurant.category, restaurant.price, restaurant.id))
        else:
            cursor.execute(SQL_CREATE_RESTAURANT, (restaurant.plate, restaurant.category, restaurant.price))
            restaurant.id = cursor.lastrowid
        self.__db.connection.commit()
        return restaurant

    def list(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SEARCH_RESTAURANT)
        restaurants = save_restaurants(cursor.fetchall())
        return restaurants

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RESTAURANT_PER_ID, (id,))
        tupla = cursor.fetchone()
        return Restaurant(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def delete(self, id):
        self.__db.connection.cursor().execute(SQL_DELETE_RESTAURANT, (id, ))
        self.__db.connection.commit()


class UserDao:
    def __init__(self, db):
        self.__db = db

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USER_PER_ID, (id, ))
        dados = cursor.fetchone()
        user = search_user(dados) if dados else None
        return user


def save_restaurants(restaurants):
    def create_restaurant_com_tupla(tupla):
        return Restaurant(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(create_restaurant_com_tupla, restaurants))


def search_user(tupla):
    return User(tupla[0], tupla[1], tupla[2])