# coding: utf-8
from turtle import *


def to_str(n, base):
    convert_str = '0123456789'
    if n < base:
        return convert_str[n]
    return to_str(n // base, base) + convert_str[n % base]


def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 10, t)
        t.right(20)
        t.backward(branch_len)


def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, t):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], t)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, t)
        sierpinski([points[1], get_mid(points[1], points[0]), get_mid(points[1], points[2])], degree - 1, t)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[2], points[0])], degree - 1, t)


def move_tower(height, from_disk, to_disk, with_disc):
    if height >= 1:
        move_tower(height-1, from_disk, with_disc, to_disk)
        move_disk(from_disk, to_disk)
        move_tower(height-1, with_disc, to_disk, from_disk)


def move_disk(from_disk, to_disk):
    print("moving disk from %s to %s\n" % (from_disk, to_disk))


if __name__ == '__main__':
    # t = Turtle()
    # mywin = t.getscreen()
    # t.left(90)
    # t.up()
    # t.backward(300)
    # t.down()
    # t.color('green')
    # tree(100, t)
    # mywin.exitonclick()

    # t = Turtle()
    # mywin = t.getscreen()
    # points = [(-500, -250), (0, 500), (500, -250)]
    # sierpinski(points, 5, t)
    # mywin.exitonclick()

    move_tower(3, 'A', 'C', 'B')
