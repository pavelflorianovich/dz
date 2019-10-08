from math import cos
from math import sin
from math import pi

x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4 = input().split()
x_1 = int(x_1)
y_1 = int(y_1)
x_2 = int(x_2)
y_2 = int(y_2)
x_3 = int(x_3)
y_3 = int(y_3)
x_4 = int(x_4)
y_4 = int(y_4)


def rotate_square(square, angle):
    x_1 = square[0][0]
    y_1 = square[0][1]
    x_2 = square[1][0]
    y_2 = square[1][1]
    x_3 = square[2][0]
    y_3 = square[2][1]
    x_4 = square[3][0]
    y_4 = square[3][1]

    xc = (x_1 + x_3) / 2
    yc = (y_1 + y_3) / 2

    x1 = xc + (x_1 - xc) * cos(angle) - (y_1 - yc) * sin(angle)
    y1 = yc + (x_1 - xc) * sin(angle) + (y_1 - yc) * cos(angle)
    x2 = xc + (x_2 - xc) * cos(angle) - (y_2 - yc) * sin(angle)
    y2 = yc + (x_2 - xc) * sin(angle) + (y_2 - yc) * cos(angle)
    x3 = xc + (x_3 - xc) * cos(angle) - (y_3 - yc) * sin(angle)
    y3 = yc + (x_3 - xc) * sin(angle) + (y_3 - yc) * cos(angle)
    x4 = xc + (x_4 - xc) * cos(angle) - (y_4 - yc) * sin(angle)
    y4 = yc + (x_4 - xc) * sin(angle) + (y_4 - yc) * cos(angle)

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

rotate_square([(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4)], pi/4)

