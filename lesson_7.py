# def say_hello():
#     print("Hello")
#
#
# number = 10
# print(number)
# print(say_hello)
# say_hello()  # виклик функції (функція починає працювати)
# say_hello()
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)
#
#
# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
# #


# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# user_hobby = input("Enter your hobby: ")
# user_info(name, age, user_hobby)
#
# user_info("Petya", 123, user_hobby)


########
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)

# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів

# def add(n1, n2): return n1 + n2
#
#
# def sub(n1, n2): return n1 - n2
#
#
# def mult(n1, n2): return n1 * n2
#
#
# def division(n1, n2): return n1 / n2
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             if second_number == 0:
#                 print("Cannot divide by zero")
#             else:
#                 print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             print("Invalid math operation!")
#
#
# # calculate()
# result = add(1, 3)
# print(result)

###

# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# user_info("Vasya", 33, "test")
# user_info("Vasya", 33)
# user_info("Vasya")
#
# user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
## Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
# print_person(name="Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)

#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

########

# def correct_sentence(text):
#     text_end = ""
#     if text[-1] != ".":
#         text_end = "."
#
#     return text[0].upper() + text[1:] + text_end
#
#
# # print(correct_sentence("greetings, friends"))
# print(correct_sentence("greetings, friends"))
# print(correct_sentence("hello"))
# print(correct_sentence("Greetings. Friends"))
# print(correct_sentence("Greetings, friends."))
# print(correct_sentence("greetings, friends."))

#####
# 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.
# import random
#
#
# def create_list_with_random_numbers(list_length=10, start_value=1, end_value=5) -> list[int]:
#     return [random.randint(start_value, end_value) for _ in range(list_length)]
#
#
# def remove_duplicates(numbers: list[int]) -> list[int]:
#     return list(set(numbers))
#
#
# def get_unique_numbers(numbers: list[int]) -> list[int]:
#     unique_numbers = []
#     for number in numbers:
#         if numbers.count(number) == 1:
#             unique_numbers.append(number)
#
#     return unique_numbers
#
#
# my_numbers = create_list_with_random_numbers()
# print(my_numbers)
# my_numbers_without_duplicates = remove_duplicates(my_numbers)
# print(my_numbers_without_duplicates)
# unique_numbers = get_unique_numbers(my_numbers)
# print(unique_numbers)
