### ДЗ 3.1. Найпростіший калькулятор

num1 = float(input("Enter first number: "))
operator = input("Enter a symbol  (+,-,*,/): ")
num2 = float(input("Enter second number: "))


if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: division by zero")
else:
    print("Error: Invalid operation")

### ДЗ 3.2. Перемістити елемент у списку
#v1
my_list = [1, 2, 3, 4, 5]
other_list = my_list.pop()
print(my_list)
my_list.insert(0, other_list)
print(my_list)

### v2
my_list = [12, 3, 4, 10, 8]

if len(my_list) > 1:
    my_list = [my_list[-1]] + my_list[:-1]

print(my_list)

### ДЗ 3.3. Розділити один список на два списки

input_list = [1, 2, 3, 4, 5, 6]

if len(input_list) == 0:
    result = [[], []]

elif len(input_list) % 2 == 0:
    middle = len(input_list) // 2
    list_1 = input_list[:middle]
    list_2 = input_list[middle:]
    result = [list_1, list_2]

else:
    middle = len(input_list) // 2 + 1
    list_1 = input_list[:middle]
    list_2 = input_list[middle:]
    result = [list_1, list_2]

print(result)

