# Part 1: Local and Global Variables

import os

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Global counter after increment: {counter}")
#output: Global counter after increment: 1

def reset_counter() : 
    counter = 0
    print(f"Local counter in reset_counter: {counter} ")
#output: Global counter after increment: 2

for _ in range(3):
    increment_counter()
#output: Global counter after increment: 3

reset_counter()
print(f"Global counter after reset_counter: {counter}")
#output: Global counter after increment: 0

# Part 2: File and Directory Operations

print("Current Working Directory:", os.getcwd())

files_and_dirs = os.listdir()
print("Files and Directories:", files_and_dirs)

os.mkdir('test_dir')
os.chdir('test_dir')
print("New Working Directory:", os.getcwd())

with open('test_file.txt', 'w') as f:
    f.write('This is a test file.')

os.remove('test_file.txt')
os.chdir('..')
os.rmdir('test_dir')

# Part 3: Error Handling
def divide_numbers(a,b):
    try:
        results = a/b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"{a} divided by {b} is {results}.")
    finally:
        print("Division operation completed.")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    results = divide_numbers(num1, num2)
    if results is not None:
        print(f"Result:, {result}")
except ValueError:
    print("Error: Invalid input. Please enter values.")
