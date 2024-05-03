# Linear search algorithm
def linear_search(data, target):
    steps = []  # Store steps for printing
    steps.append(f"Entered data: {data}")
    for i in range(len(data)):
        steps.append(f"Step {i}: Comparing {data[i]} with {target}")
        if data[i] == target:
            output = f"Target found at index {i}" + "\n" + "\n".join(steps)	
            return output  # Found it!
    steps.append("Target not found")
    return -1, steps  # Not found

# Sorting algorithm
def selection_sort(data):
    steps = []  # Store steps for printing
    n = len(data)
    steps.append(f"Unsorted data: {data}")
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            steps.append(f"Step {len(steps)}: Comparing {data[j]} with {data[min_index]}")
            if data[j] < data[min_index]:
                min_index = j
        steps.append(f"Step {len(steps)+1}: Swapping {data[i]} with {data[min_index]}")
        data[i], data[min_index] = data[min_index], data[i]
    steps.append("Sorting completed")
    result = "\n".join(steps) + f"\nSorted data: {data}"
    return result

# Binary search algorithm
def binary_search(data, target):
    data = sorted(data)  # Binary search requires a sorted list
    low = 0
    high = len(data) - 1
    steps = []  # Store steps for printing
    steps.append(f'Entered data: {data}')
    while low <= high:
        mid = (low + high) // 2
        steps.append(f"Step {len(steps)}: Checking {data[mid]}")
        if target == data[mid]:
            result = "\n".join(steps) + f"\nTarget found at index {mid}"  # Found it!
            return result
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    result = "\n".join(steps) + "\nTarget not found"  # Target not found
    return result

# Bubble sort algorithm
def bubble_sort(data):
    steps = []  # Store steps for printing
    steps.append(f"Unsorted data: {data}")
    n = len(data)
    for i in range(1, n):
        for j in range(0, n - i):
            steps.append(f"Step {len(steps)}: Comparing {data[j]} with {data[j+1]}")
            if data[j] > data[j + 1]:
                steps.append(f"Step {len(steps)}: Swapping {data[j]} with {data[j+1]}")
                data[j], data[j + 1] = data[j + 1], data[j]
    steps.append("Sorting completed")
    
    result = "\n".join(steps) + f"\nSorted data: {data}" 
    return result