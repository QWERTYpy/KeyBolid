import tkinter as tk
from tkinter import ttk
from person import Person
import object
from bolid_perm import Signal10, C2000_4
# Всплывающее меню при создании или редактировании информации о объекте
class FramePerson(tk.Toplevel):
    def __init__(self, parent, key, object, person_list, object_list):
        super().__init__(parent)
        self.key = key
        self.object = object
        self.person_list = person_list
        self.object_list = object_list
        # self.checkbox_list = []
        self.object_cur = ''
        for __ in self.object_list:
            if __.id == self.object:
                self.object_cur = __
        for _ in self.person_list:
            # print(type(_.key), type(self.key))
            if _.key == self.key:
                self.person_cur = _
        if not self.key:
            self.person_cur = Person()
            # self.person_list.append(Person())
            # self.person_cur = self.person_list[-1]
            self.person_cur.permission[self.object_cur.id] = [self.object_cur.num, '000000', '000000']

        self.create_frame()
        if self.key:
            self.filling_person()
        if self.object_cur.type == '4':
            self.bolid_4(self.object_cur)
        if self.object_cur.type == '10':
            self.bolid_10(self.object_cur)
        self.flag_change = False
        self.btn_save = ttk.Button(self, text='Сохранить', command=self.click_btn_save)
        self.btn_save.place(x=300,y=340)
        # self.btn_save.grid(row=10, column=10)


    def filling_person(self):
        self.entry_name.insert(0,self.person_cur.name)
        self.entry_surname.insert(0,self.person_cur.surname)
        self.entry_patr.insert(0,self.person_cur.patronymic)
        self.entry_hex.insert(0,self.person_cur.key)

    def bolid_4(self, obj: object.ObjectBolid):
        ttk.Label(self, text="Настройка:").place(x=0, y=90)
        if obj.type == '4':
            obj_type = 'C2000-4'
        ttk.Label(self, text=obj_type).place(x=100, y=90)
        ttk.Label(self, text=obj.name).place(x=200, y=90)

        self.object_c2000_4 = C2000_4(self, self.person_cur, obj.id)
        self.obj_text = tk.Text(self, width=44, height=4)
        self.obj_text.place(x=10, y=230)
        self.obj_text.insert(1.0, obj.comment)
        self.obj_text.configure(state=tk.DISABLED)


    def bolid_10(self, obj: object.ObjectBolid):
        ttk.Label(self, text="Настройка:").place(x=0, y=90)
        if obj.type == '10':
            obj_type = 'Сигнал10'
        ttk.Label(self, text=obj_type).place(x=100, y=90)
        ttk.Label(self, text=obj.name).place(x=200, y=90)
        self.object_signl10 = Signal10(self,self.person_cur, obj.id)
        self.obj_text = tk.Text(self, width=44, height=4)
        self.obj_text.place(x=10, y=230)
        self.obj_text.insert(1.0, obj.comment)
        self.obj_text.configure(state=tk.DISABLED)

        # checkbox_list.append(tk.IntVar())
        # checkbox_list[i].set(1)

        # ttk.Label(self, text="Шлейф").place
        # for _ in range(10):
        #     ttk.Label(self, text=f"{_+1}",width=4, background='white').grid(row=5, column=f"{3+_}")

    def create_frame(self):
        self.label_surname = ttk.Label(self, text="Фамилия:")
        self.label_surname.place(x=0,y=0)
        # self.label_surname.grid(row=0, column=0, columnspan=5, sticky='w')
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=100, y=0)

        self.label_name = ttk.Label(self, text="Имя:")
        # self.label_name.grid(row=1, column=0, columnspan=5, sticky='w')
        self.label_name.place(x=0, y=20)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=100,y=20)
        # self.entry_name.grid(row=1, column=5)
        # # self.entry_name.insert(0,"333")
        #
        self.label_patr = ttk.Label(self, text="Отчество:")
        self.label_patr.place(x=0,y=40)
        # self.label_patr.grid(row=2, column=0, columnspan=5,sticky='w')
        self.entry_patr = ttk.Entry(self)
        self.entry_patr.place(x=100,y=40)
        # self.entry_patr.grid(row=2, column=5, columnspan=5)
        #
        self.label_hex = ttk.Label(self, text="Ключ:")
        self.label_hex.place(x=0,y=60)
        # self.label_hex.grid(row=3, column=0, columnspan=5, sticky='w')
        self.entry_hex = ttk.Entry(self)
        self.entry_hex.place(x=100, y=60)
        # self.entry_hex.grid(row=3, column=5, columnspan=5)



    def click_btn_save(self):
        flag_dubl = False
        for _ in self.person_list:
            if _.key.upper() == self.entry_hex.get():
                print(f'Обнаружен дубликат ключа: {_.key.upper()}')
                flag_dubl = True

        if not flag_dubl:
            self.flag_change = True

            self.person_cur.name = self.entry_name.get()
            self.person_cur.surname = self.entry_surname.get()
            self.person_cur.patronymic = self.entry_patr.get()
            self.person_cur.key = self.entry_hex.get()
            if self.object_cur.type == '10':
                self.person_cur.permission[self.object_cur.id][2] = self.person_cur.convert_check_10(self.object_signl10.get_checkbox())
            if self.object_cur.type == '4':
                self.person_cur.permission[self.object_cur.id][2] = self.person_cur.convert_check_4(self.object_c2000_4.get_checkbox(),self.object_c2000_4.get_perm())
            self.person_list.append(self.person_cur)
            # self.person_cur = self.person_list[-1]
            # self.person_cur.permission[self.object_cur.id] = [self.object_cur.num, '000000', '000000']