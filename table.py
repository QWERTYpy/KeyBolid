# Класс отвечающий за вывод основной таблицы данных
from tkinter import ttk
import tkinter as tk
import frame_person as fp
import c20004
import sig10


class Table:
    def __init__(self, root, info_frame, object_list, person_list):
        self.root = root  # Указатель на основное окно
        self.object_list = object_list  # Список Объектов
        self.person_list = person_list  # Список Персон
        self.info_frame = info_frame  # Указатель на информационное поле
        self.object_main = '000'  # По умолчанию выбран Объект 000 - Все
        self.object_list_len = len(object_list)  # Колличество Объектов
        # Добавление элемента для выбора конкретного Объекта
        self.combobox_sort()
        # Добавление полей для поиска по Персонам
        self.search_table()
        # Отображаем таблицу
        self.main_table_create()

    def main_table_create(self):
        # Составляем колонки
        table_column = ('surname', 'name', 'patronymic', 'hex_key')
        # Создаем таблицу
        self.main_table = ttk.Treeview(self.root, columns=table_column, show='headings')
        self.main_table.grid(row=2, column=0, columnspan=4, rowspan=25, sticky="nsew")
        # Определяем заголовки
        self.main_table.heading('name', text='Имя', anchor=tk.W)
        self.main_table.heading('surname', text='Фамилия', anchor=tk.W)
        self.main_table.heading('patronymic', text='Отчество', anchor=tk.W)
        self.main_table.heading('hex_key', text='Ключ', anchor=tk.W)
        # Определяем ширину столбцов
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
        # Определяем действие двойного щелчка по полю
        self.main_table.bind("<Double-Button-1>", self.left_button_double)

    def left_button_double(self, event):
        # Если ничего не выбрано
        if self.object_main == '000':
            return False
        # Если выбран Объект открываем дочернее окно
        frame_person = fp.FramePerson(self.root, str(self.main_table.item(self.main_table.selection())['values'][3]),
                                      self.object_main,
                                      self.person_list,
                                      self.object_list)

        frame_person.geometry("400x400+50+50")
        frame_person.title('Редактирование доступа')
        frame_person.grab_set()
        frame_person.wait_window()
        # Обновляем вывод в таблице
        if frame_person.flag_change:
            self.search_table_action()

    def reboot_table(self):
        """
        Общее обновление таблицы
        :return:
        """
        # Значение по умолчанию
        combobox_obj_val = 'Все',
        # Строки в выпадающем списке
        self.object_dict = {f"{self.object_list[_].num} - {self.object_list[_].name}": self.object_list[_].id for _ in
                            range(len(self.object_list))}
        combobox_obj_val += tuple(self.object_dict.keys())
        self.combobox_obj['values'] = combobox_obj_val
        # Очищаем таблицу
        self.main_table.delete(*self.main_table.get_children())
        # Составляем данные для отображения
        self.people_table = [(_.surname, _.name, _.patronymic, _.key) for _ in self.person_list]
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)

    def search_table_action(self):
        """
        Поиск по таблице
        :return:
        """
        # Очищаем таблицу
        self.main_table.delete(*self.main_table.get_children())
        # Заполняем данными удовлетворяющими критериям поиска
        # Если заполнено одно из полей
        if self.entry_surname.get() or self.entry_name or self.entry_patronymic or self.entry_hex:
            self.people_table = [(_.surname, _.name, _.patronymic, _.key) for _ in self.person_list
                                 if self.entry_surname.get().lower() in _.surname.lower()
                                 and self.entry_name.get().lower() in _.name.lower()
                                 and self.entry_patronymic.get().lower() in _.patronymic.lower()
                                 and self.entry_hex.get() in _.key
                                 and (self.object_main in _.permission.keys() or self.object_main == '000')]
        else:
            self.people_table = [(_.surname, _.name, _.patronymic, _.key) for _ in self.person_list
                                 if (self.object_main in _.permission.keys() or self.object_main == '000')]
        # Выводим данные в таблицу
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)

    def search_table(self):
        """
        Составляем интерфейс для поиска
        :return:
        """
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
        self.btn_entry.grid(row=1, column=4, sticky=tk.NW)

    def combobox_sort(self):
        """
        Создаем интерфейс для выбора Объекта
        :return:
        """
        # Создаем метку с описанием
        self.label_obj = ttk.Label(self.root, text="Выберите прибор:", background='white')
        self.label_obj.grid(row=0, column=0, sticky=tk.W)
        # Создаем выпадающий список
        combobox_obj_val = 'Все',
        self.object_dict = {f"{self.object_list[_].num} - {self.object_list[_].name}": self.object_list[_].id for _ in
                            range(self.object_list_len)}
        combobox_obj_val += tuple(self.object_dict.keys())
        self.combobox_obj_var = tk.StringVar(value=combobox_obj_val[0])
        self.combobox_obj = ttk.Combobox(self.root, textvariable=self.combobox_obj_var)
        self.combobox_obj.config(width=29)
        self.combobox_obj['values'] = combobox_obj_val
        # Запрещаем изменять элементы выпадающего списка
        self.combobox_obj['state'] = 'readonly'
        self.combobox_obj.grid(row=0, column=1, sticky=tk.W)
        # Создаем кнопку для взаимодействия
        self.combobox_btn = ttk.Button(self.root, text='Выбрать', command=self.combobox_btn_press)
        self.combobox_btn.grid(row=0, column=2)
        # Создаем кнопку для выгрузки
        self.export_btn = ttk.Button(self.root, text='Выгрузить', command=self.export_btn_press)
        self.export_btn.grid(row=0, column=3)
        # Если Объект не выбран, то деактивируем кнопку
        if self.object_main == "000":
            self.export_btn['state'] = 'disabled'

    def export_btn_press(self):
        """
        Обрабатываем нажатие на кнопку экспорта
        :return:
        """
        permission_list = []  # Список ключей и соответсвующих им прав
        # Проходим по всем персонам и выбираем данные соответствующие выбранному Объекту
        for _ in self.person_list:
            cur_perm = _.permission.get(self.object_main)
            if cur_perm:
                permission_list.append([_.key, cur_perm[2]])
        # Выбираем Объект по индексу и в зависимости от типа выгружаем
        for _ in self.object_list:
            if self.object_main == _.id:
                if _.type == '10':
                    sig10.write_key(_.num, permission_list)
                if _.type == '4':
                    c20004.write_key(_.num, permission_list)

    def combobox_btn_press(self):
        """
        Обрабатываем нажатие на кнопку выбора Объекта
        :return:
        """
        if self.combobox_obj_var.get() == "Все":
            self.object_main = "000"
            # Меняем свойства кнопки экспорта
            self.export_btn['state'] = 'disabled'
            self.export_btn['text'] = "Выгрузить"
        else:
            # Определяем выбранный Объект
            self.object_main = self.object_dict[self.combobox_obj_var.get()]
            # Включаем кнопку экспорта
            self.export_btn['state'] = 'enabled'
            for _ in self.object_list:
                if self.object_main == _.id:
                    self.export_btn['text'] = f"Выгрузить для {_.num}"
        # Обновляем данные для вывода Персон соответсвующих Объекту
        self.search_table_action()
