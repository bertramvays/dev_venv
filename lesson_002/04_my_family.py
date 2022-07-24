#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Оля', 'Nastia', 'Anna', 'gr.Aleksandr', 'gr.Natalia']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Olia', 165],
    ['Nastia', 105],
    ['Anna', 85],
    ['gr.Aleksandr', 175],
    ['gr.Natalia', 150],
]
print(f'Рост {my_family_height[3][0]} - {my_family_height[3][1]} см')
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_height = 0
for i in my_family_height:
    sum_height += i[1]
print(f' Общий рост моей семьи {sum_height}')

