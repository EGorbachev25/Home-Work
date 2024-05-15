###
# Цикли
# - while
# - for

# v1
# i = 0
#
# while i < 10:
#     print(i, end=" ")
#     i += 1  # i = i + 1
#
#
# print("test")
#
# v2
# i = 12
#
# while True:
#     print(i)
#     i += 2

# v3
# i = 0
#
# while True:
#
#     if i == 5:
#         print("continue...")
#         i += 1
#         continue  # пропустить подальші дії циклу, але цикл не зупиниться
#
#     if i >= 10:
#         print("break...")
#         break  # цикл зупиниться (повне завершення циклу)
#
#     print(i)
#     i += 1

###
# for i in range(5):
#     print("Hello")
#     # print(i, end=" ")


# nums = [1, 2, 4, 2, 56]
#
# for i in range(len(nums)):
#     print(nums[i])


# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
#
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
#
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
#
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.

# numbers = []
# result_list = []
#
# nums_len = len(numbers)
# middle_index = nums_len // 2
# print(middle_index)
# if nums_len == 0:
#     result_list.append([])
#     result_list.append([])
#     print(result_list)
# elif nums_len % 2 != 0:
#     nums1 = numbers[:middle_index + 1]
#     nums2 = numbers[middle_index + 1:]
#     result_list.append(nums1)
#     result_list.append(nums2)
#     print(result_list)
# else:
#     nums1 = numbers[:middle_index]
#     nums2 = numbers[middle_index:]
#     result_list.append(nums1)
#     result_list.append(nums2)
#     print(result_list)


