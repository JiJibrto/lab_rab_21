#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

# в приведенной в лабораторной работе программе с функциями
# askopenfilename и asksaveasfilename генерируются исключения, если диалоговые окна
# были закрыты без выбора или указания имени файлов. Напишите код обработки данных
# исключений. При этом для пользователя должно появляться информационное диалоговое
# окно с сообщением о том, что файл не загружен или не сохранен. Добавьте кнопку
# "Очистить", которая удаляет текст из поля. Перед удалением пользователь должен
# подтвердить свои намерения через соответствующее диалоговое окно.



def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except(FileNotFoundError, TypeError):
        mb.showinfo("Ошибка!", "Файл не открыт \nПопробуйте еще раз")


def extract_text():
    file_name = fd.asksaveasfilename(
    filetypes=(("TXT files", "*.txt"),
               ("HTML files", "*.html;*.htm"),
               ("All files", "*.*")))
    try:
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except(FileNotFoundError, TypeError):
        mb.showinfo("Ошибка!", "Файл не сохранен \nПопробуйте еще раз")


def del_txt():
    qustn = mb.askyesno('', 'Вы действительно хотите удалить данные?')
    if qustn:
        text.delete(0.0, END)


root = Tk()

header_menu = Menu(root)
root['menu'] = header_menu
header_menu.add_command(label="Открыть", command=insert_text)
header_menu.add_command(label="Сохранить", command=extract_text)

text = Text(width=50, height=25)
text.pack()

cont_menu = Menu(text, tearoff=0)
cont_menu.add_command(label="Очистить", command=del_txt)

text.bind('<Button-3>', lambda temp: cont_menu.post(temp.x_root, temp.y_root))

root.mainloop()
