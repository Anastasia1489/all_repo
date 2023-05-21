def mod_3(x):
    return x % 3


def divis(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Cant div by 0')


x = 100
try:
    y = int(input())
except ValueError:
    print('Number must be integer or double, not string')

print(divis(x, y))


def magic(x):
    if len(x) != 3:
        return False
    if int(x[0]) * int(x[1]) == int(x[2][2:4]):
        return True
    return False


x = input().split('.')
print(magic(x))


def check(x):
    a, b = 0, 0
    for i in range(len(x) // 2):
        a += int(x[i])
    for i in range(len(x) // 2):
        b += int(x[len(x) // 2 + i])
    return a == b


print(check('1221'))
