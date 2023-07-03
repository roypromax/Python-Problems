# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

string = "Hello"

def vowelsCount(string):
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count+=1
  return count

print("Number of vowels:",vowelsCount(string))
  