def mapping(func, data):
    for item in data:
        yield func(item)

gen1 = mapping(str, [1, 1, 2, 3, 4, 5])
while True:
    try:
        print(next(gen1))
    except StopIteration:
        print('Итератор исчерпан')
        break