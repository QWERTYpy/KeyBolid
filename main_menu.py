# Верхнее меню
import tkinter as tk


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.main_menu = tk.Menu(self.root)
        self.main_menu.add_command(label="Сохранить", command=self.main_menu_save_object)
        self.root.config(menu=self.main_menu)

    def main_menu_save_object(self):
        print("Сохранить")
