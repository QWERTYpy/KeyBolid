# Класс описывающий доступ предоставленный определенному человеку
import tkinter as tk

class Person:
    def __init__(self):
        self.name = ''  # Имя
        self.surname = ''  # Фамилия
        self.patronymic = ''  # Отчество
        self.key = ''  # Ключ
        self.permission = {}  # Права доступа # id: [Номер прибора, ХО, Доступ]

    def show(self):
        print(self.name,self.surname,self.patronymic,self.key,self.permission)

    def get_check_10(self,id):
        permission = self.permission[id][2]
        self.chk_list = []
        # print(permission[4:6])

        bin_perm = bin(int(permission[0:2], 16))
        list_bin_perm_A = list(bin_perm[:1:-1])
        if len(list_bin_perm_A) < 8:
            for _ in range(8-len(list_bin_perm_A)):
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
        list_bin_perm = list_bin_perm_A+list_bin_perm_B+list_bin_perm_C
        # print(list_bin_perm)
        for _ in range(20):
            self.chk_list.append(tk.IntVar(value=list_bin_perm[_]))

        return self.chk_list

if __name__ == '__main__':
    per = Person()
    per.get_check_10()