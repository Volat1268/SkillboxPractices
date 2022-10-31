def get_key(obj, k):
    if k in obj:
        return obj[k]
    for subobj in obj.values():
        if isinstance(subobj, dict):
            result = get_key(subobj, k)
            if result:
                break
    else:
        result = None
    return result





site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}

value = get_key(site, 'head')
if value:
    print(value)
else:
    print('Такого ключа нет')