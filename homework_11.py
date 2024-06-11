### ДЗ 11.1. Генератор простих чисел

def prime_generator(end):
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    for number in range(2, end + 1):
        if is_prime(number):
            yield number


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


## ДЗ 11.2. Заповнення списку кубами чисел

def generate_cube_numbers(end):
    number = 2
    while True:
        cube = number ** 3
        if cube >= end:
            return
        yield cube
        number += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], '10 у кубі це 1000'
print('Ok')


### ДЗ 11.3. Перевірка на парність.

def is_even(number):
    return (number & 1) == 0


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok')
