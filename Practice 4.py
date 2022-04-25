x = int(input("Введите целое положительное число:"))

if x > 0 and x % 1 == 0:
    max_x = 0
    while x > 0:
        y = x % 10
        x //= 10
        if y > max_x:
            max_x = y
    print("Самая большая цифра в числе:", max_x)

else:
    print("Введите целое число")




