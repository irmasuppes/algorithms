import numpy as np

# Returns index of num element in the array if present, else -1
def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Test array
arr = np.random.randint(0,100,20)
# Test num
num = arr[13]
arr.sort()
print(arr, num)

result = linear_search(arr, num)
if result == -1:
    print("The element is not in the array")
else:
    print(f"The element is at index {result} in the array.")
