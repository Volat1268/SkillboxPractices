message = []
packs_amt = int(input('Кол-во пакетов: '))
untreated_paks_amt = 0

for i_pack in range(packs_amt):
    print('Пакет номер', i_pack + 1)
    pack = []
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end=' ')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) <= 1:
        message.extend(pack)
    else:
        untreated_paks_amt += 1

faults_amt = message.count(-1)

print('\nПолученное сообщение', message)
print('Кол-во ошибок в сообщении', faults_amt)
print('Кол-во потерянных пакетов', untreated_paks_amt)



