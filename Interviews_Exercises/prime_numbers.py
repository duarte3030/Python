# 1. Write a Python Program to print Prime Numbers between 2 numbers (for loop)
for num in range(5, 20):
    if all(num % i != 0 for i in range(2, num)):
        print(num)