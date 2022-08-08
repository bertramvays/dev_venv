# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v2 = sd.get_vector(v1.end_point, angle + 120, length)
#     v3 = sd.get_vector(v2.end_point, angle + 240, length)
#     v3.draw()
#     v1.draw()
#     v2.draw()
#
#
# def square(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v2 = sd.get_vector(v1.end_point, angle + 90, length)
#     v3 = sd.get_vector(v2.end_point, angle + 180, length)
#     v4 = sd.get_vector(v3.end_point, angle + 270, length)
#     v1.draw()
#     v2.draw()
#     v3.draw()
#     v4.draw()
#
#
# def fifthka(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v2 = sd.get_vector(v1.end_point, angle + 72, length)
#     v3 = sd.get_vector(v2.end_point, angle + 144, length)
#     v4 = sd.get_vector(v3.end_point, angle + 216, length)
#     v5 = sd.get_vector(v4.end_point, angle + 288, length)
#     v1.draw()
#     v2.draw()
#     v3.draw()
#     v4.draw()
#     v5.draw()
#
#
# def shystka(point, angle, length):
#     v1 = sd.get_vector(point, angle, length)
#     v2 = sd.get_vector(v1.end_point, angle + 60, length)
#     v3 = sd.get_vector(v2.end_point, angle + 120, length)
#     v4 = sd.get_vector(v3.end_point, angle + 180, length)
#     v5 = sd.get_vector(v4.end_point, angle + 240, length)
#     v6 = sd.get_vector(v5.end_point, angle + 300, length)
#     v1.draw()
#     v2.draw()
#     v3.draw()
#     v4.draw()
#     v5.draw()
#     v6.draw()
#
#
# point_0 = sd.get_point(50, 50)
# triangle(point_0, 30, 100)
#
# point_0 = sd.get_point(200, 50)
# square(point_0, 0, 100)
#
# point_0 = sd.get_point(50, 200)
# fifthka(point_0, 0, 100)
#
# point_0 = sd.get_point(250, 200)
# shystka(point_0, 0, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)

def n_angle_figure(point, angle, length, num_of_angles):
    start_point = point
    for _ in range(num_of_angles -1):
        v = sd.get_vector(point, angle, length)
        v.draw()
        point = v.end_point
        angle += int (360 / num_of_angles)

    sd.line(v.end_point, start_point)

def triangle(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=3)


def square(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=4)


def fifthka(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=5)


def shystka(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=6)

point_0 = sd.get_point(50, 50)
triangle(point_0, 30, 100)

point_0 = sd.get_point(200, 50)
square(point_0, 0, 100)

point_0 = sd.get_point(50, 200)
fifthka(point_0, 0, 100)

point_0 = sd.get_point(250, 200)
shystka(point_0, 0, 100)


# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
