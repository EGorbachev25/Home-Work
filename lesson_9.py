# Рекурсія – коли функція викликає сама себе
# 1. продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. визначити умову або умови виходу з рекурсії
# 3. запустити рекурсію (виклик цієї ж функції)

# 5! => 1 * 2 * ... * 5
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсії
#     return number * factorial(number - 1)


print(factorial(5))
#
#
# factorial(5) -> 5 * factorial(4) => 120
# factorial(4) -> 4 * factorial(3) => 24
# factorial(3) -> 3 * factorial(2) => 6
# factorial(2) -> 2 * factorial(1) => 2
# factorial(1) => 1

# Написати рекурсивну функцію знаходження ступеня числа.

# def my_pow(base, exponent):
#     if exponent <= 1:
#         return base
#
#     return base * my_pow(base, exponent-1)
#
#
# print(my_pow(2, 3))
# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2

####
# f(n) = f(n-1) + f(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# def fib(number):
#     if number == 0 or number == 1:
#         return number
#
#     return fib(number - 1) + fib(number - 2)


# for i in range(10):
#     print(fib(i), end=" ")

##############

# def test_func(num1, *args, number=100):
#     print(args)
#     print(type(args))
#     print(num1)
#     print(number)
#
#
# test_func(1, 2, 3, 4, 5, 6, 7, 8, number=12)


# def test_func(number, **kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     print(number)
#
#
# test_func(123, num1=11, num2=33, num4=1111)

###
# def test_func(number, *args, test=10, **kwargs):
#     print(number)
#     print(args)
#     print(test)
#     print(kwargs)
#
#
# test_func(100, 1, 2, 3, 4, test=123, num1=11, num2=33, num4=1111)

######
# def test_func(num1, num2, num3):
#     print((num1 + num2 + num3) / 3)
#
#
# numbers = [1, 2, 3]
# # v1
# test_func(numbers[0], numbers[1], numbers[2])
# # v2
# test_func(*numbers)

####
# def auth(username, password, secrets):
#     if username == 'admin' and password == '12345' and secrets == '12345':
#         print("Logged in successfully")
#     else:
#         print("Fail")
#
#
# def get_auth_data():
#     return {
#         'username': 'admin',
#         'password': '12345',
#         'secrets': '12345'
#     }
#
#
# auth_data = get_auth_data()
# auth(auth_data.get("username"), auth_data.get("password"), auth_data.get("secrets"))
# auth(**auth_data)

#####

# Генератори колекцій
# list comprehension

# newlist = [expression for item in iterable (if condition)]

# iterable: джерело даних, що перебирається, в якості якого може виступати список, безліч, послідовність,
# або навіть функція, яка повертає набір даних, наприклад, range()
#
# item: елемент, що витягується з джерела даних
#
# expression: вираз, який повертає певне значення. Це значення потім потрапляє в список, що генерується
#
# condition: умова, якій повинні відповідати елементи, що витягуються з джерела даних.
# Якщо елемент НЕ задовольняє умову, він не вибирається. Необов'язковий параметр.

# # v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive = []
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)
# #
# # # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)
#
# #
# nums = [n for n in range(10)]
# print(nums)
#
# #
# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)
#
# #
# users = {1: 'John', 2: 'Peter', 3: 'Max'}
# names = [name for name in users.values()]
# print(names)
#
# #
# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# new_numbers = [num * 2 if num > 5 else num for num in numbers if num > 0]
# print(new_numbers)
#
# # #
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)
#
# #
# my_set = {i for i in range(10)}
# print(my_set)

################
# Генераторні функції
# Генератор - це об'єкт, який відразу при створенні не обчислює значення всіх своїх елементів
# generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # StopIteration
# close() -> зупинка генератора
# throw() -> генератор кине виняток

# for i in generator:
#     print(i)


# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# my_gen = create_generator()
# print(my_gen)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# my_gen.close()
# print(next(my_gen))

# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             # my_gen.close()
#             my_gen.throw(Exception("End!"))
# except Exception as e:
#     print(e)

#####
# https://www.programiz.com/python-programming/methods/built-in/abs

# Замикання (closure) представляє функцію, яка запам'ятовує своє лексичне оточення навіть у тому випадку,
# коли вона виконується поза своєю областю видимості.

# Зовнішня функція, яка визначає деяку область видимості і в якій визначені деякі
# Змінні та параметри - лексичне оточення
#
# Змінні та параметри (лексичне оточення), які визначені у зовнішній функції
#
# вкладена функція, яка використовує змінні та параметри зовнішньої функції

# def outer():
#     number = 10
#     print("outer")
#     test = 10
#     test_2 = 111
#
#     def inner():
#         nonlocal number
#         number += 1
#         # print(test)
#         print(number)
#         # print("hello")
#
#     return inner
#
#
# inner_func = outer()
# inner_func()
# inner_func()
# inner_func()

####
# def multiply(number1, number2):
#     print(number1 * number2, end=" ")
#
#
# for i in range(1, 11):
#     multiply(2, i)

###
# def multiply(number1): return lambda number2: number1 * number2
#
#
# mult_by_2 = multiply(2)
# for i in range(1, 11):
#     print(mult_by_2(i), end=" ")

###
# def greeting(text):
#     def sentence_end(symbol):
#         def customer_name(name):
#             print(text + name + symbol)
#         return customer_name
#     return sentence_end
#
#
# # greeting("Hello, ")("!")("Vasya")
# # greeting("Hello, ")(".")("Petya")
# main_greeting_func = greeting("Hello, ")("!")
#
# users = ["Vasya", "Petya", "Anton"]
#
# for user in users:
#     main_greeting_func(user)
