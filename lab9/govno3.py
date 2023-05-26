import csv


input_file = input()
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    sm = 0
    for row in reader:
        sm += int(row['Quantity']) * int(row['Price'])
        print(str(row['Product']) + ' - ' + str(row['Quantity']) + 'шт. за ' + str(row['Price']) + ' руб.')

    print('Итоговая сумма: ' + str(sm) + ' руб.')
