# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и dict

seasons = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_seasons = int(input('Введите месяц в числовом формате от 1 до 12: '))

print(f'List: Месяц {month[month_seasons - 1]} относится ко времени года {seasons[month_seasons - 1]}')

seasons_dict = {
    1:'Winter',
    2:'Winter',
    3:'Spring',
    4:'Spring',
    5:'Spring',
    6:'Summer',
    7:'Summer',
    8:'Summer',
    9:'Autumn',
    10:'Autumn',
    11:'Autumn',
    12:'Winter'}

month_dict = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'}

print(f'Dict: Месяц {month_dict.get(month_seasons)} относится ко времени года {seasons_dict.get(month_seasons)}')
