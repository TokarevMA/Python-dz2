numb = input('Введите дробное число: ')
some_str = str(numb).replace('.', '')
some_str2 = list(map(int, some_str))
summ = 0
for number in some_str2:
    summ += number
print(summ)