#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
import ind_mod as module
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import logging

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.

# Выполнить индивидуальное задание 2 лабораторной работы 13, добавив возможность работы с
# исключениями и логгирование.


def add_wind():
    def add_work():
        las_name = str(ent_1.get())
        name = str(ent_2.get())
        phone = str(ent_3.get())
        date_inp = str(ent_4.get())
        date = list(map(int, date_inp.split('.')))
        staff.add(las_name, name, phone, date)
        added_window.destroy()
        mb.showinfo('Успешно', 'Сотрудник добавлен в список')
        show()
        logging.info(
            f"\nДобавлен сотрудник: {las_name}, {name}"
            f"\nНомер телефона {phone}"f""
            f"\nДата рождения {date[0]}.{date[1]}.{date[2]}"
        )

    added_window = Toplevel()
    added_window.title('Добавить человека')
    added_window.resizable(False, False)
    lab_1 = LabelFrame(added_window, text='Фамилия')
    lab_2 = LabelFrame(added_window, text='Имя')
    lab_3 = LabelFrame(added_window, text='Номер телефона')
    lab_4 = LabelFrame(added_window, text='Дата рождения')
    ent_1 = Entry(lab_1)
    ent_2 = Entry(lab_2)
    ent_3 = Entry(lab_3)
    ent_3.insert(0, '+7')
    ent_4 = Entry(lab_4)
    ent_4.insert(0, 'ДД.MM.ГГГГ')
    btn_1 = Button(added_window, text='Добавить', command=add_work)

    lab_1.pack(side=LEFT)
    lab_2.pack(side=LEFT)
    lab_3.pack(side=LEFT)
    lab_4.pack(side=LEFT)
    ent_1.pack(side=LEFT)
    ent_2.pack(side=LEFT)
    ent_3.pack(side=LEFT)
    ent_4.pack(side=LEFT)
    btn_1.pack(side=LEFT)


def load_wind():
    try:
        file_name = fd.askopenfilename()
        staff.load(file_name)
        show()
        logging.info(f"Загружены данные из файла {file_name}.")
    except():
        mb.showinfo("Ошибка",
                    "Файл не выбран!")


def save_wind():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("XML files", "*.xml"),
                       ("All files", "*.*")))
        staff.save(file_name)
        show()
        logging.info(f"Сохраннены данные в файл {file_name}.")
    except():
        mb.showinfo("Ошибка",
                    "Файл не выбран!")


def show():
    text.delete(0.0, END)
    text.insert(0.0, staff)


if __name__ == '__main__':
    logging.basicConfig(
        filename='workers.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )
    staff = module.Staff()

    root = Tk()
    root.geometry('800x500')
    root.title('Справочник по людям')

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label='Открыть', command=load_wind)
    file_menu.add_command(label='Сохранить', command=save_wind)
    file_menu.add_command(label='Закрыть', command=lambda: root.destroy())

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_command(label="Добавить", command=add_wind)
    main_menu.add_command(label="Показать", command=show)
    main_menu.add_command(label="Очистить", command=lambda: text.delete(0.0, END))

    text = Text(bg='white', width=97, height=100)
    text.pack(side=LEFT)
    scr = Scrollbar(command=text.yview)
    scr.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scr.set)

    root.mainloop()
