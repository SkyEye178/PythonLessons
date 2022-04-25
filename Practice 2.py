time = int(input("Введите времяв секундах:"))

hours = time // 3600
minutes = (time // 60) - (hours //3600 * 60)
seconds = time % 3600 - minutes * 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")