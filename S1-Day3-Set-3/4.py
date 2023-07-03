# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


def palindromeCheck(str):
  rev_str = ""
  for i in range(len(str) - 1, -1, -1):
    rev_str += str[i]
  if rev_str == str:
    print(f"The word {str} is a palindrome.")
    return
  else:
    print(f"The word {str} is not a palindrome.")
    return


string = "madam"
palindromeCheck(string)
