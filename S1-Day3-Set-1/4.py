# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

numbers = [10,20,25,45]

sum = sum(numbers)
average = sum / len(numbers)

print("Sum: ",sum," Average: ",average)