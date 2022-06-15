your_words_lst = []
for i_word in range(3):
    print('Введите', i_word + 1, 'слово:', end=' ')
    word = input()
    your_words_lst.append(word)

words_count_lst = [0, 0, 0]
text_word = input("Слово из текста: ")
while text_word != 'end':
    for i in range(3):
        if your_words_lst[i] == text_word:
            words_count_lst[i] += 1
    text_word = input("Слово из текста: ")

print("\nПодсчет слов в тексте:")
for i in range(3):
    print(your_words_lst[i], ":", words_count_lst[i])



