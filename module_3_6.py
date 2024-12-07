#Функция - универсальное решение для подсчёта суммы всех чисел и длин всех строк
def calculate_structure_sum(structure, sum):
    for item in structure:
        if isinstance(item, str): #Если строка
           sum += len(item)
        elif isinstance(item, int): #Если целое число
            sum += item
        elif isinstance(item, (list, tuple, set)): #Если список, кортеж, множество
            sum = calculate_structure_sum(item,sum)
        elif isinstance(item, dict): #Если словарь
            sum = calculate_structure_sum(item.keys(),sum)
            sum = calculate_structure_sum(item.values(),sum)
    return sum

#Основная программа
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure,0)
print(result)