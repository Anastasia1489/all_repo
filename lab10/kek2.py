dct = {}

with open('en-ru.txt') as f:
    while True:
        line = f.readline()

        if not line:
            break

        fdata = line.split('-')
        fdata[0] = fdata[0].lstrip().rstrip()

        for i in fdata[1].split(','):
            i = i.lstrip().rstrip()
            if i not in dct:
                dct[i] = [fdata[0]]
            else:
                dct[i].append(fdata[0])


with open('ru-en.txt', 'w') as f:
    for key, value in dct.items():
        f.write(key + ' - ' + ', '.join(value) + '\n')
