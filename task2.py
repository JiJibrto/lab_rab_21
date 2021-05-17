#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

# Напишите программу, в которой на главном окне находятся холст и кнопка
# "Добавить фигуру". Кнопка открывает второе окно, включающее четыре поля для ввода
# координат и две радиокнопки для выбора, рисовать ли на холсте прямоугольник или овал.
# Здесь же находится кнопка "Нарисовать", при клике на которую соответствующая фигура
# добавляется на холст, а второе окно закрывается. Проверку корректности ввода в поля
# можно опустить.

# Перепрограммируйте второе окно из п. 7, используя метод grid .

class Main_prog:
    def __init__(self, master, function):
        self.main_canv = Canvas(master, width=500, height=500, bg='white')
        self.btn_1 = Button(master, text='Добавить фигуру')
        self.btn_1['command'] = eval('self.' + function)

        self.main_canv.pack()
        self.btn_1.pack()

    def new_window(self):
        opt_wndw = Toplevel()
        opt_wndw.title("Меню создания")
        opt_wndw.resizable(False, False)
        opt_wndw.geometry('130x125')

        f_x_1 = Label(opt_wndw, text="X1")
        f_y_1 = Label(opt_wndw, text="Y1")
        f_x_2 = Label(opt_wndw, text="X2")
        f_y_2 = Label(opt_wndw, text="Y2")

        ent_x1 = Entry(opt_wndw, width=5)
        ent_y1 = Entry(opt_wndw, width=5)
        ent_x2 = Entry(opt_wndw, width=5)
        ent_y2 = Entry(opt_wndw, width=5)

        def draw_ob(event):
            x_1 = int(ent_x1.get())
            y_1 = int(ent_y1.get())
            x_2 = int(ent_x2.get())
            y_2 = int(ent_y2.get())
            if temp_var.get():
                self.main_canv.create_oval(x_1, y_1, x_2, y_2, width=2)
            else:
                self.main_canv.create_rectangle(x_1, y_1, x_2, y_2, width=2)

        temp_var = BooleanVar()
        temp_var.set(False)
        rad_oval = Radiobutton(opt_wndw, text="Овал", variable=temp_var, value=True)
        rad_rect = Radiobutton(opt_wndw, text="Прямоугольник", variable=temp_var, value=False)
        btn_creat = Button(opt_wndw, text="Нарисовать")
        btn_creat.bind("<Button-1>", draw_ob)

        f_x_1.grid(row=0, column=0)
        ent_x1.grid(row=0, column=1)
        f_y_1.grid(row=0, column=2)
        ent_y1.grid(row=0, column=3)
        f_x_2.grid(row=1, column=0)
        ent_x2.grid(row=1, column=1)
        f_y_2.grid(row=1, column=2)
        ent_y2.grid(row=1, column=3)
        rad_oval.grid(row=2, column=0, columnspan=4, sticky=W)
        rad_rect.grid(row=3, column=0, columnspan=4, sticky=W)
        btn_creat.grid(row=4, column=0, columnspan=4)


if __name__ == '__main__':
    root = Tk()
    root.title("Холст для рисования")
    main_prog = Main_prog(root, 'new_window')
    root.mainloop()
