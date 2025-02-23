## Homeworks:
Write a program that will check evennes of given number
From given 3 numbers from input, find the biggest number
Write a program that will find if the number is vowel (aeiou) or consonant
Homework 1
a = int(input("Write a number: "))
if a % 2 == 0:
    print(f"{a} is even number")
else:
    print(f"{a} is odd number")

Homework 2
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if a > b and a > c:
    print(f"{a} is max")
elif b > a and b > c:
    print(f"{b} is max") 
else :
    print(f"{c} is max")
Homework 3
a = input("Write a letter ").lower()
if a in ('a', 'e', 'i', 'o', 'u'):
    print(f"{a} is vowel")
else :
    print(f"{a} is consonant")
