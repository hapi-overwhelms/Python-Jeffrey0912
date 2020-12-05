# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:17:29 2020

@author: John Kao
"""
import time
import datetime
import turtle
tur = turtle.Turtle()
turtle.setup(500,500)
tur.penup()

tur.goto(0,120)
tur.right(180)
tur.color(0,0,0)
tur.speed(10)

tur.pendown()


def clock():
    tur.circle(120, 360, 40)
    tur.penup()
    tur.goto(0,95)
    tur.pendown()
    for x in range(12):
        tur.penup()
        tur.circle(100, -30, 10)
        tur.pendown()
        tur.write(x+1)
    for y in range(60):
        tur.penup()
        tur.circle(100, 6, 10)
        tur.pendown()
        tur.write('.')
    tur.penup()
    tur.goto(0, 76)
    tur.pendown()
    for z in range(12):
        tur.penup()
        tur.circle(80,30, 10)
        tur.pendown()
        tur.write('o')
clock()
update = True
updatesecond = True
while True:
    now= datetime.datetime.now()
    h = now.hour%12
    m = now.minute
    s = now.second
    if update:
        hour = turtle.Turtle()
        hour.seth(90)
        hour.right(h*30+m/60*30)
        hour.forward(50)
        minute = turtle.Turtle()
        minute.seth(90)
        minute.right(m*6)
        minute.forward(80)
        update= False
    if updatesecond:
        second = turtle.Turtle()
        second.seth(90)
        second.right(s*6)
        second.forward(90)
        updatesecond = False
    time.sleep(1)
    newm = datetime.datetime.now()
    nm = newm.minute
    updatesecond = True
    second.clear()
    second.reset()
    
    if newm != m:
        update = True
        hour.clear()
        hour.reset()
        minute.clear()
        minute.reset()
turtle.done()
turtle.exitonclick()