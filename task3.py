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
text = Text(width=50, height=25)
text.grid(columnspan=3)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1)
b3 = Button(text="Очистить", command=del_txt)
b3.grid(row=1, column=2, sticky=W)
root.mainloop()
