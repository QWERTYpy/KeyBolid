# Класс отвечающий за вывод Информационного поля
import tkinter as tk

class InfoFrame:
    def __init__(self, root):
        self.root = root
        self.title_left_down_text = tk.StringVar()
        self.title_left_down_text.set("Добро пожаловать ...")
        self.title_left_down = tk.Label(self.root, anchor="nw", height=1, width=20,
                                        textvariable=self.title_left_down_text, background='white')
        self.title_left_down.grid(row=27, column=0)

