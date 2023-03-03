# Верхнее меню
import tkinter as tk
import saveloadini as sl
import crc8bolid as crc
import frame_person as fp
from tkinter import filedialog
from  frame_object import FrameObject
from person import Person
import binascii
import re



class MainMenu:
    def __init__(self, root, table, info_frame, person_list, object_list):
        self.root = root
        self.table = table
        self.info_frame = info_frame
        self.person_list = person_list
        self.object_list = object_list
        self.open_object = 0
        self.main_menu = tk.Menu(self.root)
        self.main_menu.add_command(label="Сохранить", command=self.main_menu_save_object)
        self.main_menu.add_command(label="Загрузить", command=self.main_menu_load_object)
        self.main_menu.add_command(label="Добавить", command=self.main_menu_load_person)
        self.main_menu.add_command(label="Удалить", command=self.main_menu_delete_person)
        self.root.config(menu=self.main_menu)

    def main_menu_delete_person(self):
        if self.table.object_main == '000':
            self.info_frame.title_left_down_text.set("Выбирете Объект")
        else:
            select_person = str(self.table.main_table.item(self.table.main_table.selection())['values'][3])
            for _ in self.person_list:
                if _.key == select_person:
                    _.permission.pop(self.table.object_main)
            self.table.search_table_action()


    def main_menu_load_person(self):
        if self.table.object_main == '000':
            self.info_frame.title_left_down_text.set("Выбирете Объект")
        else:

            frame_person = fp.FramePerson(self.root, '', self.table.object_main, self.person_list, self.object_list)

            # descr.geometry(f"200x180+{self.position_cursor_old_x + int(x) + 10}+{self.position_cursor_old_y + int(y)}")
            frame_person.geometry("400x400+50+50")
            frame_person.title('Редактирование доступа')
            frame_person.grab_set()
            frame_person.wait_window()
            if frame_person.flag_change:
                self.table.search_table_action()

    def main_menu_save_object(self):
        sl.save_person_ini(self.person_list)
        sl.save_object_ini(self.object_list)
        self.info_frame.title_left_down_text.set("Сохранено")

    def main_menu_load_object(self):
        self.info_frame.title_left_down_text.set("Выберите файл")
        self.flag_add = False
        flag_key_add = False
        filepath = filedialog.askopenfilename()
        line_cursor = 0
        buffer_str = b''
        cursor_str = False
        if filepath != "":
            file = open(filepath, 'rb')
            for line in file:
                line_cursor += 1
                if line_cursor == 1:
                    math = re.search(r'Keys.*v.\d.\d\d', line.decode('ansi'))
                    _, type_obj, ver = math[0].split(' ')
                    # print(name,ver)
                    self.open_object = re.search(r'\d{1,3}.ki', filepath)[0][:-3]
                    for _ in self.object_list:
                        if self.open_object == _.num:
                            self.info_frame.title_left_down_text.set("Объект уже присутствует в базе.")
                            self.flag_add = True
                            break
                    if not self.flag_add:
                        self.info_frame.title_left_down_text.set("Добавление Объекта.")
                        frame_object = FrameObject(self.root, type_obj, ver, self.open_object, self.object_list)
                        frame_object.geometry("260x250+50+50")
                        frame_object.title('Добавление нового Объекта')
                        frame_object.grab_set()
                        frame_object.wait_window()
                self.info_frame.title_left_down_text.set(f"Загрузка строк - {line_cursor}.")

                if len(binascii.hexlify(line)) == 48:
                    cursor_str = True
                    continue
                if cursor_str:
                    buffer_str += line

                    if type_obj == "Signal-10" and len(binascii.hexlify(buffer_str)) == 304 or len(binascii.hexlify(buffer_str)) == 262:
                        cursor_str = False
                        self.file_key = crc.reverse_key(binascii.hexlify(buffer_str)[242:254])
                        self.file_perm = binascii.hexlify(buffer_str)[256:262]
                        buffer_str = b''
                        flag_key_add = True

                    if type_obj == 'S2000-4' and len(binascii.hexlify(buffer_str)) == 346 or len(binascii.hexlify(buffer_str)) == 276:
                        cursor_str = False

                        self.file_key = crc.reverse_key(binascii.hexlify(buffer_str)[214:226])
                        self.file_perm = binascii.hexlify(buffer_str)[228:234]
                        buffer_str = b''
                        flag_key_add = True

                # if line_cursor in list(range(4, 2000, 3)):
                #     # print(len(binascii.hexlify(line)), binascii.hexlify(line))
                #     if type_obj == "Signal-10":
                #         self.file_key = crc.reverse_key(binascii.hexlify(line)[242:254])
                #         self.file_perm = binascii.hexlify(line)[256:262]
                #     if type_obj == 'S2000-4':
                #         self.file_key = crc.reverse_key(binascii.hexlify(line)[214:226])
                #         self.file_perm =binascii.hexlify(line)[228:234]
                if flag_key_add:
                    # flag_key_add = False
                    self.file_key = self.file_key.decode('ansi')
                    self.file_perm = self.file_perm.decode('ansi')
                    for _ in self.person_list:
                        if _.key == self.file_key:
                            self.info_frame.title_left_down_text.set("Такой ключ существует")
                            if frame_object.new_object:
                               _.permission[frame_object.new_object.id] = [frame_object.new_object.num,
                                                                                     '000000', self.file_perm]
                            flag_key_add = False
                            continue
                    if flag_key_add:
                        self.info_frame.title_left_down_text.set("Добавление ключа")
                        new_person = Person()
                        new_person.name = ''  # Имя
                        new_person.surname = ''  # Фамилия
                        new_person.patronymic = ''  # Отчество
                        new_person.key = self.file_key  # Ключ
                        if frame_object.new_object:
                            new_person.permission[frame_object.new_object.id] = [frame_object.new_object.num, '000000', self.file_perm]  # Права доступа # id: [Номер прибора, ХО, Доступ]
                        self.person_list.append(new_person)
                        flag_key_add = False
            # self.table.search_table_action()
            self.table.reboot_table()


            file.close()
