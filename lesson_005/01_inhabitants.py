# -*- coding: utf-8 -*-
import room_1, room_2
# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

print('В комнате room_1 живут:')
for name in room_1.folks:
    print('\t', name)

print('В комнате room_2 живут:')
for name in room_2.folks:
    print('\t', name)

