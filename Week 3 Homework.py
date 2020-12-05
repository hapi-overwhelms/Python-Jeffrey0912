# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:25:42 2020

@author: John Kao
"""
#Below are the setup lines
import tkinter as tk
import tkinter as tk 
window = tk.Tk()
window.title("Soul releaser.exe (free version)")
window.geometry = ('500x227')
string = tk.StringVar()
#Functions below
def selection():
    label.config(text="300 Freemium Pack" + string.get())
label = tk.Label(window, bg='#f00', text = 'no')
label.pack()
radio1 = tk.Radiobutton(window, text = 'Minecraft Python', variable = string, value = 'Minecraft Python', command=selection)
radio1.pack()
radio2 = tk.Radiobutton(window, text = 'Pygame', variable =string, value = 'pygame', command = selection)
radio2.pack()
radio3 = tk.Radiobutton(window, text = 'Tkinter', variable =string, value = 'Tkinter', command = selection)
radio3.pack()
window.mainloop()


