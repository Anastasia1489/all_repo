a = [1, 2, 3, 4, 5]
b = int(input())

print(*a, b)
if b in a:
    print('Поздравляю! Вы угадали число!')
else:
    print('Нет такого числа!')


c = [1, 2, 1, 1, 3, 4, 5, 6, 7, 7]
d = set(c)
for i in d:
    if c.count(i) > 1:
        print(i)


week = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
d = int(input())

print('Ваши выходные дни: ')
for i in range(len(week) - 1, len(week) - d - 1, -1):
    print(week[i])

print('Ваши рабочие дни: ')
for i in range(0, len(week) - d):
    print(week[i])


fam = ['Q', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
another_fam = ['Ww', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj']

sport = (fam[0], fam[1], fam[2], fam[3], fam[4], another_fam[1], another_fam[2], another_fam[3], another_fam[4], another_fam[5])
print(*fam)
print(*another_fam)
print(*sport)

print(len(sport))
sport = sorted(sport)
print(*sport)

print(sport.count('Иванов'))
