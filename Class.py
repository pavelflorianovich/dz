from tkinter import *
from random import randrange as rnd, choice
import math
import time

root = Tk()
root.geometry('800x600')
canv = Canvas(root, width=800, height=600, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


class Ball:
    def __init__(self):  # создание шарика
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.move_x = rnd(-10, 10)
        self.move_y = rnd(-10, 10)
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r,
                                     self.x + self.r, self.y + self.r, fill=choice(colors), width=0)

    def new_ball(self):  # удаление предыдущих шариков и создание новых
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.move_x = rnd(-10, 10)
        self.move_y = rnd(-10, 10)
        canv.delete(self.ball)
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r,
                                     self.x + self.r, self.y + self.r, fill=choice(colors), width=0)
        root.after(2000, self.new_ball)

    def move_ball(self):
        canv.move(self.ball, self.move_x, self.move_y)  # движение шарика
        self.x = self.x + self.move_x
        self.y = self.y + self.move_y
        if self.x + self.r >= 800:   # условия рандомного отражения
            self.move_x = rnd(-10, -1)
            self.move_y = rnd(-10, 10)
        elif self.x - self.r <= 0:
            self.move_x = rnd(1, 10)
            self.move_y = rnd(-10, 10)
        if self.y + self.r >= 600:
            self.move_y = rnd(-10, -1)
            self.move_x = rnd(-10, 10)
        elif self.y - self.r <= 0:
            self.move_y = rnd(1, 10)
            self.move_x = rnd(-10, 10)
        root.after(30, self.move_ball)


class Rectangle:
    def __init__(self):  # создание m прямоугольников
        self.xc = rnd(100, 700)
        self.yc = rnd(100, 500)
        self.rc = rnd(30, 50)
        self.move_xc = rnd(-10, 10)
        self.move_yc = rnd(-10, 10)
        self.pr = canv.create_rectangle(self.xc - self.rc, self.yc - self.rc,
                                               self.xc + self.rc, self.yc + self.rc, fill="black", width=0)

    def new_rect(self):  # удаление предыдущих прямоугольников и создание новых
        self.xc = rnd(100, 700)
        self.yc = rnd(100, 500)
        self.rc = rnd(30, 50)
        self.move_xc = rnd(-10, 10)
        self.move_yc = rnd(-10, 10)
        canv.delete(self.pr)
        self.pr = canv.create_rectangle(self.xc - self.rc, self.yc - self.rc,
                                               self.xc + self.rc, self.yc + self.rc, fill="black", width=0)
        root.after(2000, self.new_rect)

    def move_rect(self):  # граничные условия для прямоугольников
        canv.move(self.pr, self.move_xc, self.move_yc)
        self.xc = self.xc + self.move_xc
        self.yc = self.yc + self.move_yc
        if self.xc + self.rc >= 800:
            self.move_xc = rnd(-10, -1)
            self.move_yc = rnd(-10, 10)
        elif self.xc - self.rc <= 0:
            self.move_xc = rnd(1, 10)
            self.move_yc = rnd(-10, 10)
        if self.yc + self.rc >= 600:
            self.move_yc = rnd(-10, -1)
            self.move_xc = rnd(-10, 10)
        elif self.yc - self.rc <= 0:
            self.move_yc = rnd(1, 10)
            self.move_xc = rnd(-10, 10)
        root.after(5, self.move_rect)


class point():
    def __init__(self):  # создание класса очков
        self.score = 0  # self.score - количество очков

    def increse_ball(self):  # функция прибавления количества очков за попадания в шарик
        self.score += 1

    def increse_rect(self):  # функция прибавления количества очков за попадания в прямоугольник
        self.score += 3

    def print_point(self):  # функция печати количества очков
        print(self.score)


def yes(n):  # Создание n шариков
    for i in range(n):
        b.append(Ball())
        b[i].new_ball()
        b[i].move_ball()


def yes_1(m):  # Создание m прямоугольников
    for i in range(m):
        r.append(Rectangle())
        r[i].new_rect()
        r[i].move_rect()


def click(event):  # подсчет и печать очков
    for i in range(len(b)):
        x_1 = b[i].x
        y_1 = b[i].y
        r_1 = b[i].r
        if (x_1 - event.x) ** 2 + (y_1 - event.y) ** 2 <= r_1 ** 2:  # условие попадания в цель
            k.increse_ball()
            k.print_point()
    for i in range(len(r)):
        xc_1 = r[i].xc
        yc_1 = r[i].yc
        rc_1 = r[i].rc
        if math.sqrt((xc_1 - event.x) ** 2) <= rc_1 and math.sqrt((yc_1 - event.y) ** 2) <= rc_1:  # условие попадания
            k.increse_rect()
            k.print_point()

print('name: ')  # запрос имени игрока
name = input()
k = point()
b = []  # лист состояший из объктов класса Ball
r = []  # лист состояший из объктов класса Rectangle

yes(5)
yes_1(3)
canv.bind('<Button-1>', click)  # запуск функции click после нажатия на левую кнопку мышки
mainloop()


point_str = str(k.score)  # переводим количество очков в стрку

f = open('Res.txt', mode='a')  # открываем файл Res.txt для записи
f.write('\n' + name + ': ' + point_str)  # записываем
f.flush()
f.close()
