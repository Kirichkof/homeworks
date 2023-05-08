def main(begin: int, end: int) -> list:
    if begin > end:
        raise ValueError
    return (num for num in range(begin, end+1) if num%2==0)

print(main(1, 10))
for item in main(1, 10):
    print(item, end = ', ')

print('\n', '*'*35)
gen2 = main(2, -14)
while True:
    print(next(gen2), end= ', ')