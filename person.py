# Класс описывающий доступ предоставленный определенному человеку

class Person:
    def __init__(self):
        self.name = ''  # Имя
        self.surname = ''  # Фамилия
        self.patronymic = ''  # Отчество
        self.key = ''  # Ключ
        self.permission = {}  # Права доступа # id: [Номер прибора, ХО, Доступ]

    def show(self):
        print(self.name,self.surname,self.patronymic,self.key,self.permission)