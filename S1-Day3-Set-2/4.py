# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:
# yaivePNT

str1 = "PyNaTive"

def lowerUpper(string):
  output = ""
  for item in string:
    if item.lower()==item:
      output += item

  for item in string:
    if item.upper()==item:
      output += item

  return output

print(lowerUpper(str1))