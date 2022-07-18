nums = []
for i in range(1, 5):
    while True:
        print('Введите', i, 'число в диапазоне от 0 до 255 (включительно):', end=' ')
        nmb = int(input())
        if nmb > 255:
            print('Число больше 255! Будьте внимательней"')
        else:
            break
    nums.append(nmb)
ip_address = '{0}.{1}.{2}.{3}'.format(nums[0], nums[1], nums[2], nums[3])
print('Ваш IP-адрес:', ip_address)

