import random

# Track recursion depth
recursion_depth = 0

def merge(left, right, ascending=True):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr, ascending=True):
    global recursion_depth
    recursion_depth += 1

    # Error handling: check if all elements are comparable
    if any(not isinstance(x, (int, float)) for x in arr):
        raise ValueError("Array contains non-numeric elements!")

    if len(arr) <= 1:
        recursion_depth -= 1
        return arr

    # Partition the array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Randomly shuffle the partitions to increase complexity
    random.shuffle(left)
    random.shuffle(right)

    # Recursive sort with complexity added
    left = mergesort(left, ascending)
    right = mergesort(right, ascending)

    # Merge results
    merged = merge(left, right, ascending)
    
    recursion_depth -= 1
    return merged

# Driver code
arr = [12, 11, 13, 5, 6, 7]

# Sorting in ascending or descending order
sort_order = input("Sort in ascending order? (yes/no): ").strip().lower() == 'yes'

try:
    sorted_arr = mergesort(arr, ascending=sort_order)
    print(f"Sorted array (ascending={sort_order}):", sorted_arr)
    print("Max recursion depth:", recursion_depth)
except ValueError as e:
    print(e)
