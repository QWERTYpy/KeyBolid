import tkinter as tk


def on_closing():
    # Действия при закрытии окна
    print("Закрытие окна")
    root.destroy()  # Закрыть окно




root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title(("KeyBolid - v.1.0"))
root.geometry("1210x608+100+100")  # Создаем окно
root.resizable(False, False)  # Запрещаем изменять размер окна
root.configure(background='#ffffff')  # Устанавливаем цвет фона

# Меню
def main_menu_save_object():
    print("Сохранить")

main_menu =tk.Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="Сохранить", command=main_menu_save_object)


# - Меню


root.mainloop()  # Запускаем отображение