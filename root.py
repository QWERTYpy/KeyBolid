import tkinter as tk
import saveloadini as sl
import main_menu as mm
import table as tbl
import info_frame as i_f
from tkinter import messagebox as mb
# 4.1.6.12290 UProg


def on_closing():
    # Действия при закрытии окна
    # print("Закрытие окна")

    # answer = mb.askyesno(
    #     title="Обнаружены изменения",
    #     message="Сохранить данные?")
    # print(answer)
    flag_change = False
    flag_change = table.flag_change or main_menu.flag_change
    #     flag_change = False
    # print(flag_change)
    if flag_change:
        answer = mb.askyesno(
                title="Обнаружены изменения",
                message="Сохранить данные?")
    if flag_change and answer:
        sl.save_person_ini(person_list)
    root.destroy()  # Закрыть окно


# Основные переменные
object_list = sl.load_object_ini()  # Список объектов
person_list = sl.load_person_ini()  # Список персон
object_list_len = len(object_list)
# Создаем приложение
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title(("KeyBolid - v.1.3.3"))
root.geometry("840x600+10+10")  # Создаем окно
root.resizable(False, False)  # Запрещаем изменять размер окна
root.configure(background='#ffffff')  # Устанавливаем цвет фона
# Создаем инфополе
infoframe = i_f.InfoFrame(root)
# Создаем основную таблицу
table = tbl.Table(root, infoframe, object_list, person_list)# Создаем главное меню
main_menu = mm.MainMenu(root, table, infoframe, person_list, object_list)
# Запускаем отображение
root.mainloop()

