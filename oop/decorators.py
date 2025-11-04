import time
import functools
"""
@timer
def slow_function(n):
time.sleep(n)
return f"Slept for {n} seconds"
result = slow_function(2)
# Output: [TIMER] Function 'slow_function' executed in 2.0023 seconds
print(result)
# Output: Slept for 2 seconds
# Logger decorator
@logger
def add(a, b):
return a + b
result = add(5, 3)
# Output: [LOGGER] Calling function 'add' with args=(5, 3), kwargs={}
# Output: [LOGGER] Function 'add' returned: 8
# Count calls decorator
@count_calls
def greet(name):
return f"Hello, {name}!"
greet("Alice")
greet("Bob")
greet("Charlie")
print(f"Total calls: {greet.call_count}")
Hints:
Import time module for timing
Use time.time() or time.perf_counter()
Use functools.wraps(func) to preserve function metadata
Store call count as function attribute
Decorator structure: def decorator(func): def wrapper(*args, **kwargs): ...
return wrapper
Bonus Challenge:
Create a @slow_down(seconds) decorator that adds a delay before function execution.
Problem 5: E-commerce Product System (OOP -
Intermediate)
# Output: Total calls: 3
# Debug decorator
@debug
def calculate_average(numbers):
return sum(numbers) / len(numbers)
result = calculate_average([10, 20, 30, 40])
# Output: [DEBUG] Calling 'calculate_average'
# Output: [DEBUG] args: ([10, 20, 30, 40],)
# Output: [DEBUG] kwargs: {}
# Output: [DEBUG] 'calculate_average' returned: 25.0
# Stack multiple decorators
# Stack multiple decorators
@timer
@logger
def multiply(x, y):
return x * y
result = multiply(4, 5)
# Output: [LOGGER] Calling function 'multiply' with args=(4, 5), kwargs={
# Output: [LOGGER] Function 'multiply' returned: 20
# Output: [TIMER] Function 'multiply' executed in 0.0001 seconds
"""
def timer(original):
    @functools.wraps(original)
    def wrapper(*l, **kl):
        print(f"now go to {l}")
        r= original(*l,*kl)
        print(f"finished ")
        return r
    return wrapper
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling function '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
def count_calls(originalfunction):
    @functools.wraps(originalfunction)
    def wrapper(*args):
        wrapper.cont+=1
        print(f"{wrapper.cont} {originalfunction.__name__} has been called {wrapper.cont}")
        return originalfunction(*args)
    wrapper.cont=0
    return wrapper
def debug(orig):
    @functools.wraps(orig)
    def wrapper(*args):
        print(f"[DEBUG] Calling '{orig.__name__}'")
        print(f"[DEBUG] args: {args}")
        result = orig(*args)
        print(f"[DEBUG] '{orig.__name__}' returned: {result}")
        return result
    return wrapper
    
@count_calls
def greet(name):
    return f"Hello, {name}!"
print(greet("nono"))

greet("Ali")
greet("Boba")
greet("youm")
print(f"Total calls: {greet.cont}")

@timer
@logger
@debug
def slow_function(n):
    time.sleep(n)
    print(f"Slept for {n} seconds")
result = slow_function(2)
result
# Output: [TIMER] Function 'slow_function' executed in 2.0023 seconds