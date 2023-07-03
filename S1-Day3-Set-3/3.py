# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def twoSum(array, target):
  for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
      if array[i] + array[j] == target:
        return [i, j]


array = [2, 7, 11, 15]
target = 9

print(twoSum(array, target))
