import time
import functools

def measure(func):
    """Декоратор для измерения времени выполнения функции."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution = end - start
        print(f"Функция '{func.__name__}' выполнена за {execution:.6f} секунд")
        return result
    return wrapper

@measure
def slow():
    time.sleep(1)
    return None

@measure
def fast():
    return sum(range(1000))

@measure
def sum_two_numbers(a, b):
    return a + b

print(slow())  
print(fast())  
print(sum_two_numbers(5, 10))  
