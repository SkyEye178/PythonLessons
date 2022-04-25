numb_list = []

while True:
    numbers = (input('Введите числа через пробел или введите Q для выхода из цикла: '))

    if numbers.upper() != 'Q':
        try:
            for i in numbers.split(' '):
                numb_list.append(int(i))
                sum_numb = sum(numb_list)
            print(sum_numb)

        except ValueError:
            print('Ошбика! Необходимо ввести только числа или Q для выхода из цикла. \n')
    else:
        print(f'Вы вышли из цикла. \n Итоговая сумма = {sum_numb}')
        break