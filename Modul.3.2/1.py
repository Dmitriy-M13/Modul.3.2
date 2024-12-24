a = int(input('введите диапозон чисел от: '))
b = int(input('до: '))

summ = 0
summ_2 = 0
summ_3 = 0
for i in range(a, b+1):
    if i%2 != 0:
        summ += i
    if i%2 == 0:
        summ_2 += i
    if i%9 == 0:
        summ_3 += i
print("Сумма нечётных: ", summ)
print("Сумма чётных: ", summ_2)
print("Сумма кратных на 9: ", summ_3)