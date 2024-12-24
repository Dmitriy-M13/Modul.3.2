summ = 0
max_num = -10_000
min_num = 10_000

while True:
    num = int(input('введите число: '))

    if num == 7:
        break

    summ += num
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(f'Минимум: {min_num} | Максимум: {max_num} | Сумма: {summ}')