txt = input('Введите строку: ')
txt_set = set(txt)
nums = set([str(num) for num in range(10)])

response = list(sorted(txt_set & nums))
print('Различные цифры строки: ', end='')
for sym in response:
    print(sym, end='')
