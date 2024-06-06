# def additional_logic(func):
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Some logic 2")
#     return wrapper
#
#
# @additional_logic
# def hello():
#     print("Hello")
#
#
# hello()


####
# def check_permissions(func):
#     def wrapper(role):
#         if role == 'admin':
#             print("Permissions granted!")
#             func(role)
#         else:
#             print("Permission denied!")
#     return wrapper
#
#
# @check_permissions
# def get_secret_information(user_role):
#     print(f"Hi {user_role}, this is secret information.")
#
#
# get_secret_information("user")
# get_secret_information("admin")

####
# def start(func):
#     def wrapper(name):
#         print("Hello ", end="")
#         func(name)
#     return wrapper
#
#
# def end(func):
#     def wrapper(name):
#         print("Goodbye ", end="")
#         func(name)
#     return wrapper
#
#
# @start
# @end
# def hello(name):
#     print(name)
#
#
# hello("Vasya")

###
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")

####
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
# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             my_gen.close()
#             # my_gen.throw(Exception("End!"))
# except Exception as e:
#     print(e)

####
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених
# випадковим чином і знаходить позицію, з якої починається послідовність з 10 чисел, сума яких мінімальна.
# import math
# import random
#
#
# def find_min_sum_index(numbers: list[int], start_index, end_index, min_sum=math.inf, min_index=0):
#     if end_index < len(numbers):
#         current_sum = sum(numbers[start_index:end_index+1])
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_index = start_index
#
#         start_index += 1
#         end_index += 1
#
#         print(f"Current sum: {current_sum} and Min sum: {min_sum}")
#
#         return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)
#
#     return min_index
#
#
# nums = [random.randint(1, 10) for _ in range(4)]
# print(nums)
# result = find_min_sum_index(nums, 0, 1)
# print(result)

###
# \d - відповідає будь-якій одній цифрі і замінює собою вираз [0-9];
# \D - виключає всі цифри та замінює [^0-9];
# \w - Замінює будь-яку цифру, букву, а також знак нижнього підкреслення;
# \W - будь-який символ крім латиниці, цифр або нижнього підкреслення;
# \s - відповідає будь-якому пробельного символу;
# \S - описує будь-який непробільний символ.
#
#
# . Один символ, крім нового рядка \n.
# ? 0 або 1 входження шаблону зліва
# + 1 і більше входжень шаблону зліва
# * 0 і більше входжень шаблону зліва
# \w Будь-яка цифра або буква (\W - все, крім букви або цифри)
# \d Будь-яка цифра [0-9] (\D - все, крім цифри)
# \s Будь-який символ пробілу (\S - будь-який символ пробілу)
# \b Кордон слова
# [..] Один із символів у дужках ([^..] — будь-який символ, крім тих, що у дужках)
# \ Екранування спеціальних символів (\. означає точку або \+ - знак "плюс")
# ^ і $ Початок і кінець рядка відповідно
# {n,m} Від n до m входжень ({,m} - від 0 до m)
# a|b Відповідає a або b
# () Групує вираз і повертає знайдений текст
# \t, \n, \r Символ табуляції, нового рядка та повернення каретки відповідно
#
# Для чого використовуються регулярні вирази
# для визначення потрібного формату, наприклад, телефонного номера або email-адреси;
# для розбивки рядків на підрядки;
# для пошуку, заміни та вилучення символів;
# для швидкого виконання нетривіальних операцій.
#
# А ось найбільш популярні методи, які надає модуль:
#
# re.match() - Цей метод шукає за заданим шаблоном на початку рядка
# re.search() - Метод схожий на match(), але шукає не лише на початку рядка
# re.findall() - Повертає список усіх знайдених збігів.
# У методу findall() немає обмежень на пошук на початку або в кінці рядка.
# re.split() - Цей метод поділяє рядок за заданим шаблоном
# re.sub() - Шукає шаблон у рядку і замінює його на вказаний підрядок.
# Якщо шаблон не знайдено, рядок залишається незмінним
# re.compile() - Ми можемо зібрати регулярне вираження в окремий об'єкт, який можна використовувати для пошуку.
# Це також позбавляє переписування одного і того ж виразу.

# import re

# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))
# #
# #
# result = re.search(r'world', 'hello world hello')
# print(result.start())
# print(result.end())
# #
# #
# result = re.findall(r'he', 'hello world hello')
# print(result)
# #
# #
# result = re.split(r'l', 'hello world hello', maxsplit=1)
# print(result)
# #
# result = re.split(r'l', 'hello world hello')
# print(result)
# #
# #
# pattern = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)

# result = re.findall(r'.', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w*', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+$', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'^\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\b\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'@\w+.\w+', "test1@gmail.com, test2@qqq.com, test3@www.com")
# print(result)
#
# result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
# print(result)
#
# result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-017-2004')
# print(result)

# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# - домашній номер телефону (тільки цифри та довжина номера)
#
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
#
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
#
# додатково:
#
# - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ,
# довжина пароля – від 8 до 16 символів)
