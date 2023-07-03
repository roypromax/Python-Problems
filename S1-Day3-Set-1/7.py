# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

input_number = int(input("Enter number : "))

def checkPrime(number):
  if number<=1:
    return False

  for i in range(2,number):
    if number%i==0:
      return False

  return True

if checkPrime(input_number) :
  print(input_number,"is a prime number")
else : 
  print(input_number,"is not a prime number")