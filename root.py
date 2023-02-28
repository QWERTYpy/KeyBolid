import tkinter as tk
import saveloadini as sl
import main_menu as mm
import table as tbl


def on_closing():
    # Действия при закрытии окна
    print("Закрытие окна")
    root.destroy()  # Закрыть окно


# Основные переменные
object_list = sl.load_object_ini()
object_list_len = len(object_list)
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title(("KeyBolid - v.1.0"))
root.geometry("800x608+10+10")  # Создаем окно
root.resizable(False, False)  # Запрещаем изменять размер окна
root.configure(background='#ffffff')  # Устанавливаем цвет фона
# Создаем главное меню
main_menu = mm.MainMenu(root)
# Создаем основную таблицу
table = tbl.Table(root, object_list)
# Запускаем отображение
root.mainloop()

