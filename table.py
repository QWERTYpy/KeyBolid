# Класс отвечающий за вывод основной таблицы данных
from tkinter import ttk
import tkinter as tk


class Table:
    def __init__(self, root, info_frame, object_list, person_list):
        self.root = root
        self.object_list = object_list
        self.person_list = person_list
        self.info_frame = info_frame
        self.object_main = '000'
        self.object_list_len = len(object_list)
        # Сортировка по Объектам
        self.combobox_sort()
        # Поиск
        self.search_table()
        # Отображаем таблицу
        self.main_table_create()

    def main_table_create(self):
        # Составляем колонки
        table_column = ('surname', 'name', 'patronymic', 'hex_key')
        self.main_table = ttk.Treeview(self.root, columns=table_column, show='headings')
        self.main_table.grid(row=2, column=0, columnspan=4, rowspan=25, sticky="nsew")

        # определяем заголовки
        self.main_table.heading('name', text='Имя', anchor=tk.W)
        self.main_table.heading('surname', text='Фамилия', anchor=tk.W)
        self.main_table.heading('patronymic', text='Отчество', anchor=tk.W)
        self.main_table.heading('hex_key', text='Ключ', anchor=tk.W)
        self.main_table.column("#1", stretch=tk.NO, width=200)
        self.main_table.column("#2", stretch=tk.NO, width=200)
        self.main_table.column("#3", stretch=tk.NO, width=200)
        self.main_table.column("#4", stretch=tk.NO, width=200)
        # Добавляем прокрутку
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.main_table.yview)
        self.main_table.configure(yscroll=self.scrollbar.set, height=25)
        self.scrollbar.grid(row=2, column=4, rowspan=25, sticky="ns")
        # Составляем данные для отображения
        self.people_table = [(_.surname, _.name, _.patronymic, _.key) for _ in self.person_list]
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)

    def search_table_action(self):
        # self.main_table.delete(self.main_table.selection()[0])
        # Очищаем
        self.main_table.delete(*self.main_table.get_children())
        if self.entry_surname.get() or self.entry_name or self.entry_patronymic or self.entry_hex:
            self.people_table = [(_.surname, _.name, _.patronymic, _.key) for _ in self.person_list
                                 if self.entry_surname.get() in _.surname
                                 and self.entry_name.get() in _.name
                                 and self.entry_patronymic.get() in _.patronymic
                                 and self.entry_hex.get() in _.key.decode("utf-8")
                                 and (self.object_main in _.permission.keys() or self.object_main == '000')]
        else:
            self.people_table = [(_.surname, _.name, _.patronymic, _.key) for _ in self.person_list
                                 if (self.object_main in _.permission.keys() or self.object_main == '000')]
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)

    def search_table(self):
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.config(width=32)
        self.entry_name.grid(row=1, column=1, sticky=tk.NW, ipady=1)
        self.entry_surname = ttk.Entry(self.root)
        self.entry_surname.config(width=32)
        self.entry_surname.grid(row=1, column=0, sticky=tk.NW, ipady=1)
        self.entry_patronymic = ttk.Entry(self.root)
        self.entry_patronymic.config(width=32)
        self.entry_patronymic.grid(row=1, column=2, sticky=tk.NW, ipady=1)
        self.entry_hex = ttk.Entry(self.root)
        self.entry_hex.config(width=32)
        self.entry_hex.grid(row=1, column=3, sticky=tk.NW, ipady=1)
        self.btn_entry = ttk.Button(self.root, text='>', command=self.search_table_action, width=2)
        self.btn_entry.grid(row=1,column=4, sticky=tk.NW)

    def combobox_sort(self):
        # Создаем метку с описанием
        self.label_obj = ttk.Label(self.root, text="Выберите прибор:", background='white')
        self.label_obj.grid(row=0, column=0, sticky=tk.W)
        # Создаем выпадающий список
        combobox_obj_val = 'Все',
        self.object_dict = {f"{self.object_list[_].num} - {self.object_list[_].name}": self.object_list[_].id for _ in range(self.object_list_len)}
        combobox_obj_val += tuple(self.object_dict.keys())
        self.combobox_obj_var = tk.StringVar(value=combobox_obj_val[0])
        self.combobox_obj = ttk.Combobox(self.root, textvariable=self.combobox_obj_var)
        self.combobox_obj.config(width=29)
        self.combobox_obj['values'] = combobox_obj_val
        self.combobox_obj['state'] = 'readonly'
        self.combobox_obj.grid(row=0, column=1, sticky=tk.W)
        # Создаем кнопку для взаимодействия
        self.combobox_btn = ttk.Button(self.root, text='Выбрать', command=self.combobox_btn_press)
        self.combobox_btn.grid(row=0, column=2)

    def combobox_btn_press(self):
        if self.combobox_obj_var.get() == "Все":
            self.object_main = "000"
        else:
            self.object_main = self.object_dict[self.combobox_obj_var.get()]
        self.search_table_action()



