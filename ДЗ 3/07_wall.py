# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

k = 0
for y in range(0, 800, 50):
    k += 50
    for x in range(0, 650, 100):

        bottom_point = sd.get_point(x + k, y)
        top_point = sd.get_point(x + 100 + k, y + 50)
        sd.rectangle(bottom_point, top_point, sd.random_color(), width=2)
    k *= -1


sd.pause()
