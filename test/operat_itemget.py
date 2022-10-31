from operator import itemgetter

obj = [(123, 'aleks', 'aaa'), (22, 'aleks', 'bbb'), (999, 'boris', 'aaa'), (58, 'boris', 'zzz')]

a = sorted(obj, key=itemgetter(0))
b = sorted(obj, key=itemgetter(0), reverse=True)
c = sorted(obj, key=itemgetter(2))
d = sorted(obj, key=itemgetter(2), reverse=True)
e = sorted(obj, key=itemgetter(2, 1))
print(a)
print(b)
print(c)
print(d)
print(e)