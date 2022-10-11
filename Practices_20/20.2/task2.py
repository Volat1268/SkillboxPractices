import math
r = int(input('Введите радиус: '))
h = int(input('Введите высоту: '))

def barrel(r, h):
    side = round(2 * math.pi * r * h, 2)
    full = round(side + 2 * (2 * math.pi * r), 2)
    return side, full
response = barrel(r, h)
print(f'Площадь боковой поверхности: {response[0]}')
print(f'Полная площадь: {response[1]}')


