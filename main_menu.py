# Верхнее меню
import tkinter as tk
import saveloadini as sl
from tkinter import filedialog
from  frame_object import FrameObject
import binascii
import re



class MainMenu:
    def __init__(self, root, info_frame, person_list, object_list):
        self.root = root
        self.info_frame = info_frame
        self.person_list = person_list
        self.object_list = object_list
        self.open_object = 0
        self.main_menu = tk.Menu(self.root)
        self.main_menu.add_command(label="Сохранить", command=self.main_menu_save_object)
        self.main_menu.add_command(label="Загрузить", command=self.main_menu_load_object)
        self.root.config(menu=self.main_menu)

    def main_menu_save_object(self):
        sl.save_person_ini(self.person_list)
        sl.save_object_ini(self.object_list)
        self.info_frame.title_left_down_text.set("Сохранено")

    def main_menu_load_object(self):
        self.info_frame.title_left_down_text.set("Выберите файл")
        self.flag_add = False
        filepath = filedialog.askopenfilename()
        line_cursor=1
        if filepath != "":
            file = open(filepath, 'rb')
            for line in file:
                if line_cursor == 1:
                    line_cursor += 1
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
                        self.info_frame.title_left_down_text.set("Добавление нового Объекта.")
                        # if type_obj == "Signal-10":

                        frame_object = FrameObject(self.root, type_obj, ver, self.open_object, self.object_list)
                        frame_object.geometry("260x250+50+50")
                        frame_object.title('Добавление нового Объекта')
                        frame_object.grab_set()
                        frame_object.wait_window()

                        # if type_obj == 'S2000-4':
                        #     pass
                # print(line.decode('ansi'))
                # print(binascii.hexlify(line))
            file.close()