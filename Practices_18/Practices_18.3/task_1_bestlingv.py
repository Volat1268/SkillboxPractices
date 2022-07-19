words_lst = []
for i_word in range(1, 4):
    print('Введите', i_word, 'слово', end=' ')
    word = input()
    words_lst.append(word)
text = input('Введите текст: ')

text_lst = text.split()

amt_lst = []
for word in words_lst:
    amt = text_lst.count(word)
    amt_lst.append(amt)

for i in range(len(words_lst)):
    print('Слово', words_lst[i - 1], 'встречается', amt_lst[i - 1], 'раз.')
