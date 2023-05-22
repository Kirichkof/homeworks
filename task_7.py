def min_max(data: list) -> tuple:
    data_min = (min(data))
    data_max = (max(data))
    if data_min == data_max:
        raise ValueError
    return data_min, data_max

if __name__ == '__main__':
    print(min_max([1, 2, 3, 4, 5, 6]))
    print(min_max([1, 2, 1, 2, 2, 1]))
    print(min_max([1, 1, 1, 1, 1, 1]))