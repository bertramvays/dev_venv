# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

grant, expenses, mnth = 10000, 12000, 1
symmary_expenses = 12000
exp = []
while mnth < 10:
    exp.append(expenses)
    grant += 10000
    symmary_expenses += expenses * 1.03
    expenses *= 1.03
    mnth += 1

deficit_budgeta = symmary_expenses - grant

print(f'Студенту надо попросить {round(deficit_budgeta)} рублей')


