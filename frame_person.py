import tkinter as tk
from tkinter import ttk
# Всплывающее меню при создании или редактировании информации о объекте
class FramePerson(tk.Toplevel):
    def __init__(self, parent, key, object, person_list, object_list):
        super().__init__(parent)
        self.key = key
        self.object = object
        self.person_list = person_list
        self.object_list = object_list
        self.create_frame()
        self.filling_person()
        self.flag_change = False

    def filling_person(self):
        for _ in self.person_list:
            if _.key == self.key:
                self.entry_name.insert(0,_.name)
                self.entry_surname.insert(0,_.surname)
                self.entry_patr.insert(0,_.patronymic)
                self.entry_hex.insert(0,_.key)

    def create_frame(self):
        self.label_surname = ttk.Label(self, text="Фамилия:")
        self.label_surname.grid(row=0, column=0, sticky='w')
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.grid(row=0, column=1)

        self.label_name = ttk.Label(self, text="Имя:")
        self.label_name.grid(row=1, column=0, sticky='w')
        self.entry_name = ttk.Entry(self)
        self.entry_name.grid(row=1, column=1)
        # self.entry_name.insert(0,"333")

        self.label_patr = ttk.Label(self, text="Отчество:")
        self.label_patr.grid(row=2, column=0, sticky='w')
        self.entry_patr = ttk.Entry(self)
        self.entry_patr.grid(row=2, column=1)

        self.label_hex = ttk.Label(self, text="Ключ:")
        self.label_hex.grid(row=3, column=0, sticky='w')
        self.entry_hex = ttk.Entry(self)
        self.entry_hex.grid(row=3, column=1)

        self.btn_save = ttk.Button(self, text='Сохранить', command=self.click_btn_save)
        self.btn_save.grid(row=10, column=10)

    def click_btn_save(self):
        self.flag_change = True
        for _ in self.person_list:
            if _.key == self.key:
                _.name = self.entry_name.get()
                _.surname = self.entry_surname.get()
                _.patronymic = self.entry_patr.get()
                _.key = self.entry_hex.get()