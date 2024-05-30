# def second_index(text, some_str):
#     if text.count(some_str) > 1:
#         return text.find(some_str, text.index(some_str) + 1)
#
#
# # print(second_index("sims", "s"))
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range)
# для 100 елементів, за наступними правилом:
#
# Один список з числами кратними 3, інший з кратними числами 5.
#
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
#
# Функція повинна повернути цю множину як результат своєї роботи.


# def common_elements():
#     first_numbers = [number for number in range(100) if number % 3 == 0]
#     second_numbers = [number for number in range(100) if number % 5 == 0]
#     return set(first_numbers).intersection(set(second_numbers))
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print("ok")
# print(common_elements())


####
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.


# def calc_numbers_pow(numbers: list[int], degree: int) -> list[int]:
#     return [number ** degree for number in numbers]
#
#
# print(calc_numbers_pow([1, 2, 3, 4, 5], 2))


##
# def delete_items_from_list(numbers: list[int], number_to_delete: int) -> int:
#     counter = 0
#     for number in numbers:
#         if number == number_to_delete:
#             numbers.remove(number_to_delete)
#             counter += 1
#
#     print(f"Result list: {numbers}")
#     return counter
#
#
# print(delete_items_from_list([1, 2, 1, 3, 4, 1, 5, 2], 1))  # 3

####
# def hello(): print("Hello")
#
#
# print(hello)
# message = hello  # надав посилання на функцію в іншу змінну
# print(message)
#
# hello()
# message()


##################
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def division(a, b): return a / b
#
#
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return add
#         case "-":
#             return sub
#         case "*":
#             return mult
#         case "/":
#             return division
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)


######
# message = lambda: print("Hello world!")
# message()
# print(message)
# print(lambda: print("Hello world!"))


####
# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))


# def calculate(a, b, math_operation) -> None:
#     print(f"Result: {math_operation(a, b)}")
#
#
# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(2, 5, lambda n1, n2: n1 / n2)

####
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return lambda a, b: a + b  # повернення посилання на функцію
#         case "-":
#             return lambda a, b: a - b
#         case "*":
#             return lambda a, b: a * b
#         case "/":
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

################
# LEGB - почитати
# https://www.bestprog.net/uk/2020/07/29/python-the-scopes-of-names-in-python-local-names-visibility-rules-for-names-legb-rule-the-global-keyword-overriding-names-in-functions-ua/

#####
# області видимості
# number = 10
#
#
# def test() -> None:
#     number: int = 11  # перекриття глобальної змінної
#
#     if 1:
#         number = 12
#
#         if 1:
#             number = 13
#             print(number)
#     print(number)
#
#
# print(number)
# test()
# print(number)
# number = 35
# print(number)

##########
# number = 10
#
#
# def test():
#     global number
#     number = 11  # змінюємо значення глобальної змінної
#     print(number)
#
#
# print(number)
# test()
# print(number)

#########
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()

#############
###
# number = 10
#
#
# def outer():
#     global number
#     number = 1
#     new_number = number
#
#     def inner():
#         global number
#         nonlocal new_number
#         new_number = 2
#         print(new_number)
#         number = 2
#
#         def inner_number_2():
#             global number
#             nonlocal new_number
#             new_number = 3
#             print(new_number)
#             number = 3
#
#         inner_number_2()
#
#     inner()
#     print(new_number)
#
#
# outer()
# print(number)

#####



