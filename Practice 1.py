def div():
    try:
        div_d = int(input('Деление чисел:\nвведите делимое: '))
        div_r = int(input('Деление чисел:\nвведите делитель: '))
    except ValueError:
        return
    try:
        div_d = div_d / div_r
        return  div_d
    except ZeroDivisionError:
        return

print(f'Ответ: {div()}')

