def countDown(start, indent=0):
    print('-'*indent, '>', start)
    start = start - 1
    indent = indent + 1
    if start >= 0:
        # Рекурсивный вызов 'countDown', в которой
        # происходит печать строки, но только уже с
        # другими значениями, которые вычисляются выше
        countDown(start, indent)

countDown(5, 2)