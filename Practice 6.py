first_day = int(input("Сколько вы пробежали в первый км день?:"))
last_day = int(input("К какому результату вы стремиьтесь?:"))
sum_in_day = 0.05
day = 1

while True:
    print(f"{day}-й день: {first_day:.2f} км.")
    first_day = first_day + (first_day * sum_in_day)
    if first_day > (last_day + (last_day * sum_in_day)):
        break
    else:
        day += 1
    continue

print(f"Спортсмену потребуется {day} для достижения {last_day} км.")