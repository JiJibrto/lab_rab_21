#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

# Напишите программу, в которой на главном окне находятся холст и кнопка
# "Добавить фигуру". Кнопка открывает второе окно, включающее четыре поля для ввода
# координат и две радиокнопки для выбора, рисовать ли на холсте прямоугольник или овал.
# Здесь же находится кнопка "Нарисовать", при клике на которую соответствующая фигура
# добавляется на холст, а второе окно закрывается. Проверку корректности ввода в поля
# можно опустить.

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
        opt_wndw.geometry('300x100')

        header_1 = LabelFrame(opt_wndw, text="X1 Y1")
        header_2 = LabelFrame(opt_wndw, text="X2 Y2")
        bottom_1 = LabelFrame(opt_wndw)

        ent_x1 = Entry(header_1, width=20)
        ent_y1 = Entry(header_1, width=20)
        ent_x2 = Entry(header_2, width=20)
        ent_y2 = Entry(header_2, width=20)

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
        rad_oval = Radiobutton(bottom_1, text="Овал", variable=temp_var, value=True)
        rad_rect = Radiobutton(bottom_1, text="Прямоугольник", variable=temp_var, value=False)
        btn_creat = Button(bottom_1, text="Нарисовать")
        btn_creat.bind("<Button-1>", draw_ob)

        header_1.pack(side=TOP)
        header_2.pack(side=TOP)
        bottom_1.pack(side=TOP)
        ent_x1.pack(side=LEFT)
        ent_y1.pack(side=LEFT)
        ent_x2.pack(side=LEFT)
        ent_y2.pack(side=LEFT)
        rad_oval.pack(side=LEFT)
        rad_rect.pack(side=LEFT)
        btn_creat.pack(side=BOTTOM)


if __name__ == '__main__':
    root = Tk()
    root.title("Холст для рисования")
    main_prog = Main_prog(root, 'new_window')
    root.mainloop()

