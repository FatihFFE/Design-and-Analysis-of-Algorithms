# Function to find the maximum subarray sum using a divide and conquer approach
def maxSubarraySum(arr):
    # Base case. If the array is empty, then the maximum subarray sum is 0.
    if len(arr) == 0:
        return 0
    
    # Base case. If the array has only one element, then the maximum subarray sum is that element.
    if len(arr) == 1:
        return arr[0]
    
    # Calculate the midpoint of the array
    mid = len(arr) // 2

    # Divide the array into left and right subarrays
    l_subArr = arr[:mid]
    r_subArr = arr[mid:]

    # Recursively call the maximumSubarraySum for the left and right subarrays
    max_leftSum = maxSubarraySum(l_subArr)
    max_rightSum = maxSubarraySum(r_subArr)

    # Calculate the maximum subarray sum that crosses the midpoint
    max_crossing_sum = maxCrossingSum(arr, mid)

    # Return the maximum of the three sums: left subarray, right subarray, and crossing sum
    return max(max_leftSum, max_rightSum, max_crossing_sum)

# Function to find the maximum subarray sum that crosses the midpoint
def maxCrossingSum(arr, mid):
    left_sum = float('-inf') # Handle case. Initialize left_sum to -infinity in any case that a negative number can be greatest subarray 
    sum = 0
    # Find the maximum sum for the left part of the array
    for i in range(mid, -1, -1): # Start from mid stop in -1 for array index step -1 to scan every index
        sum += arr[i]
        left_sum = max(left_sum, sum) # Check if the left sum or new sum is greater then assign it to left_sum

    right_sum = float('-inf')  # Handle case. Initialize Right_sum to -infinity in any case that a negative number can be greatest subarray 
    sum = 0
    # Find the maximum sum for the right part of the array
    for i in range(mid + 1, len(arr)): # Start from mid + 1 stop in len(arr) to scan array index
        sum += arr[i]
        right_sum = max(right_sum, sum)  # Check if the left sum or new sum is greater then assign it to right_sum

    # Return the sum of the maximum sums of the left and right parts
    return left_sum + right_sum

arr = [-1, 2, -2, 5, -2, 3, 2, -4, 4] #[5, -2, 3, 2] when we sum them up answer should be 8
result = maxSubarraySum(arr)
print("Maximum Subarray Sum:", result)