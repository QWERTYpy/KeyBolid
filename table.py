# Класс отвечающий за вывод основной таблицы данных
from tkinter import ttk
import tkinter as tk


class Table:
    def __init__(self, root, object_list):
        self.root = root
        self.object_list = object_list
        self.object_list_len = len(object_list)
        # Сортировка по Объектам
        self.combobox_sort()
        # Поиск
        self.search_table()
        # Отображаем таблицу
        self.main_table()

    def main_table(self):
        # Составляем колонки
        table_column = ('surname', 'name', 'patronymic', 'hex_key')
        self.main_table = ttk.Treeview(columns=table_column, show='headings')
        self.main_table.grid(row=5, column=0, columnspan=4, sticky="nsew")

        # определяем заголовки
        self.main_table.heading('name', text='Имя', anchor=tk.W)
        self.main_table.heading('surname', text='Фамилия', anchor=tk.W)
        self.main_table.heading('patronymic', text='Отчество', anchor=tk.W)
        self.main_table.heading('hex_key', text='Ключ', anchor=tk.W)
        self.main_table.column("#1", stretch=tk.NO, width=200)
        self.main_table.column("#2", stretch=tk.NO, width=200)
        self.main_table.column("#3", stretch=tk.NO, width=200)
        self.main_table.column("#4", stretch=tk.NO, width=200)

    def search_table(self):
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.config(width=32)
        self.entry_name.grid(row=1, column=0, sticky=tk.NW)
        self.entry_surname = ttk.Entry(self.root)
        self.entry_surname.config(width=32)
        self.entry_surname.grid(row=1, column=1, sticky=tk.NW)
        self.entry_patronymic = ttk.Entry(self.root)
        self.entry_patronymic.config(width=32)
        self.entry_patronymic.grid(row=1, column=2, sticky=tk.NW)
        self.entry_hex = ttk.Entry(self.root)
        self.entry_hex.config(width=32)
        self.entry_hex.grid(row=1, column=3, sticky=tk.NW)

    def combobox_sort(self):
        # Создаем метку с описанием
        self.label_obj = ttk.Label(self.root, text="Выберите прибор:", background='white')
        self.label_obj.grid(row=0, column=0, sticky=tk.W)
        # Создаем выпадающий список
        combobox_obj_val = 'Все',
        combobox_obj_val += tuple(
            f"{self.object_list[_].num} - {self.object_list[_].name}" for _ in range(self.object_list_len))
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
        print(self.combobox_obj_var.get())

