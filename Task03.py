list = []
n = int(input('Введите число:'))
sumnum = 0
for i in range(1, n + 1):
    sumnum = ((1+1/i)** i)
    list.append(sumnum)    
print(list)
print(f'Сумма чисел последовательности (1+1/n)^n: {sum(list)}')