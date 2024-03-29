import math
import time
from random import choice, randint as rnd
from tkinter import *

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canvas = Canvas(root, bg='blue')
canvas.pack(fill=BOTH, expand=1)
canvas.create_line(0, 520, 800, 520, width=7)


class Ball:
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['white', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 30

    def set_coords(self):
        canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 500:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.vy *= 0.99
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canvas.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779
        if self.x < 0:
            self.vx = -self.vx / 2
            self.x = 1

    def hit_test(self, ob):
        return abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r)


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        x = 40
        y = 450
        self.id = canvas.create_line(x - 20, y, x + 10, y - 30, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        if event.x > new_ball.x:
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = -self.f2_power * math.sin(self.an)
        else:
            new_ball.vx = self.f2_power * math.cos(self.an + math.pi)
            new_ball.vy = -self.f2_power * math.sin(self.an + math.pi)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        x = 40
        y = 450
        if event:
            self.an = math.atan((event.y - y) / (event.x - x + 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, x - 20, y, x - 20 + max(self.f2_power, 20) * math.cos(self.an),
                      y + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.id = canvas.create_oval(0, 0, 0, 0)
        self.id_points = canvas.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        x = self.x = rnd(20, 780)
        y = self.y = rnd(0, 500)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canvas.itemconfig(self.id_points, text=self.points)


t1 = Target()
screen1 = canvas.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global Gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', g1.fire2_end)
    canvas.bind('<Motion>', g1.targetting)
    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hit_test(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                canvas.itemconfig(screen1,
                                  text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canvas.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canvas.itemconfig(screen1, text='')
    canvas.delete(Gun)
    root.after(750, new_game)


new_game()
mainloop()
