# word = input('Введите слово: ')
# new_word = []
# for i in range(len(word) - 1, -1, -1):
#     new_word.append(word[i])
# print(new_word)
#
# if list(word) == new_word:
#     print('OK')
# else:
#     print('Non')

word = input('Введите слово: ')
new_word = ''
for i in range(len(word) - 1, -1, -1):
    new_word += word[i]
print(new_word)

if word == new_word:
    print('OK')
else:
    print('Non')