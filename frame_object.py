import tkinter as tk
from tkinter import ttk
from object import ObjectBolid
import object
from bolid_perm import Signal10, C2000_4
# Всплывающее меню при создании или редактировании информации о объекте
class FrameObject(tk.Toplevel):
    def __init__(self, parent, type_object, ver, open_object, object_list):
        super().__init__(parent)
        self.type_object = type_object
        self.ver = ver
        self.open_object = open_object
        self.object_list = object_list
        self.create_frame()
        self.flag_change = False
        self.new_object = None

    def create_frame(self):
        self.label_num = ttk.Label(self, text="Номер:")
        self.label_num.place(x=0, y=0)
        self.entry_num = ttk.Entry(self)
        self.entry_num.place(x=100, y=0)
        self.entry_num.insert(0, self.open_object)

        self.label_name = ttk.Label(self, text="Наименование:")
        self.label_name.place(x=0, y=20)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=100, y=20)

        self.label_type = ttk.Label(self, text="Тип:")
        self.label_type.place(x=0, y=40)
        self.entry_type = ttk.Entry(self)
        self.entry_type.place(x=100, y=40)
        self.entry_type.insert(0, self.type_object)

        self.interface = tk.IntVar()
        self.chk_interface = ttk.Checkbutton(self, variable=self.interface, text='Touch Memory')
        self.chk_interface.place(x=0, y=60)

        self.label_desc = ttk.Label(self, text="Описание:")
        self.label_desc.place(x=0, y=80)
        self.obj_text = tk.Text(self, width=30, height=5)
        self.obj_text.place(x=10, y=100)

        self.btn_save = ttk.Button(self, text='Сохранить', command=self.click_btn_save)
        self.btn_save.place(x=150, y=200)



    def click_btn_save(self):
        self.flag_change = True
        index_object = []
        for _ in self.object_list:
            index_object.append(_.id)
        index_list = ['{:03}'.format(_) for _ in range(1,999)]
        for _ in index_list:
            if _ in index_object:
                continue
            obj = ObjectBolid()
            obj.id = _
            obj.num = self.entry_num.get()
            obj.name = self.entry_name.get()
            if self.type_object == 'Signal-10':
                obj.type = '10'
                obj.interface = self.interface.get()
            if self.type_object == 'S2000-4':
                obj.type = '4'
                obj.interface = 0
            obj.ver = self.ver

            obj.comment = self.obj_text.get("1.0",tk.END)
            self.new_object = obj
            self.object_list.append(obj)
            break