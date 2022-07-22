alph = [chr(i) for i in range(ord('а'), ord('я') + 1)]

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

new_text = ''.join(
    [' ' if sym == ' ' else alph[(alph.index(sym) + shift) % 32] for sym in text]
)
print('Зашифрованный текст:', new_text)

