def sum_factorials(num):
    part_fact = 1
    summa = 0
    for i in range(1, num+1):
        part_fact *= i
        summa += part_fact
    return summa

n = int(input('Введите число: '))
print(sum_factorials(n))