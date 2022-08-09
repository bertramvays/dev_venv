from random import randint


def riddle_number():
    """функция загадывания числа"""
    while True:
        global NN, nn_lst
        NN = randint(1234, 9876)
        nn_lst = [x for x in str(NN)]
        if len(set(nn_lst)) == 4:
            break
    return NN


def check_number(user_number):
    """ проверяет сколько в угаданных коров и быков"""
    user_num_lst = [ x for x in str(user_number)]
    B, C = 0, 0
    for digit in range(4):
        if user_num_lst[digit] == nn_lst[digit]:
            B += 1
        elif user_num_lst[digit] in nn_lst:
            C += 1
    bulls_cows = {'bulls': B, 'cows': C}

    return bulls_cows


if __name__ == '__main__':
    print(riddle_number())
    print(check_number(1256))
