import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# import time

import configparser

# Инициализация основных переменных
config = configparser.ConfigParser()
config.read("postgres.ini", encoding="utf-8")
dict_conf = {}

# Настройка БД
dict_conf['user'] = config["postgres"]["user"]
dict_conf['password'] = config["postgres"]["password"]
dict_conf['host'] = config["postgres"]["host"]
dict_conf['port'] = config["postgres"]["port"]
dict_conf['database'] = config["postgres"]["database"]


# print(dict_conf)


class PostgessBase:
    def __init__(self):
        try:
            # Подключение к существующей базе данных
            self.connection = psycopg2.connect(user=dict_conf['user'],
                                               # пароль, который указали при установке PostgreSQL
                                               password=dict_conf['password'],
                                               host=dict_conf['host'],
                                               port=dict_conf['port'],
                                               database=dict_conf['database'])
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Курсор для выполнения операций с базой данных
            self.cursor = self.connection.cursor()

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def __del__(self):
        try:
            if self.connection:
                self.cursor.close()
                # self.connection.close()
                print("Соединение с PostgreSQL закрыто")
        except (Exception, Error) as error:
            print("Ошибка при открытии", error)

    def search_fio(self, name, firstname, secondname):
        insert_query = f"SELECT * FROM staff.person WHERE name ilike '%{name}%' AND " \
                       f"firstname ilike '%{firstname}%' " \
                       f"AND secondname ilike '%{secondname}%' " # AND  personcatid IS NOT NULL"
        self.cursor.execute(insert_query)
        person_list = []
        for _ in self.cursor.fetchall():
            # _[0] = personid
            insert_query = f"SELECT cardid FROM staff.pass WHERE personid = '{_[0]}' and cardstatus = 1"
            self.cursor.execute(insert_query)
            cardid = self.cursor.fetchall()

            if len(cardid) > 0:
                # print(cardid)
                insert_query = f"SELECT fullcardcode FROM staff.card WHERE cardid = '{cardid[0][0]}'"
                self.cursor.execute(insert_query)
                key = self.cursor.fetchall()
                person_list.append([_[2], _[3], _[4], _[5], key[0][0]])  # name, firstname, secondname, tableno, key

        return person_list

    def seach_card(self,key):
        insert_query = f"SELECT cardstatus FROM staff.card WHERE fullcardcode = '{key}' and cardstatus = '1'"
        self.cursor.execute(insert_query)
        cardstatus = self.cursor.fetchall()
        if len(cardstatus) == 0:
            return 0
        else:
            return cardstatus[0][0]



if __name__ == '__main__':
    bd = PostgessBase()
    # print(bd.select_date())
    # a = bd.search_fio('ноздр', 'свет', 'п')
    # print(len(a))
    # for _ in a:
    #     print(_)
    print(bd.seach_card('000000559188'))
    print(bd.seach_card('00000073D712'))
    print(bd.seach_card('0000003DFAD9'))
