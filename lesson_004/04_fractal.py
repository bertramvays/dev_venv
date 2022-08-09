# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 700)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(point, length, angle=30):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v2 = sd.get_vector(start_point=point, angle=180-angle, length=length, width=3)
#     v1.draw()
#     v2.draw()
#     return v1.end_point, v2.end_point

# def draw_branches(point, angle, length, width):
#     if length < 10:
#         return
#     else:
#         v0 = sd.Vector(point, angle, length, width)
#         v0.draw()
#         draw_branches(v0.end_point, angle - 30, length * 0.8, width)
#         draw_branches(v0.end_point, angle + 30, length * 0.8, width)

def draw_branches(point, angle, length, width):
    if length < 5:
        return
    else:
        v0 = sd.Vector(point, angle, length, width)
        v0.draw()
        draw_branches(v0.end_point, angle - sd.random_number(18, 42), length * sd.random_number(60, 90) / 100, width)
        draw_branches(v0.end_point, angle + sd.random_number(18, 42), length * sd.random_number(60, 90) / 100, width)


point_0 = sd.get_point(300, 30)
draw_branches(point_0, 90, 100, 2)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
