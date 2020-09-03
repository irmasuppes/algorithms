import numpy as np

# Bubble sorting algorithm implementation. Returns sorted array.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test array
arr = np.random.randint(0,100,20)
result = bubble_sort(arr)
# Sorted array for validation
arr.sort()
print(f"Bubble sort result: {result}")
print(f"Sorted array: {arr}")