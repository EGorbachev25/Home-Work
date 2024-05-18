# Додаткові завдання по матрицях:
#
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
#
# вивести на екран
#
# - вивести суму чисел головної діагоналі матриці
#
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
#
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
#
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

#####################################################

# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!

# numbers = [1, 0, 2, 0, 4, 0, 1, 6, 9]
# new_numbers = []
#
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         new_numbers.append(numbers[i])
#
# print(new_numbers)
#
# count_zeros = numbers.count(0)
#
# print(count_zeros)
#
# for _ in range(count_zeros):
#     new_numbers.append(0)
#
# print(numbers)
# print(new_numbers)

#####
# numbers = [1, 0, 2, 0, 4, 0, 1, 6, 9]
#
# my_sum = 0
#
# # сумма четных чисел
# for number in numbers:
#     if number % 2 == 0:
#         my_sum += number
#
# print(my_sum)
#
# # сумма чисел по четным индесам
# my_sum = 0
#
# # сумма четных чисел
# for index in range(len(numbers)):
#     if index % 2 == 0:
#         my_sum += numbers[index]
#
# print(my_sum)

# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

# import random
#
# numbers = []
#
# # v1
# numbers_len = random.randint(3, 10)
# for _ in range(numbers_len):
#     numbers.append(random.randint(3, 10))
#
# print(numbers_len)
# print(numbers)
#
# # v2
# numbers = [random.randint(3, 10) for _ in range(numbers_len)]
# print(numbers_len)
# print(numbers)
#
# result_numbers = [numbers[0], numbers[2], numbers[-2]]
# print(result_numbers)

####
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i * j, end=" ")
#         j += 1
#     print()
#
#     i += 1

#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()

####
# for value in 1, 3, "qwer", 12.5, True, 1234:
#     print(value)

#
# for i in range(5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(end, start - 1, -1):
#     # print("Hello")
#     print(i, end=" ")

######
# Показати на екран усі прості числа в діапазоні, вказаному користувачем.
# Число називається простим, якщо воно ділиться без залишку тільки на себе і на одиницю.
# Наприклад, три - це просте число, а чотири - ні.

# start = int(input("Enter start value: "))
# end = int(input("Enter end value: "))
#
# # v1
# if start > end:
#     start, end = end, start

# # v2
# if start > end:
#     temp = start
#     start = end
#     end = temp

# for number in range(start, end + 1):
#     is_simple = True
#
#     if number < 2:
#         continue
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
#
#     if is_simple:
#         print(number, end=" ")

# #####
# # v1
# numbers = [number for number in range(-10, 10) if number % 2 != 0]
# print(numbers)
#
# # v2
# numbers = []
#
# for number in range(-20, 20):
#     if number % 2 != 0:
#         numbers.append(number)
#
# print(numbers)

####################################
###
# message = "hello world"
# # [] -> індексатори
# # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

###
# # string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
#
# # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# # slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)
#
#
# text = "Hello, world" * 3
# print(text)
#
# print("---" * 10)

# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(99))

####
# text = "helLo woRlD"
#
# # isalpha(): повертає True, якщо рядок складається лише з алфавітних символів
#
# print(text.isalpha())
#
# # islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі
#
# print(text.islower())
#
# # isupper(): повертає True, якщо всі символи рядка у верхньому регістрі
#
# print(text.isupper())
#
# # isdigit(): повертає True, якщо всі символи рядка - цифри
#
# print(text.isdigit())
#
# # isnumeric(): повертає True, якщо рядок є числом
#
# print(text.isnumeric())
#
# # startswith(str): повертає True, якщо рядок починається з підрядка str
#
# print(text.startswith("helLo"))
#
# # endswith(str): повертає True, якщо рядок закінчується на підрядок str
#
# print(text.endswith("D"))
#
# # lower(): перекладає рядок у нижній регістр
#
# print(text.lower())
#
# # upper(): перекладає рядок у верхній регістр
#
# print(text.upper())
#
# # title(): початкові символи всіх слів у рядку перекладаються у верхній регістр
#
# print(text.title())
#
# # capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
#
# print(text.capitalize())
#
# fio = input("Enter fio: ").title()
# print(fio)
#
#
# # lstrip(): видаляє початкові пробіли з рядка
# text = "helLo woRlD"
# print(text)
# print(text.lstrip())
#
# # rstrip(): видаляє кінцеві пробіли з рядка
# print(text)
# print(text.rstrip())
#
# # strip(): видаляє початкові та кінцеві пробіли з рядка
# print(text)
# print(text.strip())
#
# # ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється праворуч
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): якщо довжина рядка менша за параметр width,
# # то ліворуч і праворуч від рядка рівномірно додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))
#
# # find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
# text = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
#
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
#
# print(text.find("p"))  # -1
# #
# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

#

# # # replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)


#####
# import string
# import random
#
# DATA_FOR_PASSWORD = string.ascii_letters + string.digits + string.punctuation
# MIN_PASSWORD_LENGTH = 8
# MAX_PASSWORD_LENGTH = 16
#
#
# while True:
#     password = ""
#
#     while True:
#         pass_len = int(input(f"Enter password length from {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}: "))
#
#         if pass_len > MAX_PASSWORD_LENGTH or pass_len < MIN_PASSWORD_LENGTH:
#             print(f"Password must be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}")
#         else:
#             break
#
#     for _ in range(pass_len):
#         password += random.choice(DATA_FOR_PASSWORD)
#
#     print(password)
#
#     user_choice = input("Press 'q' for exit\n")
#
#     if user_choice == "q":
#         break
