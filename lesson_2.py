# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних: True False
# str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативної пам'яті значення можна змінювати
# number: int = 10
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

###
# print(number := 10)  # моржовый оператор

###
# userName1 = "Vasya"
# print(userName1)
# user_name = "Petya"
# print(user_name)
###

######
# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3)  # основа ** показник (зведення в ступінь)
# print(2 // 3)  # ціла частина від розподілу
# print(2 % 3)  # залишок від ділення
#
# num1 = 15
# num2 = 8
# print(num1 // num2)
# print(num1 % num2)

############
# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %

# number = int(input("Enter a number: "))
# n1 = number // 100
# # v1
# # n2 = number // 10 % 10
# # v2
# n2 = number % 100 // 10
# n3 = number % 10
#
# print(n1)
# print(n2)
# print(n3)
#
# result = n1 + n2 + n3
# print("Result:", result)

###
# input -> буде очікувати на введення даних з клавіатури в
# консолі і поверне за замовчуванням значення типу даних str

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # v1
# print("Hello,", name, "You are", age, "years old!")
# # v2 конкатенація - складання рядків. Рядок + рядок -> один великий рядок
# print("Hello, " + name + " You are " + str(age) + " years old!")
# # v3 інтерполяція рядка - вбудовування змінних у рядок завдяки функції format (вивчимо докладніше пізніше)
# print(f"Hello, {name}. You are {age} years old!")
#
# age_after_ten_years = age + 10
# print(age_after_ten_years)

####
# number = int(input('Enter a number: '))  # 56198
#
# n1 = 5
# n2 = 6
# n3 = 1
# n4 = 9
# n5 = 8
#
# result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
# print(result)

####
# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
#
# numbers_sum = number1 + number2 + number3
# numbers_multiplication = number1 * number2 * number3
# print(f"The sum of the numbers: {numbers_sum}")
# print(f"The multiplication of the numbers: {numbers_multiplication}")

###
#  Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.

first_diagonal = int(input("Enter first diagonal: "))
second_diagonal = int(input("Enter second diagonal: "))
area = first_diagonal * second_diagonal / 2
print(f"The area of the rhombus: {area}")
