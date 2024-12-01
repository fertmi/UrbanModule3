#Функция поиска однокоренных слов
def single_root_words(root_word, *other_words):
    same_words = [x for x in other_words if x.upper() in root_word.upper() or root_word.upper() in x.upper()]
    return same_words

#Основная программа
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'RicHies')
result2 = single_root_words('Disablement', 'ABLe', 'Mable', 'DisabLe', 'Bagel')
print(result1)
print(result2)