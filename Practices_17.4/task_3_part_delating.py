import random

orig_lst = [random.randint(1, 100) for _ in range(10)]
a = random.randint(1, 4)
b = random.randint(5, 9)

print(orig_lst)
print('index a:', a)
print('index b:', b)

orig_lst[a:b+1] = ''

print(orig_lst)