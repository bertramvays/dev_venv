# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# # и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def n_angle_figure(point, angle, length, num_of_angles):
    start_point = point
    colors = {
               1: sd.COLOR_RED,
               2: sd.COLOR_ORANGE,
               3: sd.COLOR_YELLOW,
               4: sd.COLOR_GREEN,
               5: sd.COLOR_CYAN,
               6: sd.COLOR_BLUE,
               7: sd.COLOR_PURPLE
               }
    color_input = input(f'Какого цвета Вы бы хотели {num_of_angles}-угольник? '
                  f'\nДоступные цвета: \n1 - красный, 2 - оранжевый, \n3 - жёлтый, 4 - зелёный,'
                  f' \n5 - зелёно-голубой, 6 - голубой, 7 - пурпурный'
                        f'\n>>> ')
    color = colors[int(color_input)]
    for _ in range(num_of_angles - 1):
        v = sd.get_vector(point, angle, length)
        v.draw(color=color)
        point = v.end_point
        angle += int (360 / num_of_angles)

    sd.line(v.end_point, start_point, color)

def triangle(point, angle, length):

    n_angle_figure(point, angle, length, num_of_angles=3)



def square(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=4)


def fifthka(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=5)


def shystka(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=6)

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
#
#
# sd.pause()

print(sd.random_number(int(30 - 30 *.4), int(30 + 30 *.4)))