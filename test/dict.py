import copy

# d1 = {
#     'name': 'Aleks',
#     'city': 'Minsk',
#     'age': 53
# }
# d2 = dict(color1='red', color2='blue', color3='black')
# d3 = dict([('a', 'A'), ('b', 'B'), ('c', 'C')])
# d4 = dict(dict({'Amanda': 27, 'Teresa': 38}, Paula=17, Mario=40))
# d5 = dict.fromkeys(['one', 'two', 'three'], 'ints')
# d6 = {i: chr(65 + i) for i in range(5)}
# d7 = {i: chr(65 + i) for i in range(10, 20) if i % 2 == 0}
# d6.update(d7)
# del d6[18]
# dcopy = d3.copy()
# dcopy['c'] = 'D'
# d44 = d4.copy()
# d44.update([('Amanda', 22), ('Teresa', 33)])
# d44.update(Paula=11, Mario={'m': 1, 'a': 2, 'r': 3}, Claus=[55, 66, 66])
# d44copy = copy.deepcopy(d44)
# d44copy['Claus'][2] = 67
# d44copy['Mario']['r'] = 33
# print(d44)
# print(d44copy)

# prod = {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100, 'pillow': 10, 'shelf': 70, 'sofa': 400}
# min_prod = {product: price for product, price in prod.items() if price < 120}
#
# print(min_prod)

# txt = 'aa & )))abld//.bad'
# d = {}
# for i in txt:
#     if i.isalpha():
#         d[i] = d.get(i, 0) + 1
# for i in sorted(d):
#     print(i, d[i])

# order = {'ivanov': [{'pizza1': 2}, {'pizza2': 3}], 'petrov': [{'pizza3': 1}, {'pizza4': 1}, {'pizza3': 3}]}
# plus = {'pizza1': 12}
# order['ivanov'].append(plus)
# print(order)

# for k, v in order.items():
#     pizzas = {}
#     for i in v:
#         print(i.keys())
#     if i.keys() in pizzas:
#         pizzas[i.keys()] += pizzas[i.values()]
#     else:
#         pizzas[i.keys()] = pizzas[i.values()]
# print(pizzas)

lst = [{}]
