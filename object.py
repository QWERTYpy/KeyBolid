# Класс описывающий прибор


class ObjectBolid:
    def __init__(self):
        self.num = 0  # Номер прибора
        self.id = 0  # Возможно потребуется для дублированный адресов
        self.name = ''  # Название
        self.type = 0  # Тип прибора 4/10
        self.ver = ''  # Версия
        self.comment = ''  # Комментарий


    def show(self):
        print(self.num,self.id,self.name,self.type,self.ver,self.comment)
