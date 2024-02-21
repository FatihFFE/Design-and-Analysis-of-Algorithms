import random

def find_median(arr):
    n = len(arr)
    if n%2 == 1:
        return quickselect(arr,0,n-1,n//2)
    else:
        mid1 = quickselect(arr,0,n-1,n//2)
        mid2 = quickselect (arr,0,n-1,n//2-1)
        return (mid1 + mid2)/2
    

def quickselect(arr,left,right,k):
    if left == right:
        return arr[left]
    
    pivot_index = random.randint(left,right)
    pivot_index = partition(arr,left,right,pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr,left,pivot_index - 1,k)
    else:
        return quickselect(arr,pivot_index+1,right,k)
    

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def test_find_median():
    # Test cases with expected outputs
    test_cases = [
        ([5, 2, 5, 2, 6, 10, 3, 7, 6, 4], 5),
        ([3, 4, 5, 6, 7], 5),
        ([4, 3, 2, 1, 0], 2),
        ([9, 3, 4, 8, 4, 2, 7], 4),
        ([10, 20, 30, 40], 25.0),
    ]

    for arr, expected_result in test_cases:
        result = find_median(arr)
        if result == expected_result:
            print(f"PASS: Median of {arr} is {result}")
        else:
            print(f"FAIL: Median of {arr} is {result}, expected {expected_result}")

# Run the tests
test_find_median()