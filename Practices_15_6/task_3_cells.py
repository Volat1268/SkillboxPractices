cells = []
count_cells = int(input('Количество клеток: '))
for i in range(count_cells):
    print('Эффективность', i + 1, 'клетки:', end=' ')
    efficiency = int(input())
    cells.append(efficiency)
print(cells)


rang_lst = []
rang = 1
for i in cells:
    rang_lst.append(rang)
    rang += 1
print(rang_lst)


select_cells = []
for i in range(count_cells):
    print(i, rang_lst[i], cells[i])
    if rang_lst[i] > cells[i]:
        select_cells.append(cells[i])
        # print(cells[i])
print('Неподходящие значения:', select_cells)
