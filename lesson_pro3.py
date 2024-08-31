# Task 1
def sequence_generator(user_function, start_value, n):
    current_value = start_value
    count = 0

    while count < n:
        yield current_value
        current_value = user_function(current_value)
        count += 1


# Приклад використання

# Функція користувача, що визначає закон послідовності (наприклад, арифметична прогресія з кроком 2)
def user_function(x):
    return x + 2


# Створюємо генератор для послідовності з першим членом 1 і 5 членами послідовності
gen = sequence_generator(user_function, 1, 5)

# Виводимо елементи генератора
for number in gen:
    print(number)
# Task 2
def memoize(func):
    cache = {}  # Зберігає обчислені значення

    def memoized_func(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return memoized_func


# Простий рекурсивний підхід для обчислення n-го члена ряду Фібоначчі
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Використання мемоізації для прискорення функції
fibonacci_memoized = memoize(fibonacci_recursive)

# Порівняння швидкості виконання
import time

n = 35

# Замір часу для рекурсивної функції без мемоізації
start_time = time.time()
print(f"Рекурсивний підхід без мемоізації: Fibonacci({n}) = {fibonacci_recursive(n)}")
end_time = time.time()
print(f"Час виконання без мемоізації: {end_time - start_time:.5f} секунд")

# Замір часу для рекурсивної функції з мемоізацією
start_time = time.time()
print(f"Рекурсивний підхід з мемоізацією: Fibonacci({n}) = {fibonacci_memoized(n)}")
end_time = time.time()
print(f"Час виконання з мемоізацією: {end_time - start_time:.5f} секунд")
# Task 3
def apply_and_sum(numbers, user_function):
    # Застосовуємо функцію користувача до кожного елемента списку та зберігаємо результат в новий список
    transformed_numbers = [user_function(number) for number in numbers]

    # Обчислюємо суму оброблених елементів
    total_sum = sum(transformed_numbers)

    return total_sum


# Приклад використання

# Користувацька функція (наприклад, функція, що підносить до квадрату)
def square(x):
    return x ** 2


# Список чисел
numbers = [1, 2, 3, 4, 5]

# Виклик функції
result = apply_and_sum(numbers, square)
print(result)
