nmb = int(input('Введите количество заказов: '))
orders = {}

for i_ord in range(1, nmb + 1):
    pers_order = {}

    new_ord = {}
    new_pers = {}

    print(f'{i_ord}-й заказ:', end=' ')
    order_lst = input().split()
    if order_lst[0] in orders:
        pers_order_lst = []
        pass
        # if order_lst[1] == orders[order_lst[0]]['title']:
        #     orders[order_lst[0]]['qnt'] += int(order_lst[2])
        # else:
        #     new_ord['title'] = order_lst[1]
        #     new_ord['qnt'] = int(order_lst[2])
        #     orders.update(new_ord)
    else:
        pers_order['title'] = order_lst[1]
        pers_order['qnt'] = int(order_lst[2])




print(orders)
