# Linear search algorithm
def linear_search(data, target):
  for i in range(len(data)):
    if data[i] == target:
      return i  # Found it!
  return -1  # Not found

# Sorting algorithm
def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

     
# Binary search algorithm
def binary_search(data, target):
    data = sorted(data)      # Binary search requires a sorted list
    low = 0
    high = len(data) - 1
    while low <= high:
      mid = (low + high) // 2
      if target == data[mid]:
        return mid  # Found it!
      elif target < data[mid]:
        high = mid - 1
      else:
        low = mid + 1
    return -1  # Not found

# Bubble sort algorithm
def bubble_sort(data):
    n = len(data)
    for i in range(1, n):
        for j in range(0, n - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

