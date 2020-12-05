# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:12:05 2020

@author: John Kao
"""

import turtle
tur = turtle.Turtle()




turtle.setup(500,500)

def triangle():
    loop = 3
    tur.left(60)
    for x in range(loop):
        tur.forward(100)
        tur.right(120)
        
def square():
    
    loop = 4
    for x in range(loop):
        tur.forward(100)
        tur.right(90)
        
def rect():
    
    loop = 2
    for x in range(loop):
        tur.forward(150)
        tur.right(90)
        tur.forward(40)
        tur.right(90)

def vertrect():
    loop = 2
    for x in range(loop):
        tur.forward(50)
        tur.right(90)
        tur.forward(130)
        tur.right(90)


def pentagon():
    loop = 5
    tur.right(36)
    for x in range(loop):
        tur.forward(100)
        tur.right(72)
        
tur.penup()
tur.goto(50,50)
tur.pendown()
tur.fillcolor(1,0,0)
tur.begin_fill()
vertrect()
tur.end_fill()


tur.goto(0,50)
tur.fillcolor(1,1,1)
tur.begin_fill()
vertrect()
tur.end_fill()


tur.goto(-50,50)
tur.fillcolor(0,0,1)
tur.begin_fill()
vertrect()
tur.end_fill()







turtle.done()
turtle.exitonclick()