def arguments_print(func):
    def wrapper(*args, **kwargs):
        if len(args) != 0:
            print('именованные аргументы:', end = ' ')
            for item in args:
                print(f'{item}', end = '')
            print('')
        if len(kwargs) != 0:
            print('позиционные аргументы', end = ' ')
            for name, value in kwargs.items():
                print(f'{name}={value}', end = ',')
            print('')
        result = func(*args, **kwargs)
        return result
    
    return wrapper

def f1(x, y, z):
    return None

f1 = arguments_print(f1)


print(f1(1,2,3))
print(f1(x=11,z=12,y=13))
print(f1(11,z=12,y=13))