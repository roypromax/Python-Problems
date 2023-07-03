# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

input_num = int(input("Enter number : "))

def fib(num):
  output = []
  if num>=1 :
    output.append(0)
  if num>=2 : 
    output.append(1)
  for i in range(3,num+1):
    fibNum = output[i-2] + output[i-3]
    output.append(fibNum)
  return output

print(fib(input_num))