import simple_draw as sd
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()



sd.resolution = (1000, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
flake_x_points = []  # coordinate x
for _ in range(20):
    flake_x_points.append(sd.random_number(20, 950))
flake_y_points = [] # coordinate y
for _ in range(20):
    flake_y_points.append(sd.random_number(400, 550))
flake_params = []
for _ in range(20): # length and factors of different snowflakes
    length = sd.random_number(10, 100)
    factor_a = sd.random_number(1, 100) / 100
    factor_b = sd.random_number(1, 100) / 100
    factor_c = sd.random_number(1, 179)
    param = []
    param.append(length)
    param.append(factor_a)
    param.append(factor_b)
    param.append(factor_c)
    flake_params.append(param)

sd.start_drawing()
while True:
    sd.clear_screen()

    for i in range(20):

        point = sd.get_point(flake_x_points[i], flake_y_points[i])


        sd.snowflake(center=point, length=flake_params[i][0], color=sd.background_color,
                     factor_a=flake_params[i][1], factor_b=flake_params[i][2], factor_c=flake_params[i][3])
        flake_y_points[i] -= 30
        sd.snowflake(center=point, length=flake_params[i][0], color=sd.COLOR_WHITE,
                     factor_a=flake_params[i][1], factor_b=flake_params[i][2], factor_c=flake_params[i][3])

        flake_x_points[i] *= -1.03

        if flake_y_points[i] < 50:
            break

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
