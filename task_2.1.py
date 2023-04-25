list = [7, 5, 3, 3, 2]
while True:
    new_list = int(input('Введите число: '))
    if (new_list > 0):
        list.append(new_list)
        list.sort(reverse=True)
        print(*list, sep=', ')
    else:
        break