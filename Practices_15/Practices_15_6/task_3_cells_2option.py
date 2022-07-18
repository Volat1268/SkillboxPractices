# ввожу данные по клеткам
cells = []
count_cells = int(input('Количество клеток: '))
for i in range(count_cells):
    print('Эффективность', i + 1, 'клетки:', end=' ')
    efficiency = int(input())
    cells.append(efficiency)

# создаю список из рангов клеток
rang_lst = []
rang = 1
for i in cells:
    rang_lst.append(rang)
    rang += 1

# сравниваю величины ранга и эффективности и делаю отбор неподходящих клеток
select_cells = []
for i in range(count_cells):
    if rang_lst[i] > cells[i]:
        select_cells.append(cells[i])
print('Неподходящие значения:', select_cells)
