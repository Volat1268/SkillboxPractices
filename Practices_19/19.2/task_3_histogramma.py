txt = input('Введите текст: ')
hist = dict()
for sym in txt:
    if sym in hist:
        hist[sym] += 1
    else:
        hist[sym] = 1
print(hist)
for sym in sorted(hist):
    print('{0} : {1}'.format(sym, hist[sym]) )

print('Максимальная частота: {}'.format(max(hist.values())))
