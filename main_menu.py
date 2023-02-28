# Верхнее меню
import tkinter as tk
import saveloadini as sl


class MainMenu:
    def __init__(self, root, info_frame, person_list):
        self.root = root
        self.info_frame = info_frame
        self.person_list = person_list
        self.main_menu = tk.Menu(self.root)
        self.main_menu.add_command(label="Сохранить", command=self.main_menu_save_object)
        self.root.config(menu=self.main_menu)

    def main_menu_save_object(self):
        sl.save_person_ini(self.person_list)
        self.info_frame.title_left_down_text.set("Сохранено")
