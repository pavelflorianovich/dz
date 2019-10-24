from tkinter import *
from random import randrange as rnd, choice
import math
import time

root = Tk()
root.geometry('800x600')
canv = Canvas(root, width=800, height=600, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


def n_ball():  # создание n шариков
    global x, y, r, move_x, move_y, ball, n
    x = []
    y = []
    r = []
    move_x = []
    move_y = []
    ball = []
    for i in range(n):
        new_ball(i)
    move_ball()


def new_ball(i):  # коардинаты i-того шарика
    global x, y, r, move_x, move_y, ball
    x.append(rnd(100, 700))
    y.append(rnd(100, 500))
    r.append(rnd(30, 50))
    move_x.append(rnd(-10, 10))
    move_y.append(rnd(-10, 10))
    ball.append(canv.create_oval(x[i] - r[i], y[i] - r[i], x[i] + r[i], y[i] + r[i], fill=choice(colors), width=0))


def move_ball():  # граничные условия для шариков
    global x, y, move_x, move_y
    for i in range(len(ball)):
        canv.move(ball[i], move_x[i], move_y[i])
        x[i] = x[i] + move_x[i]
        y[i] = y[i] + move_y[i]
        if x[i] + r[i] >= 800:
            move_x[i] = rnd(-10, -1)
            move_y[i] = rnd(-10, 10)
        elif x[i] - r[i] <= 0:
            move_x[i] = rnd(1, 10)
            move_y[i] = rnd(-10, 10)
        if y[i] + r[i] >= 600:
            move_y[i] = rnd(-10, -1)
            move_x[i] = rnd(-10, 10)
        elif y[i] - r[i] <= 0:
            move_y[i] = rnd(1, 10)
            move_x[i] = rnd(-10, 10)
    root.after(30, move_ball)


def m_rectangle():  # создание m прямоугольников
    global xc, yc, rc, move_xc, move_yc, rectangle, m
    xc = []
    yc = []
    rc = []
    move_xc = []
    move_yc = []
    rectangle = []
    for i in range(m):
        new_rectangle(i)
    move_rectangle()


def new_rectangle(i):  # коардинаты i-того прямоугольника
    global xc, yc, rc, move_xc, move_yc, rectangle
    xc.append(rnd(100, 700))
    yc.append(rnd(100, 500))
    rc.append(rnd(30, 50))
    move_xc.append(rnd(-10, 10))
    move_yc.append(rnd(-10, 10))
    rectangle.append(canv.create_rectangle(xc[i] - rc[i], yc[i] - rc[i],
                                           xc[i] + rc[i], yc[i] + rc[i], fill="black", width=0))


def move_rectangle():  # граничные условия для прямоугольников
    global xc, yc, move_xc, move_yc
    for i in range(len(rectangle)):
        canv.move(rectangle[i], move_xc[i], move_yc[i])
        xc[i] = xc[i] + move_xc[i]
        yc[i] = yc[i] + move_yc[i]
        if xc[i] + rc[i] >= 800:
            move_xc[i] = rnd(-10, -1)
            move_yc[i] = rnd(-10, 10)
        elif xc[i] - rc[i] <= 0:
            move_xc[i] = rnd(1, 10)
            move_yc[i] = rnd(-10, 10)
        if yc[i] + rc[i] >= 600:
            move_yc[i] = rnd(-10, -1)
            move_xc[i] = rnd(-10, 10)
        elif yc[i] - rc[i] <= 0:
            move_yc[i] = rnd(1, 10)
            move_xc[i] = rnd(-10, 10)
    root.after(5, move_rectangle)


def click(event):  # подсчет и печать очков
    for i in range(n):
        if math.sqrt((x[i] - event.x) ** 2 + (y[i] - event.y) ** 2) <= r[i]:
            score[0] += 1
        score[1] += 0
    for i in range(m):
        if math.sqrt((xc[i] - event.x) ** 2) <= rc[i] and math.sqrt((yc[i] - event.y) ** 2) <= rc[i]:
            score[0] += 5
    score[1] += 1
    print(score)


n = 5
m = 3
score = [0, 0]

print('name: ')  # запрос имени игрока
name = input()
n_ball()
m_rectangle()
canv.bind('<Button-1>', click)
mainloop()

point_str = str(score)  # переводим количество очков и попыток в стрку

f = open('Res1.txt', mode='a')  # открываем файл Res1.txt для записи
f.write('\n' + name + ': ' + point_str)  # записываем
f.flush()
f.close()
