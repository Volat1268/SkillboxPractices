players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

players_a_rest = [
    player['name']
    for player in players_dict.values()
    if player['status'] == 'Rest' and player['team'] == 'A'
]

players_b_training = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'

]

players_c_traveling = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]

# print('Все члены команды из команды А, которые отдыхают: ', players_a_rest)
# print('Все члены команды из команды B, которые тренируются: ', players_b_training)
# print('Все члены команды из команды С, которые путешествуют: ', players_c_traveling)

