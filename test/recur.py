site = {
    'html': {
        'head': {
            'title': 'My site'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result



user_key = input('Введите ключ: ')
response = find_key(site, user_key)
if response:
    print(response)
else:
    print('Non')