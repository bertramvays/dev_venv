# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (500, 500)

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

figures = {
    1: 'треугольник',
    2: 'квадрат',
    3: 'пятиугольник',
    4: 'шестиугольник',
}

print(f'Возможные фигуры:'
      f'\n\t1 - треугольник'
      f'\n\t2 - квадрат'
      f'\n\t3 - пятиугольник'
      f'\n\t4 - шестиугольник')
while True:
    user_choise_figure = input('Введите желаемую фигуру >>> ')
    if not user_choise_figure.isnumeric():
        print('Вы ввели некоректный номер')
    elif not 0 < int(user_choise_figure) < 5:
        print('Не правильная цифра, попробуйте еще.')
    else:
        break


def n_angle_figure(point, angle, length, num_of_angles):
    start_point = point

    color = sd.random_color()
    for _ in range(num_of_angles - 1):
        v = sd.get_vector(point, angle, length)
        v.draw(color=color)
        point = v.end_point
        angle += int(360 / num_of_angles)

    sd.line(v.end_point, start_point, color)


def triangle(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=3)


def square(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=4)


def fifthka(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=5)


def shystka(point, angle, length):
    n_angle_figure(point, angle, length, num_of_angles=6)


sheet_center_point = sd.get_point(int(sd.resolution[0] / 2), int(sd.resolution[1] / 2))
if user_choise_figure == '1':
    triangle(sheet_center_point, 30, 100)
elif user_choise_figure == '2':
    square(sheet_center_point, 0, 100)
elif user_choise_figure == '3':
    fifthka(sheet_center_point, 0, 100)
else:
    shystka(sheet_center_point, 0, 100)

sd.pause()
