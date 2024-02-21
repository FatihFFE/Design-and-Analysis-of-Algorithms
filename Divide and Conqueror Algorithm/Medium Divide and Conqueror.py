# merge_sort function that takes an unsorted list(arr) as an input
def merge_sort(arr):
    # Base case: If the length of the array is 0 or 1, then arr already sorted -> return the array.
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves (divide and conqueror)
    mid = len(arr) // 2  # Find the middle index of the array by divide the length
    left_half = arr[:mid]  # Split the array into the left half by start to mid
    right_half = arr[mid:]  # Split the array into the right half by mid to end

    # Recursively sort the two halves
    left_half = merge_sort(left_half)  # Recursively sort the left half
    right_half = merge_sort(right_half)  # Recursively sort the right half

    # Merge the sorted halves using the merge function
    sorted_arr = merge(left_half, right_half)
    return sorted_arr

# Merge function that combines two sorted lists(left,right) into one
def merge(left, right):
    merged = []  # An empty list to store the merged result
    left_idx, right_idx = 0, 0  # Initialize indexes for the left and right lists

    # Compare elements from the left and right lists and add the smaller element to the merged list
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])  # Add the element from the left list to merged
            left_idx += 1
        else:
            merged.append(right[right_idx])  # Add the element from the right list to merged
            right_idx += 1

    # After the while loop, one of the lists can be still have remaining elements
    # Extend the merged list with the remaining elements from both left and right lists
    merged.extend(left[left_idx:])  # Add remaining elements from the left list
    merged.extend(right[right_idx:])  # Add remaining elements from the right list

    return merged  # Return the merged and sorted list

# Test the merge_sort function
input_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(input_list)
print(sorted_list)  # Print the sorted result

