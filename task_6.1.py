def main(begin: int, end: int) -> list:
    if begin > end:
        raise ValueError
    return [num for num in range(begin, end+1) if num%2==0]

print(main(1,10))
print(main(1,13))
print(main(-2,14))
print(main(1,-10))