year = int(input('Введите год: '))
if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
    print ('Год ' + str(year) + ' является високосным')
else:
    print ('Год ' + str(year) + ' не является високосным')