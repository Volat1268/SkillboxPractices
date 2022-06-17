cells = []
count_cells = int(input('Количество клеток: '))
for i in range(count_cells):
    print('Эффективность', i + 1, 'клетки:', end=' ')
    efficiency = int(input())
    cells.append(efficiency)

select_cells = []
count = 1
for i in range(len(cells)):
    if count > cells[count-1]:
        select_cells.append(cells[count - 1])
    count += 1
print('Неподходящие значения:', select_cells)
