import numpy as np

# Returns the index of the num element in the array if present,else -1
def binary_search(array, num):
    low = 0
    high = len(array) - 1

    while low <= high:
        # Find the middle element
        mid = (low + high) // 2

        # Check if the middle element is smaller than num
        if array[mid] < num:
            low = mid + 1
        # Check if the middle element is bigger than num
        elif array[mid] > num:
            high = mid - 1
        # Found the num element
        else:
            return mid

    # Reached this line when the num element is not in array
    return -1
            
    

# Test array
arr = np.random.randint(0, 100, 20)
# Test num
num = arr[13]
arr.sort()
print(arr, num)
result = binary_search(arr, num)

if result == -1:
    print("The element is not in the array.")
else:
    print(f"The element is at the index {result} in the array.")