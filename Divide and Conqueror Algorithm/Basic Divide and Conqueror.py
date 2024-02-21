def find_max(arr, low, high):
    if low == high:
        return arr[low]  # Base case: If there's only one element, return it.

    mid = (low + high) // 2

    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)

    return max(left_max, right_max)

def max_element(arr):
    if not arr:
        return None  # Handle the case of an empty array.

    return find_max(arr, 0, len(arr) - 1)

# Example:
arr = [7, 9, 4, 6, 3, 2, 5]
print("The maximum element is:", max_element(arr))
