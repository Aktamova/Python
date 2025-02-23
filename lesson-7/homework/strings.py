No Parameters / No Return Value
1. Write a function `greet()` that prints 'Hello, World!' when called.
def greet():
    print('Hello, World')
greet()
2. Create a function `show_date_time()` that prints the current date and time.
from datetime import datetime
def show_date_time():
   x = datetime.now()
   print(x)
show_date_time()
3. Write a function `display_even_numbers()` that prints even numbers from 1 to 20.
def display_even_numbers():
    for x in range(1, 20):
        if x % 2 == 0:
            print(x)
display_even_numbers()
Parameters / No Return Value

4. Write a function `greet_user(name)` that takes a name as a parameter and prints 'Hello, [name]!'
def greet_user(name):
    print(f"Hello, {name}")
greet_user('Umida')
5. Create a function `print_square(n)` that prints the square of a given number.
def print_square(n):
    print(n**2)
print_square(5)
6. Write a function `multiply_numbers(a, b)` that takes two numbers and prints their product.
def multiply_numbers(a, b):
    print(a*b)
multiply_numbers(3, 8)
No Parameters / Return Value

7. Write a function `get_pi()` that returns the value of π (3.14159).
import math
def get_pi():
    print(math.pi)
get_pi()
8. Create a function `random_number()` that returns a random number between 1 and 100.
import random
def random_number():
    print(random.randint(1, 100))
random_number()
9. Write a function `current_year()` that returns the current year.
from datetime import datetime

def current_year():
    return datetime.now().year
current_year()    
Parameters / Return Value

10. Write a function `add_numbers(a, b)` that returns the sum of two numbers.
def add_numbers(a, b):
    print(a+b)
add_numbers(5, 6)
11. Create a function `is_even(n)` that returns `True` if the number is even and `False` otherwise.
def is_even(n):
    if n % 2 == 0:
        print (True)
    else: print (False)
is_even(15)
12. Write a function `get_factorial(n)` that returns the factorial of a given number
def get_factorial(n):
    a = 1
    r = 1
    while a<= n:
        r = r*a
        a+=1
    print(r)
get_factorial(4)
13. Write a recursive function `countdown(n)` that prints numbers from `n` to `1`.
def countdown(n):
    if n <= 0:  
        return
    print(n)  
    countdown(n - 1)  

countdown(5)
14. Create a recursive function `sum_natural(n)` that returns the sum of the first `n` natural numbers.
def sum_natural(n):
    if n <= 0:  
        return 0
    return n + sum_natural(n - 1)  

print(sum_natural(5))  
15. Write a recursive function `fibonacci(n)` that returns the `n`th Fibonacci number.
def fibonacci(n):
    if n <= 0:  
        return 0
    elif n == 1:  
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  

print(fibonacci(4))  
16. Write a function `sum_numbers(*args)` that takes multiple numbers and returns their sum.
def sum_numbers(*args):
    print(sum(args))  

sum_numbers(1, 2, 3, 4, 5)  
17. Create a function `print_info(**kwargs)` that prints key-value pairs passed as arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_info(name="Alice", age=25, city="New York")

18. Write a function `power(base, exponent=2)` that returns `base` raised to the power of `exponent`.
def power(base, exponent=2):
    return base ** exponent  

print(power(3, 3)) 
19. Create a function `calculate_area(length: float, width: float) -> float` that returns the area of a rectangle. Add a docstring explaining the function.
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    Returns the  area of the rectangle.
    """
    return length * width  

print(calculate_area(5, 3.0))  

20. Given a list of numbers, use `map()` to square each number and use `filter()` to return only the even squares. Write a function `process_numbers(nums: list) -> list`.
def process_numbers(nums: list) -> list:

    squared_nums = map(lambda x: x ** 2, nums)  
    even_squares = filter(lambda x: x % 2 == 0, squared_nums)  
    return list(even_squares)  

print(process_numbers([1, 2, 3, 4, 5]))  
