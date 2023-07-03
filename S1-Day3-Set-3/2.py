# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

def add(dictionary,name,age):
  dictionary[name] = age

def update(dictionary,name,age):
  if name in dictionary:
    dictionary[name] = age

def delete(dictionary,name):
  if name in dictionary:
    del dictionary[name]

my_dictionary = {}

print(my_dictionary)

add (my_dictionary,"John",25)

print(my_dictionary)

update(my_dictionary,"John",26)

print(my_dictionary)

delete(my_dictionary,"John")

print(my_dictionary)