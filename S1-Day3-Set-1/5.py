# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

string = "Python"

def reverse_str(str):
  output = ""
  for i in range(len(str)-1,-1,-1):
    output += str[i]
  return output

print(reverse_str(string))
    