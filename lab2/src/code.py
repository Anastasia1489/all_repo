a = input()
b = input()

if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')


n = int(input())
if n > 36:
    print('боковое место')
elif n % 2 == 0:
    print('в купе наверху')
else:
    print('в купе внизу')


year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print(f"Год {year} - високосный")
else:
    print("Этот год не високосный")
