from random import choice

names_all = ['Иван', 'Федор', 'Катерина', 'Марина', 'Илья', 'Ольга', 'Анастасия', ]
actions_all = ['гулять', 'в школу', 'на дачу', 'в магазин', 'на спортплощадку', 'на тренировку', ]
targets_all = ['идет', 'едет', 'спешит', 'бежит', 'не торопится', ]

def mix(number, names, actions, targets):
    result = list()
    for i in range(number):
        result.append(f'{choice(names)} {choice(targets)} {choice(actions)}')
    return result

print(mix(3, names_all, actions_all, targets_all))