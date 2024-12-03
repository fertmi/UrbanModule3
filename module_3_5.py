#Функция рекурсивное умножение цифр
def get_multiplied_digits(number):
    str_number = str(number)        # перевод числа в строку
    first = int(str_number[0])      # first присваиваем первую цифру
    if len(str_number) > 1 and int(str_number[1:]) > 0:         # если длина числа > 1 и срез больше 0 (для исключения умножения на 0)
        return first * get_multiplied_digits(int(str_number[1:])) # вызываем функцию со срезом: со второго числа и умножаем на первое
    else:
        return first                # если осталась 1 цифра возвращаем это число

#Основная программа
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result3 = get_multiplied_digits(1000040010005)
print(result3)