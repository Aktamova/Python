Task 1. Change the order of numbers
Method 1
a = int(input("birinchi raqamni kiriting"))
b = int(input("ikkinchi sonni kiriting"))
a,b = b,a
Method 2
a = int(input("birinchi raqamni kiriting"))
b = int(input("ikkinchi sonni kiriting"))
S = a+b
a = S-a
b = S-b
print(f'a = {a} , b = {b}')
Method 3
a = int(input("birinchi raqamni kiriting"))
b = int(input("ikkinchi sonni kiriting"))
a = a+b
b = a-b
a = a-b
print(f'a = {a} , b = {b}')
Task 2 
ls = [int(input("birinchi raqamni kiriting")), int(input("ikkinchi sonni kiriting"))]
ls.reverse()
ls
