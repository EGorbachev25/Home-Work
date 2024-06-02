### ДЗ 9.1. Визначити популярність певних слів у тексті
def popular_words(text, words):
    # Приводим текст в нижний регистр и разбиваем на отдельные слова
    text = text.lower()
    words_list = text.split()

    # Создаем словнік для считывания результатов
    result = {word: 0 for word in words}

    # Считаем количество появлений каждого слова из списка words
    for word in words:
        result[word] = words_list.count(word)

    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')


### ДЗ 9.2. Різниця між числами

def difference(*args):
    if not args:
        return 0

    max_value = max(args)
    min_value = min(args)
    result = max_value - min_value

    return round(result, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
