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

    def convert_check_10(self,chk_list):
        list_bin_perm = []
        for _ in range(len(chk_list)):
            list_bin_perm.append(chk_list[_].get())
        # hex_perm_A =
        list_bin_perm_tmp = list_bin_perm[0:8]
        str_bin = ''.join(map(str,list_bin_perm_tmp[::-1]))
        str_bin = '0b'+ str_bin
        hex_A = hex(int(str_bin,2))[2:]
        if len(hex_A)<2:
            hex_A='0'+hex_A

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
        # print(list_bin_perm_tmp, str_bin,hex_A, hex_B, hex_C)
        return hex_A+hex_B+hex_C

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