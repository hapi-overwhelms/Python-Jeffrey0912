# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:25:42 2020

@author: John Kao
"""
#Below are the setup lines
import tkinter as tk 
import tkinter.messagebox
window = tk.Tk()
window.title("Soul releaser.exe (free version)")
window.geometry = ('500x227')

#Functions below
def clickMe():
    tkinter.messagebox.showinfo(title = 'Emergency Message', message = 'Success! You have released 6000 souls into the living world')

#define label
label = tk.Label(window, text = "Hehe... Don't Press it(Please enter the numnber that you need)", fg = "#6FF")

#define entry
entry = tk.Entry(window, width = 20)

#define button
button = tk.Button(window, text = "Click to Unleash", command = clickMe)

#Below are the command lines
label.pack()
entry.pack()
button.pack()
window.mainloop()