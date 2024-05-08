# ДЗ 2.1. Виведення числа в стовпчик

number = int(input("Enter a 4-digit number: "))

print("Result: ")
print(number // 1000)
print((number % 1000) // 100)
print((number % 100) // 10)
print(number % 10)

# ДЗ 2.2. Необхідно "перевернути" 5-ти значне число

number = int(input("Enter a 5-digit positive integer: "))

reversed_number = (number % 10) * 10000 + (number % 100 // 10) * 1000 + (number % 1000 // 100) * 100 +(number // 1000 % 10) * 10 + (number // 10000)
print("Reversed number: ", reversed_number)