def replace(lst_data):
    lst_res = lst_data.copy()
    min_val = min(lst_res)
    max_val = max(lst_res)
    if min_val == max_val:
        return None
    for i, el in enumerate(lst_res):
        if el == min_val:
            lst_res[i] = max_val
    return lst_res

print(replace([1, 3, 1, 3, 4, 2, 5, 5, 2]))
print(replace([2, 3, 2, 3, 4, 2, 4, 4, 2]))
print(replace([3, 3, 3, 3, 3, 3, 3, 3, 3]))