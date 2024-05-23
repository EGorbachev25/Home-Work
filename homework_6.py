### ДЗ 6.1. Діапазон букв
import string


input_letters = input("Enter two letters separated by a hyphen: ")

start_symbol, end_symbol = input_letters.split('-')

all_letters = string.ascii_letters

start_index = all_letters.index(start_symbol)
end_index = all_letters.index(end_symbol)

result = all_letters[start_index:end_index + 1]

print(result)

### ДЗ 6.2. Конвертер із числа в дату

total_seconds = int(input("Enter the number of seconds (from 0 to 8639999): "))

# Проверяем, что введенное значение в допустимом диапазоне
if total_seconds < 0 or total_seconds >= 8640000:
    print("Error: The number of seconds must be in the range 0 to 8639999.")
else:
    # Вычисляем количество дней, часов, минут и секунд
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Форматируем часы, минуты и секунды с ведущими нулями
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    # Определяем правильное склонение слова "день"
    if days % 10 == 1 and days % 100 != 11:
        day_word = "day"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "days"
    else:
        day_word = "days"

    print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")

### ДЗ 6.3. Добуток чисел

number = int(input("Enter an integer: "))

while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    number = product

print(f"number ->", number)

