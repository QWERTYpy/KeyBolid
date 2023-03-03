import tkinter as tk
import saveloadini as sl
import main_menu as mm
import table as tbl
import info_frame as i_f


def on_closing():
    # Действия при закрытии окна
    print("Закрытие окна")
    root.destroy()  # Закрыть окно


# Основные переменные
object_list = sl.load_object_ini()  # Список объектов
person_list = sl.load_person_ini()  # Список персон
object_list_len = len(object_list)
# Создаем приложение
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title(("KeyBolid - v.1.0"))
root.geometry("824x608+10+10")  # Создаем окно
root.resizable(False, False)  # Запрещаем изменять размер окна
root.configure(background='#ffffff')  # Устанавливаем цвет фона
# Создаем инфополе
infoframe = i_f.InfoFrame(root)
# Создаем основную таблицу
table = tbl.Table(root, infoframe, object_list, person_list)# Создаем главное меню
main_menu = mm.MainMenu(root, table, infoframe, person_list, object_list)
# Запускаем отображение
root.mainloop()

