calls = 0

# Функция подсчета количества вызовов функций
def count_calls():
    global calls   #Глобальная переменная
    calls += 1

# Функция возвращает количество символов строки, строку в верхнем и нижнем регистре
def string_info(string):
    count_calls()
    string = (len(string),string.upper(),string.lower())
    return string

# Функция сравнивает строку со списком
def is_contains(string,list_to_search):
    count_calls()
    list_to_search = [x.upper() for x in list_to_search] # использование "включ. в послед-ть" для изм. регистра списка
    if string.upper() in list_to_search:
        return True
    else:
        return False

# Основная программа
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('UrbanModule3'))
print('Urban is contains in list: ', is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print('mIkhail is contains in list: ', is_contains('mIkhail', ['Aleksey', 'Andrey', 'Mikhail']))
print('cycle is contains in list: ', is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print('Количество вызовов функций: ', calls)