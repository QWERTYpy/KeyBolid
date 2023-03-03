# Класс описывающий доступ предоставленный определенному человеку
import tkinter as tk


class Person:
    def __init__(self, name='', surname='', patronymic='', key=''):
        self.name = name  # Имя
        self.surname = surname  # Фамилия
        self.patronymic = patronymic  # Отчество
        self.key = key  # Ключ
        self.permission = {}  # Права доступа # id_object: [Номер прибора, ХО, Доступ]

    def show(self):
        print(self.name, self.surname, self.patronymic, self.key, self.permission)

    def convert_check_10(self, chk_list):
        """
        Преобразует список флагов полученный из чекбоксов в hex строку
        :param chk_list: Список переменных чекбоксов
        :return: FFFFFF
        """
        list_bin_perm = []  # Список флагов
        for _ in range(len(chk_list)):
            list_bin_perm.append(chk_list[_].get())  # Заполянем список значениями флагов
        # Первые 8 флагов образуют 1 байт
        list_bin_perm_tmp = list_bin_perm[0:8]
        # Берем их в обратном порядке, преобразуем в строку и склеиваем
        str_bin = ''.join(map(str, list_bin_perm_tmp[::-1]))
        # Добавляем префикс чтобы указать, что это бинарная запись
        str_bin = '0b' + str_bin
        # Преобразуем в hex из бинарной строки и берем только значение
        hex_A = hex(int(str_bin, 2))[2:]
        # Если символов меньше 2 добиваем спереди 0
        if len(hex_A) < 2:
            hex_A = '0' + hex_A

        list_bin_perm_tmp = list_bin_perm[8:16]
        str_bin = ''.join(map(str, list_bin_perm_tmp[::-1]))
        str_bin = '0b' + str_bin
        hex_B = hex(int(str_bin, 2))[2:]
        if len(hex_B) < 2:
            hex_B = '0' + hex_B

        list_bin_perm_tmp = list_bin_perm[16:20]
        str_bin = ''.join(map(str, list_bin_perm_tmp[::-1]))
        str_bin = '0b' + str_bin
        hex_C = hex(int(str_bin, 2))[2:]
        if len(hex_C) < 2:
            hex_C = '0' + hex_C
        return hex_A + hex_B + hex_C

    def get_check_10(self, id_object):
        """
        Получение списка флагов для чекбоксов из hex
        :param id_object:
        :return:
        """
        # Получаем hex для данного Объекта
        permission = self.permission[id_object][2]
        # Инициализируем будущий список
        self.chk_list = []
        # Получаем первый байт и преобразуем в двоичный
        bin_perm = bin(int(permission[0:2], 16))
        # Получаем список битов в обратном порядке
        list_bin_perm_A = list(bin_perm[:1:-1])
        # Если длина меньше 8, то добиваем 0
        if len(list_bin_perm_A) < 8:
            for _ in range(8 - len(list_bin_perm_A)):
                list_bin_perm_A.append('0')

        bin_perm = bin(int(permission[2:4], 16))
        list_bin_perm_B = list(bin_perm[:1:-1])
        if len(list_bin_perm_B) < 8:
            for _ in range(8 - len(list_bin_perm_B)):
                list_bin_perm_B.append('0')

        bin_perm = bin(int(permission[4:6], 16))
        list_bin_perm_C = list(bin_perm[:1:-1])
        if len(list_bin_perm_C) < 4:
            for _ in range(4 - len(list_bin_perm_C)):
                list_bin_perm_C.append('0')
        # Составляем итоговый список с флагами
        list_bin_perm = list_bin_perm_A + list_bin_perm_B + list_bin_perm_C
        # Создаем список для чекбокса
        for _ in range(20):
            self.chk_list.append(tk.IntVar(value=list_bin_perm[_]))

        return self.chk_list

    def get_check_4(self, id_object):
        """
        С2000-4
        Получение списка флагов для чекбоксов из hex
        :param id_object:
        :return:
        """
        permission = self.permission[id_object][2]
        self.chk_list = []
        # Сами права находятся во 2 байте
        bin_perm = bin(int(permission[2:4], 16))
        list_bin_perm = list(bin_perm[:1:-1])

        if len(list_bin_perm) < 8:
            for _ in range(8 - len(list_bin_perm)):
                list_bin_perm.append('0')

        for _ in range(8):
            self.chk_list.append(tk.IntVar(value=list_bin_perm[_]))

        return self.chk_list

    def get_perm(self, id):
        """
        С2000-4
        Получение значения ключа ХО или прав доступа
        :param id:
        :return:
        """
        perm = self.permission[id][2][0:2]
        if perm == '10' or perm == '18':
            return tk.IntVar(value=1)
        else:
            return tk.IntVar(value=0)

    def convert_check_4(self, chk_list, perm):
        """
        Получение hex для C2000-4
        :param chk_list:
        :param perm:
        :return:
        """
        if perm.get():
            hex_A = '10'
        else:
            hex_A = '00'
        list_bin_perm = []
        for _ in range(len(chk_list)):
            list_bin_perm.append(chk_list[_].get())

        str_bin = ''.join(map(str, list_bin_perm[::-1]))
        str_bin = '0b' + str_bin
        hex_B = hex(int(str_bin, 2))[2:]
        if len(hex_B) < 2:
            hex_B = '0' + hex_B

        if hex_B != '00':
            if hex_A == '10':
                hex_A = '18'
            if hex_A == '00':
                hex_A = '08'
        return hex_A + hex_B + '00'


if __name__ == '__main__':
    per = Person()
    per.get_check_4()
