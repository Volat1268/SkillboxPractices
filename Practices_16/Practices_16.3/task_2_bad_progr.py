def amt_of_symbols(text):
    count = 0
    for i in text:
        if i == '?' or i == '!':
            count += 1
    return count

third_text = ' '
first_text = input('Первое сообщение: ')
second_text = input('Второе сообщение: ')

first_text_amt = amt_of_symbols(first_text)
second_text_amt = amt_of_symbols(second_text)

if first_text_amt > second_text_amt:
    third_text = first_text + third_text
    third_text = third_text + second_text

    print('\nТретье сообщение', third_text)
elif first_text_amt < second_text_amt:
    third_text = third_text + second_text
    third_text = first_text + third_text

    print('\nТретье сообщение', third_text)
else:
    print('\nТретье сообщение', 'Ой!')




