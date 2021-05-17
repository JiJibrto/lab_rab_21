#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
from random import random


def rand_spawn():
    new_x = random()
    new_y = random()
    btn_1.place(relx=new_x, rely=new_y)

root = Tk()
root['bg'] = 'white'
root.title('AMOGUS')
root.geometry('1000x1000')
img = PhotoImage(file='amogus.png')

btn_1 = Button(image=img, bg='white', borderwidth=0,
             activebackground='white', command=rand_spawn)
btn_1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
