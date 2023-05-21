n = int(input())
ans = ""
for i in range(n):
    s = input()
    ans = ans + " " + s
print(ans)


ans = ""
while True:
    s = input()
    if s == "stop":
        break
    ans = ans + " " + s
print(ans)


while True:
    s = input()
    if 'ф' in s:
        print("Ого, это редкое слово")
    else:
        print("Эх, это не очень редкое слово...")


from random import randint

print('Давайте поиграем, вводи правильные ответы:')
res, ans = 0, 0
while True:
    if res == 3:
         print(f'Игра окончена. Правильных ответов: {ans}')

    a = randint(1, 100)
    b = randint(1, 100)
    print(f"{a} + {b} = ", end="")
    res = input()
    while not res.isdigit() and res != 'stop':
        print("Вы ввели что-то не то, повторите ввод: ", end="")
        res = input()
    res = int(res)
    if a + b == res:
        ans += 1
        print("Правильно!")
    else:
        res += 1
        print("Ответ неправильный :(")
