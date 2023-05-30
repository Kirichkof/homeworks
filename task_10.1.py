def mapping(func, data):
    gen = (func(item) for item in data)
    if isinstance(data, list):
        proc = list
    if isinstance(data, tuple):
        proc = tuple
    if isinstance(data, set):
        proc = set
    return proc(gen)

print(mapping(str, [1, 1, 2, 3, 4, 5] ))
print(mapping(float, (1, 1, 2, 3, 4, 5) ))
print(mapping(round, {1.1, 1.4, 2.6, 3.3, 4.8, 5.0} ))