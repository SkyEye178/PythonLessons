#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().

elements = int(input('Какое колличестов элементов вы хотите внести в список? \n'))

my_list = [ ]
for i in range(elements):
    i += 1
    a = input(f'Элемент №{i}: ')
    my_list.append(a)

print(f'Лист до изменения: {my_list} \n')

n_list = []

for i in range(len(my_list)):
    if i % 2 != 0:
        n_list.insert(i - 1, my_list[i])
    else:
        n_list.insert(i + 1, my_list[i])

print(f'Лист полсе изменения: {n_list}\n')
