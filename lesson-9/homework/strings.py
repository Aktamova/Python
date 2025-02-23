Puzzle 1: Create a Simple Class

Define a class Car with attributes brand and year. Create an object and print its attributes.
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def info(self):
        print(f'Brand nomi: {self.brand} \nYili: {self.year}')

car1 = Car('BMW', 2000)
car1.info()
Puzzle 2: Default Constructor

Create a class Person with a default constructor that sets name = "John" and age = 30.
class Person:
    def __init__(self):
        self.name = "John"
        self.age = 30

    def display(self):
        print(f'Name = {self.name} \nAge = {self.age}')

person = Person()
person.display()
Puzzle 3: Class Method

Create a class Circle with an attribute radius and a method area() that returns the area of the circle.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    
circle1 = Circle(5)
circle1.area()
Puzzle 4: Class with Multiple Methods

Define a class Rectangle with methods area() and perimeter().
class Rectangle:
    def __init__(self, a, b):
        self.a =a
        self.b =b
    def area(self):
        print(f'The area of rectangle is {self.a*self.b}')
    def perimetr(self):
        print(f'The perimetr of rectangle is {(self.a + self.b)*2}')

first = Rectangle(5, 6)
first.area()
first.perimetr()
Puzzle 5: Encapsulation

Create a class BankAccount with a private attribute _balance. Provide methods to deposit and withdraw money.
class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                return f"Withdrew: ${amount:.2f}. Remaining balance: ${self._balance:.2f}"
            return "Error: Insufficient funds."
        return "Withdrawal amount must be positive."

    def get_balance(self):
        return self._balance

account = BankAccount(100)  
account.deposit(100)
account.get_balance()
account.withdraw(150)
Puzzle 6: Addition

Create a class method that will add x to y. Show the output
class Addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Add(self):    
        print(f'The sum of x and y:  {self.x + self.y}')
first = Addition(5, 6)
first.Add()
    
Puzzle 7. Multiple Inheritance

Create classes A and B. Create a class C that inherits from both.
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class B:
    def __init__(self, country, university):
        self.country = country
        self.university = university

class C(A, B):
    def __init__(self, name, age, country, university):
        A.__init__(self, name, age) 
        B.__init__(self, country, university)

item = C('Umida', 22, 'Uzb', 'TSUE')
print(item.name, item.university)    
Puzzle 8: Private Methods

Create a class Secret with a private method _hidden_message() that prints "This is private".
class Secret:
    def __init__(self):
        pass
        
    def __hidden_message(self):
        print("This is private")

    def reveal(self):
        self.__hidden_message()

secret_obj = Secret()
secret_obj.reveal() 
Puzzle 9: Class with a Counter

Create a class Student that keeps track of the total number of students created.
class Student:
    total_students = 0 

    def __init__(self, name):
        self.name = name
        Student.total_students += 1  

    def get_total_students():
        return Student.total_students  

s1 = Student("Alice")
s2 = Student("Bob")
# s3 = Student("Charlie")

print(f"Total students: {Student.get_total_students()}")  
Puzzle 10: Class with a Generator Method

Create a class EvenNumbers that generates even numbers up to a given limit using a method generate_even().
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def generate_even(self):
        lst =[]
        for num in range(1, self.limit + 1,):
            if num %2 == 0:
                lst.append(num) 
        print(lst)              

evens = EvenNumbers(10)
evens.generate_even()
