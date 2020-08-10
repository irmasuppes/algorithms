import numpy as np

# Returns index of the num element if present else -1
# low - lowest search index in current recursion step
# high - highest search index in current recursion step
def binary_search(array, low, high, num):
    #Check if the num element is in array
    if high >= low:
        # Find middle element index
        mid = (high + low) // 2
        # Check if the middle element is num
        if array[mid] == num:
            return mid
        # Check if the num element is bigger than the middle element
        elif array[mid] > num:
            return binary_search(array, low, mid-1, num)
        # If not, num element is smalle than the middle element
        else:
            return binary_search(array, mid + 1, high, num)
    # Num element is not in the array
    else:
        return -1

# Test array
arr = np.random.randint(0,100,20)
arr.sort()
# Test num
num = arr[7]
result = binary_search(arr, 0, len(arr) - 1, num)

if result == -1:
    print("Number is not presented in the array.")
else:
    print(f"Number is at index {result} in the array.")