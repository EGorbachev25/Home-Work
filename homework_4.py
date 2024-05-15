### ДЗ 4.1. Перемістити всі нулі до кінця списку
## V1
# my_list = [5, 0, 12, 23, 0, 0, 25, 8, 0, 3]
# my_list.sort(key=bool, reverse=True)
# print(my_list)

#### V2
# nums = [5, 0, 12, 23, 0, 0, 25, 8, 0, 3]
#
# for num in nums:
#     if num == 0:
#         nums.remove(num)
#         nums.append(0)
#
# print(nums)


### ДЗ 4.2. Знайти суму елементів із парними індексами

# num = [0, 1, 7, 2, 4, 8]
#
# sum_even = sum(num[::2])
# result = sum_even * num[-1]
# print(result)

### ДЗ 4.3. Список із 3 елементів

# numbers = [1, 2, 3, 4, 5, 6, 7, 9]
#
# new_list = [numbers[0], numbers[2], numbers[-2]]
#
# print(new_list)


### V2
# import random
#
# # случайное количество элементов от 3 до 10
# n = random.randint(3, 10)
#
# # Создаем список случайных чисел
# random_numbers = [random.randint(1, 100) for _ in range(n)]
#
# # Создаем новый список из первого, третьего и второго из конца элементов
# new_list = [random_numbers[0], random_numbers[2], random_numbers[-2]]
#
# print("Initial list:", random_numbers)
# print("New list:", new_list)

