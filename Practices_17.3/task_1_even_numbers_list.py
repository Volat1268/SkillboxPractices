start = int(input('Введите начало диапазона: '))
finish = int(input('Введите конец диапазона: '))
lst_even = [num for num in range(start, finish + 1) if num % 2 == 0]

print(lst_even)