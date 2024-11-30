#Функция печати параметров
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#Основная программа
print_params()
print_params(16, 'Nice day', False)
print_params(45, c='Happy', b=True)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Andrey', 2006, True]
values_dict = {'a': 'Aleksey', 'b': 2009, 'c': True}
print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2012, 'Kristina']
print()
print_params(*values_list_2, 42)