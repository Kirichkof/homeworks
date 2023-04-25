n = int(input('Введите число: '))

a = n % 10
b = n % 100 // 10
c = n // 100

result = a + b + c

print('Сумма чисел числа ' + str(n) + ' равна ' + str(result))