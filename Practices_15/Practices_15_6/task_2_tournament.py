names = ["Петр", "Дима", "Слава", "Коля", "4", "5", "6", "7"]
participants_names = []
count = 0
for name in names:
    if count % 2 == 0:
        participants_names.append(name)
    count += 1
print(participants_names)

