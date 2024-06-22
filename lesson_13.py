# Обробка винятків

# v1
# n1, n2 = 10, 0 # множинне привласнення
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

# v2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:  # Exception -> базовий тип виключення пишемо останнім з except
#     print(f"Exception occurred: {error}")
# finally:  # Відпрацьовує завжди. Писати по потребі
#     print("End of calculation")
#
# print("some text")

####
# try:
#     name = input("Enter you name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")  # raise -> згенерувати виняток (кинути виняток)
# except Exception as e:
#     print(f"Error: {e}")


# У Python є такі базові типи винятків:
#
# BaseException: базовий тип для всіх вбудованих винятків
#
# Exception: базовий тип, який зазвичай застосовується для створення своїх типів винятків
#
# ArithmeticError: базовий тип для винятків, пов'язаних з арифметичними операціями
# (OverflowError, ZeroDivisionError, FloatingPointError).
#
# BufferError: Виняток, який виникає при неможливості виконати операцію з буфером
#
# LookupError: базовий тип для винятків, які виникають під час звернення до колекцій
# за некоректним ключем або індексом (наприклад, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: виняток виникає, якщо індекс при зверненні до елемента колекції знаходиться поза допустимим діапазоном
#
# KeyError: виникає, якщо у словнику немає ключа, за яким відбувається звернення до елемента словника.
#
# OverflowError: виникає, якщо результат арифметичної операції не може бути представлений поточним
# Чисельним типом (зазвичай типом float).
#
# RecursionError: виникає, якщо перевищено допустиму глибину рекурсії.
#
# TypeError: якщо операція або функція застосовується до значення неприпустимого типу.
#
# ValueError: виникає, якщо операція або функція одержують об'єкт коректного типу з некоректним значенням.
#
# ZeroDivisionError: виникає при розподілі на нуль.
#
# NotImplementedError: тип виключення для вказівки, що якісь методи класу не реалізовані
#
# ModuleNotFoundError: виникає при неможливості знайти модуль при його імпорті директивою import
#
# OSError: тип винятків, які генеруються при виникненні помилок системи (наприклад, неможливо знайти файл,
# пам'ять диска заповнена і т.д.)

############
##
# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени

# import os
# import sys
#
# CONTACTS_FILE_PATH = "contacts.txt"
#
#
# def get_contacts(path_to_file: str) -> list[str]:
#     if os.path.exists(path_to_file):
#         with open(path_to_file, "r", encoding="utf-8") as file:
#             return file.readlines()
#     raise FileNotFoundError(f"File {path_to_file} not found!")
#
#
# def show_contacts(contacts: list[str]) -> None:
#     if len(contacts) == 0:
#         raise Exception("No contacts found!")
#
#     all_contacts = ""
#     for i in range(len(contacts)):
#         all_contacts += str(i + 1) + ". " + contacts[i]
#
#     print(f"Current contacts book:\n{all_contacts}")
#
#
# def add_contact(path_to_file: str, contact: dict) -> None:
#     with open(path_to_file, "a", encoding="utf-8") as file:
#         file.write(contact.get("name") + " - " + contact.get("phone") + "\n")
#
#
# def modify_contact(path_to_file: str, contact: dict, contact_phone: str) -> None:
#     current_contacts = get_contacts(path_to_file)
#     for i in range(len(current_contacts)):
#         if current_contacts[i].find(contact_phone) != -1:
#             current_contacts[i] = contact.get("name") + " - " + contact.get("phone") + "\n"
#
#     with open(path_to_file, "w", encoding="utf-8") as file:
#         file.writelines(current_contacts)
#
#
# def delete_contact(path_to_file: str, contact_phone: str) -> None:
#     current_contacts = get_contacts(path_to_file)
#     for contact in current_contacts:
#         if contact.find(contact_phone) != -1:
#             current_contacts.remove(contact)
#
#     with open(path_to_file, "w", encoding="utf-8") as file:
#         file.writelines(current_contacts)
#
#
# def search_contact_by_name(path_to_file: str, contact_name: str) -> list[str]:
#     found_contacts = []
#     current_contacts = get_contacts(path_to_file)
#     for i in range(len(current_contacts)):
#         if current_contacts[i].find(contact_name) != -1:
#             found_contacts.append(current_contacts[i])
#
#     return found_contacts
#
#
# def main():
#     while True:
#         user_select = int(input("\n1. Add contact"
#                                 "\n2. Modify contact"
#                                 "\n3. Delete contact"
#                                 "\n4. Get all contacts"
#                                 "\n5. Search contact by name"
#                                 "\n6. Exit\n"))
#         match user_select:
#             case 1:
#                 test_contact: dict = {
#                     "name": input("Enter contact's name: "),
#                     "phone": input("Enter contact's phone number: ")
#                 }
#                 add_contact(CONTACTS_FILE_PATH, test_contact)
#             case 2:
#                 phone_number_to_update = input("Enter contact's phone to update: ")
#                 updated_test_contact: dict = {
#                     "name": input("Enter updated contact's name: "),
#                     "phone": input("Enter updated contact's phone number: ")
#                 }
#                 modify_contact(CONTACTS_FILE_PATH, updated_test_contact, phone_number_to_update)
#             case 3:
#                 phone_number_to_delete = input("Enter contact's phone to delete: ")
#                 delete_contact(CONTACTS_FILE_PATH, phone_number_to_delete)
#             case 4:
#                 all_contacts = get_contacts(CONTACTS_FILE_PATH)
#                 show_contacts(all_contacts)
#             case 5:
#                 contact_name = input("Enter contact's name to find: ")
#                 found_contacts_data = search_contact_by_name(CONTACTS_FILE_PATH, contact_name)
#                 show_contacts(found_contacts_data)
#             case 6:
#                 sys.exit()
#             case _:
#                 raise ValueError("You selected incorrect menu item!")
#
#
# try:
#     main()
# except FileNotFoundError as error:
#     print(error)
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)


# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.

# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації


# успадкування
# v1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# v1
# class Employee(Person):  # успадковуємося від класу Person
#     def work(self):
#         print(f"{self.name} works!")
#
#
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()


# v2
# class Employee(Person):
#     def __init__(self, name, age, company):
#         # v1
#         super().__init__(name, age)  # виклик конструктора базового класу Person
#         # super() -> посилання на базовий клас, отримуємо доступ до елементів базового класу
#         # v2
#         # Person.__init__(self, name, age)
#         self.company = company
#
#     # перевизначення методу
#     def show_info(self):
#         super().show_info()  # виклик методу базового класу
#         print(f"Works in {self.company} company")  # розширили своєю логікою
#
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()


# Створити ієрархію класів для опису академії.
#
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.

############
# v3
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print(f"{self.name} works!")
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name} studies!")
#
#
# class WorkingStudent(Student, Employee):  # множинне спадкування
#     pass
#
#
# vasya = WorkingStudent("Vasya")
# vasya.work()
# vasya.study()
# print(WorkingStudent.mro())

# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]
