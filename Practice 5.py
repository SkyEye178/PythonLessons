profit = int(input("Какая прибыль у фирмы?:"))
costs = int(input("Какие издержки у фирмы?:"))
result = profit - costs

if profit > costs:
    profitability = (result / profit) * 100
    print(f"Рентабельность составляет {result:.2f} или {profitability:.2f}%")

    employses = int(input("Укажите колличество сотрудников в фирме:"))
    profit_employses = result / employses
    print(f"На одного сотрудника прибыль: {profit_employses:.2f}")

elif profit < costs:
    print(f"Убыток составляет {result:.2f}")

else:
    print("Прибыль равна издержкам")