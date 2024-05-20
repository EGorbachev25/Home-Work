### ДЗ 5.1. Ім'я змінної


import string
import keyword

variable_name = input("Enter variable name: ")

# Предположим что имя переменной корректное
is_valid = True

# Проверяем, начинается ли строка с цифры
if variable_name[0].isdigit():
    is_valid = False

# Проверяем, содержит ли строка заглавные буквы или пробелы и знаки препинания (кроме "_")
for variable in variable_name:
    if variable in string.punctuation and variable != "_":
        is_valid = False
    if variable.isupper():
        is_valid = False
    if variable.isspace():
        is_valid = False

# Проверяем, является ли строка зарегистрированным словом
if variable_name in keyword.kwlist:
    is_valid = False

# Проверяем, что в имени переменной не более одного нижнего подчеркивания
if variable_name.count('_') > 1:
    is_valid = False

print(is_valid)

### ДЗ 5.2. Модифікувати калькулятор

while True:
    num1 = float(input("Enter first number: "))
    operator = input("Enter a symbol (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    match operator:
        case "+":
            result = num1 + num2
            print(result)

        case "-":
            result = num1 - num2
            print(result)

        case "*":
            result = num1 * num2
            print(result)

        case "/":
            if num2 != 0:
                result = num1 / num2
                print(result)
            else:
                print("Error: division by zero")
        case _:
            print("Error: Invalid operation")

    continue_calculation = input("Do you want to perform another calculation? (yes/y to continue): ").lower()
    if continue_calculation != "yes" and continue_calculation != "y":
        break



### ДЗ 5.3. hashtag

import string

user_input = input("Enter the string: ")

# Удаляем знаки препинания и разделяем строку на слова
words = user_input.translate(str.maketrans('', '', string.punctuation)).split()

# Преобразуем каждое слово в хэштег
hashtag = '#' + ''.join(word.capitalize() for word in words)

# Обрезаем хэштег, если его длина превышает 140 символов
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)

