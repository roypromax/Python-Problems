# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

input_number = int(input("Enter number : "))

def factorial(num):
  value = 1
  for i in range(1,num+1):
    value = value * i
  return value

print(f"Factorial of {input_number} is {factorial(input_number)}.")
    