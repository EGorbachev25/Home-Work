## ДЗ 7.1. Вітання
def say_hi(name, age) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"


name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
result = say_hi(name, age)
print(result)


## ДЗ 7.2. Модифікувати рядок

def correct_sentence(text):
    text = text.rstrip('.')
    corrected_text = text[0].upper() + text[1:]
    if not corrected_text.endswith('.'):
        corrected_text += '.'

    return corrected_text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')


## ДЗ 7.3. Пошук підрядка

def second_index(text, some_str):
    # Ищем первое вхождение some_str
    first_index = text.find(some_str)
    if first_index == -1:
        return None

    # Ищем второе вхождение some_str, начиная с позиции после первого вхождения
    two_index = text.find(some_str, first_index + 1)
    if two_index == -1:
        return None

    return two_index


print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))


### ДЗ 7.4. Пошук спільних елементів

def common_elements():
    multiples_of_3 = [i for i in range(100) if i % 3 == 0]

    multiples_of_5 = [i for i in range(100) if i % 5 == 0]

    set_of_3 = set(multiples_of_3)
    set_of_5 = set(multiples_of_5)

    common_set = set_of_3.intersection(set_of_5)
    return common_set


result = common_elements()
print("Common elements:", result)
