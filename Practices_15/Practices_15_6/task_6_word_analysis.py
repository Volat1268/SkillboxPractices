word = input('Введите слово: ')

number_unique_letters = 0
for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1
    if count == 1:
        number_unique_letters += 1

print(number_unique_letters)
