seqNum = int(input("Количество чисел в списке: "))
your_list = []
for i in range(seqNum):
    print("Введите", i + 1, "число:", end=" ")
    your_num = int(input())
    your_list.append(your_num)

devisor = int(input("\nВведите делитель: "))
print()
summa = 0
i_count = 0
for i_list in your_list:
    if i_list % devisor == 0:
        print("Индекс числа ", i_list, ": ", i_count, sep="")
        summa += i_count
    i_count += 1

print("Сумма индексов:", summa)
