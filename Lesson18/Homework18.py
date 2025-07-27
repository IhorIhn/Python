#generators 1

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

#generators 2

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

#iterators 1

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

#iterators 2

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

#Decorators 1

def logger(func):
    def wrapper(a, b):
        print("Аргументи:", a, b)
        result = func(a, b)
        print("Результат:", result)
        return result
    return wrapper

@logger
def multiply (x,y):
   return x*y

multiply (3,5)

#Decorators 2

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виняток перехопили: {e}")
            return None
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))