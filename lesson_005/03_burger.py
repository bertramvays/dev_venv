# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from my_burger import *

# print('Сейчас приготовим двойной чизбургер:')
# bun()
# add_cutlet()
# add_cutlet()
# add_cucumber()
# add_tomato()
# add_mayo()
# add_cheese()
# add_cheese()
# print('\tДвойной чизбургер готов, приятного аппетита!')

print('Сейчас приготовим постный бургер:')
bun()
add_cucumber()
add_tomato()
add_salat()
add_oil()
print('\tПостный бургер готов, приятного аппетита!')

