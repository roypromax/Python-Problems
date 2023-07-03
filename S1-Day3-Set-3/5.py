# 5. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"


def selectionSort(array):
  for i in range(0, len(array) - 1):
    min_index = i
    for j in range(i+1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp
  return array


input_array = [64, 25, 12, 22, 11]
output_array = selectionSort(input_array)

print(output_array)
