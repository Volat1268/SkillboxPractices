ef get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    cells = []
    count_cells = int(input('Количество клеток: '))
    for i in range(count_cells):
        print('Эффективность', i + 1, 'клетки:', end=' ')
        efficiency = int(input())
        cells.append(efficiency)
    return cells
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """
    rang_lst = []
    rang = 1
    for i in cells:
        rang_lst.append(rang)
        rang += 1


    select_cells = []
    for i in range(count_cells):
        print(i, rang_lst[i], cells[i])
        if rang_lst[i] > cells[i]:
            select_cells.append(cells[i])


    # TODO: в этой функции пишем логику отбора клеток.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass

