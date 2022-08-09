# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, smile_color):
    # голова

    center_point = sd.get_point(x, y)
    sd.circle(center_point, radius=50, color=smile_color, width=2)

    # улыбка
    lines_points = [sd.get_point(x - 40, y - 10),
                    sd.get_point(x - 10, y - 30),
                    sd.get_point(x + 10, y - 30),
                    sd.get_point(x + 40, y - 10),
                    ]
    sd.lines(lines_points, color=smile_color)
    sd.line(sd.get_point(x - 40, y - 10), sd.get_point(x + 40, y - 10), color=smile_color,)


#     глаза
    eye_center_point_1 = sd.get_point(x - 20, y + 10)
    sd.circle(eye_center_point_1, radius=10, color=smile_color, width=3)
    eye_center_point_2 = sd.get_point(x + 20, y + 10)
    sd.circle(eye_center_point_2, radius=10, color=smile_color, width=3)


if '__name__' == '__main__':

    for _ in range(20):
        pt = sd.random_point()
        smile(pt.x, pt.y, sd.random_color())
    sd.pause()
