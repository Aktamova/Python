Puzzle 1: Write to a File 
Create a file example.txt and write "Hello, World!" using w mode
with open ('example.txt', 'w') as test:
    test.write("Hello, World")
Puzzle 2: Append to a File 
Append "This is an appended line." to example.txt.
with open ('example.txt', 'a') as test:
    test.write("\nThis is an appended line")
Puzzle 3: Read a File 
Read and print the content of example.txt.
with open ('example.txt', 'r') as test:
    data = test.read()
    print(data)    
Puzzle 4: Write and Read a File
Write "Python is fun!" to test.txt and read it
with open('test.txt', 'w+') as test:
    test.write('Python is fun')
    test.seek(0)
    data = test.read()
    print(data)
Puzzle 5: Append and Read 
Append "New data" to log.txt, then read the entire file.
with open ('test.txt', 'a+') as test:
    test.write("\nNew data")
    test.seek(0)
    data = test.read()
    print(data)
Puzzle 6: Write a List of Numbers to a File
Write numbers 1 to 5, each on a new line in numbers.txt.
with open ('numbers.txt', 'w') as test:
    for i in range(1, 6):
        test.write(f'{i}\n')
Puzzle 7: Read a File Line by Line
Read numbers.txt line by line and print each line.
with open ('numbers.txt', 'r') as test:
    data = test.read()
    print(data)
Puzzle 8: Count the Number of Words in a File
Count the number of words in story.txt.
count = 0
with open('test.txt', 'r') as test:
    data = test.read()
    lines = data.split()
    count += len(lines)
print(count)
Puzzle 9: Find and Replace in a File
Replace "old" with "new" in data.txt.
with open('test.txt', 'r+') as file:
    data = file.read().replace('New', 'Old')
with open('test.txt', 'w') as file:
    file.write(data)
Puzzle 10: Remove Blank Lines from a File
Remove all empty lines from text.txt.
with open('test.txt', 'r') as file:
    data = [line for line in file if line.strip()]
with open('test.txt', 'w') as file:
    file.writelines(data)
Puzzle 11: Handle Division by Zero
Handle ZeroDivisionError when dividing numbers.
def division(a, b):
    try:
        return a / b  
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

division(1, 0)

Puzzle 12: Handle Multiple Exceptions
Catch ValueError and ZeroDivisionError.
def test(a, b):

    try:
        return a / b  
    except ZeroDivisionError :
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."

test(1, 0)
Puzzle 13: Use finally Block
Ensure "Execution completed" always prints.
try:
    3/0
except ZeroDivisionError as z:
    print('You got zero division error')
finally:
    print('Execution completed')  
Puzzle 14: Raise a Custom Exception
Raise an error if a number is negative.
def check_positive(number):

    if number < 0:
        raise ValueError("Error: Negative numbers are not allowed.")
    return "The number is positive."

print(check_positive(-10))   

Puzzle 15: Handle File Not Found Exception
Handle a missing file error when reading a file.
try:
    with open('newtext.txt', "r") as file:  
        file.read()  
except FileNotFoundError:
    print(f"Error: The file was not found.")

