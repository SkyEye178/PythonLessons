print('1. Возведение в минусовую степень с помощью оператора **')


def my_func(x, y):
    try:
        if y > 0:
            y = y * -1
        return print(abs(x) ** y)
    except ZeroDivisionError:
        return


my_func(2, 4)


print('2. Возведение в минусовую степень без оператора **, с помощью цикла')


def my_func(x, y):
    try:
        if y > 0:
            y = y * -1
        i = 0
        a = 1
        while i < abs(y):
            i += 1
            a *= x

        return print(1 / a)
    except ZeroDivisionError:
        return


my_func(4, -6)