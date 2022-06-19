video_cards = []
vacrds_count = int(input('Количество видеокарт: '))
for i in range(vacrds_count):
    print(i + 1, 'Видеокарта:', end=' ')
    vcard = int(input())
    video_cards.append(vcard)

print('Старый список видеокарт', video_cards)


video_max = 0
for i in video_cards:
    if i > video_max:
        video_max = i


new_video_cards = []
for i in video_cards:
    if i < video_max:
        new_video_cards.append(i)
print('Новый список видеокарт', new_video_cards)


