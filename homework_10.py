### ДЗ 10.1. Генераторна функція
def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    current = begin
    count = 0
    while count < end:
        yield current
        current = func(current)
        count += 1


def pow(x):
    return x ** 2


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

### ДЗ 10.2. Знайти перше слово
import re


def first_word(text):
    """ Пошук першого слова """

    match = re.search(r'\b[\w\']+\b', text)
    return match.group(0) if match else None


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')


### ДЗ 10.3. Перевірити чи є парним чи ні

def is_even(digit):
    """ Перевірка чи є парним число """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
