# Класс отвечающий за вывод основной таблицы данных
from tkinter import ttk
import tkinter as tk
import frame_person as fp
import c20004
import sig10


class Table:
    def __init__(self, root, info_frame, object_list, person_list):
        self.flag_change = False
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
        table_column = ('surname', 'name', 'patronymic', 'hex_key', 'permission')
        # Создаем таблицу
        self.main_table = ttk.Treeview(self.root, columns=table_column, show='headings')
        self.main_table.place(x=10, y=70)
        # Определяем заголовки
        self.main_table.heading('name', text='Имя', anchor=tk.W)
        self.main_table.heading('surname', text='Фамилия', anchor=tk.W)
        self.main_table.heading('patronymic', text='Отчество', anchor=tk.W)
        self.main_table.heading('hex_key', text='Ключ', anchor=tk.W)
        self.main_table.heading('permission', text='Приборы', anchor=tk.W)
        # Определяем ширину столбцов
        self.main_table.column("#1", stretch=tk.NO, width=150)
        self.main_table.column("#2", stretch=tk.NO, width=150)
        self.main_table.column("#3", stretch=tk.NO, width=150)
        self.main_table.column("#4", stretch=tk.NO, width=150)
        self.main_table.column("#5", stretch=tk.NO, width=200)
        # Добавляем прокрутку
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.main_table.yview)
        self.main_table.configure(yscroll=self.scrollbar.set, height=20)
        self.scrollbar.place(relx=1.0, relheight=1.0, in_=self.main_table, bordermode='outside')
        # Составляем данные для отображения
        self.people_table = [(_.surname, _.name, _.patronymic, _.key, _.get_perm_obj()) for _ in self.person_list]
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)
        self.info_frame.title_left_down_text.set(f"Найдено {len(self.people_table)} записей")
        # Определяем действие двойного щелчка по полю
        self.main_table.bind("<Double-Button-1>", self.left_button_double)

    def left_button_double(self, event):
        # Если ничего не выбрано
        if self.object_main == '000':
            return False
        # Если выбран Объект открываем дочернее окно
        self.frame_person = fp.FramePerson(self.root, str(self.main_table.item(self.main_table.selection())['values'][3]),
                                      self.object_main,
                                      self.person_list,
                                      self.object_list)

        self.frame_person.geometry("400x400+50+50")
        self.frame_person.title('Редактирование доступа')
        self.frame_person.grab_set()
        self.frame_person.wait_window()
        # Обновляем вывод в таблице
        if self.frame_person.flag_change:
            self.search_table_action()
        self.flag_change = self.flag_change or self.frame_person.flag_change

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
        self.people_table = [(_.surname, _.name, _.patronymic, _.key, _.get_perm_obj()) for _ in self.person_list]
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)
        self.info_frame.title_left_down_text.set(f"Найдено {len(self.people_table)} записей")

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
            self.people_table = [(_.surname, _.name, _.patronymic, _.key, _.get_perm_obj()) for _ in self.person_list
                                 if self.entry_surname.get().lower() in _.surname.lower()
                                 and self.entry_name.get().lower() in _.name.lower()
                                 and self.entry_patronymic.get().lower() in _.patronymic.lower()
                                 and self.entry_hex.get().upper() in _.key.upper()
                                 and (self.object_main in _.permission.keys() or self.object_main == '000')]
        else:
            self.people_table = [(_.surname, _.name, _.patronymic, _.key, _.get_perm_obj()) for _ in self.person_list
                                 if (self.object_main in _.permission.keys() or self.object_main == '000')]
        # Выводим данные в таблицу
        for person in self.people_table:
            self.main_table.insert("", tk.END, values=person)
        self.info_frame.title_left_down_text.set(f"Найдено {len(self.people_table)} записей")


    def search_table(self):
        """
        Составляем интерфейс для поиска
        :return:
        """
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.config(width=23)
        self.entry_name.place(x=160, y=40)

        self.entry_surname = ttk.Entry(self.root)
        self.entry_surname.config(width=23)
        self.entry_surname.place(x=10, y=40)

        self.entry_patronymic = ttk.Entry(self.root)
        self.entry_patronymic.config(width=23)
        self.entry_patronymic.place(x=310, y=40)

        self.entry_hex = ttk.Entry(self.root)
        self.entry_hex.config(width=23)
        self.entry_hex.place(x=460, y=40)

        self.btn_entry = ttk.Button(self.root, text='Искать ...', command=self.search_table_action, width=10)
        self.btn_entry.place(x=610, y=38)

    def combobox_sort(self):
        """
        Создаем интерфейс для выбора Объекта
        :return:
        """
        # Создаем метку с описанием
        self.label_obj = ttk.Label(self.root, text="Выберите прибор:", background='white')
        self.label_obj.place(x=10, y=10)
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
        self.combobox_obj.place(x=150, y=10)
        # Создаем кнопку для взаимодействия
        self.combobox_btn = ttk.Button(self.root, text='Выбрать', command=self.combobox_btn_press)
        self.combobox_btn.place(x=360, y=9)
        # Создаем кнопку для выгрузки
        self.export_btn = ttk.Button(self.root, text='Выгрузить', command=self.export_btn_press)
        self.export_btn.place(x=450, y=9)
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
