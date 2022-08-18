family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

print(family_member['children'])

for child in family_member['children']:
    if child['name'] == 'Bob':
        print('Ребенок с именем Bob есть.')
        surname = child.get('surname', 'Nonsurname')
        print(surname)

