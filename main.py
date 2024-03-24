import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
# Функция для проверки ввода
def validate_entry(entry):
    if not entry.strip():
        return False
    return True

# Функция для добавления новой записи
def add_entry():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    # Проверка ввода
    if not validate_entry(website) or not validate_entry(login) or not validate_entry(password):
        mb.showerror("Ошибка", "Все поля должны быть заполнены!")
        return

    # Добавление записи в таблицу
    table.insert("", "end", values=(website, login, password))

# Функция для сохранения данных
def save_data():
    filename = fd.asksaveasfilename(title="Сохранить пароль", defaultextension=".csv")
    if not filename:
        return

    # Сохранение данных в файл
    with open(filename, "w") as f:
        f.write("Сайт,Логин,Пароль\n")
        for row in table.get_children():
            item = table.item(row)
            values = item["values"]
            f.write(",".join(values) + "\n")

    mb.showinfo("Успешно", "Данные сохранены!")

# Создание окна
window = tk.Tk()
window.title("Kpass")

# Создание элементов интерфейса
website_label = tk.Label(text="Сайт:")
website_entry = tk.Entry()

login_label = tk.Label(text="Логин:")
login_entry = tk.Entry()

password_label = tk.Label(text="Пароль:")
password_entry = tk.Entry(show="*")

add_button = tk.Button(text="Добавить", command=add_entry)
save_button = tk.Button(text="Сохранить", command=save_data)

# Создание таблицы
table = ttk.Treeview(window, columns=("Сайт", "Логин", "Пароль"))
table.heading("Сайт", text="Сайт")
table.heading("Логин", text="Логин")
table.heading("Пароль", text="Пароль")

# Размещение элементов
website_label.grid(row=0, column=0)
website_entry.grid(row=0, column=1)

login_label.grid(row=1, column=0)
login_entry.grid(row=1, column=1)

password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)

add_button.grid(row=3, column=0)
save_button.grid(row=3, column=1)

table.grid(row=4, column=0, columnspan=2)

# Запуск окна
window.mainloop()

