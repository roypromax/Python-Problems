# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

numbers = [5,4,3,2,1,6,7,8,9,10]
numbers.append(20)
numbers.remove(3)
numbers.sort()
print(numbers)