# Класс описывающий интерфейс Сигнал10
from tkinter import ttk
import tkinter as tk
from person import Person
class Signal10:
    def __init__(self, root,person_cur: Person, obj):
        self.root = root
        ttk.Label(self.root, text="Шлейф").place(x=0,y=130)
        for _ in range(10):
            ttk.Label(self.root, text=f"{_+1}",width=4, justify=tk.CENTER).place(x=f"{70+_*30}", y=130)
        ttk.Label(self.root, text="Взятие").place(x=0, y=160)
        ttk.Label(self.root, text="Снятие").place(x=0, y=190)
        self.checkbox_list = person_cur.get_check_10(obj)
        # for _ in range(20):
        #     print(self.checkbox_list[_].get())
        i = -1
        for _ in range(10):
            i += 1
            # self.checkbox_list.append(tk.IntVar())
            ttk.Checkbutton(self.root, variable=self.checkbox_list[i]).place(x=f"{70+_*30}", y=190)
            i += 1
            # self.checkbox_list.append(tk.IntVar())
            ttk.Checkbutton(self.root, variable=self.checkbox_list[i]).place(x=f"{70 + _ * 30}", y=160)

    def get_checkbox(self):
        return self.checkbox_list


