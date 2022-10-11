txt_str = 'О Дивный Новый мир!'
txt_lst = [100, 200, 300, 'буква', 0, 2, 'а']
txt_dct = {0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}
def get_even_elements(txt):
    if isinstance(txt, dict):
        txt = txt.values()
    result = [v for i, v in enumerate(txt) if i % 2 == 0]
    return result

print(get_even_elements(txt_str))
print(get_even_elements(txt_lst))
print(get_even_elements(txt_dct))