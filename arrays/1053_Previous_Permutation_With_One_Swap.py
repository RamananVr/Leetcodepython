"""
LeetCode Problem #1053: Previous Permutation With One Swap

Problem Statement:
Given an array of positive integers `arr` (not necessarily distinct), return the lexicographically largest permutation that is smaller than `arr`, that can be made with exactly one swap (a swap exchanges the positions of two numbers `arr[i]` and `arr[j]`). If it cannot be done, return the same array.

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i] <= 10^4
"""

def prevPermOpt1(arr):
    """
    Returns the lexicographically largest permutation smaller than the input array
    by performing at most one swap.

    :param arr: List[int] - The input array
    :return: List[int] - The resulting array after the swap
    """
    n = len(arr)
    
    # Step 1: Find the first index `i` from the right where arr[i] > arr[i+1]
    i = n - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    
    # If no such index exists, the array is already the smallest permutation
    if i < 0:
        return arr
    
    # Step 2: Find the largest index `j` to the right of `i` such that arr[j] < arr[i]
    j = n - 1
    while arr[j] >= arr[i]:
        j -= 1
    
    # Step 3: Ensure we pick the leftmost occurrence of arr[j] if there are duplicates
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
    
    # Step 4: Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]
    
    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 2, 1]
    print(prevPermOpt1(arr1))  # Output: [3, 1, 2]

    # Test Case 2
    arr2 = [1, 1, 5]
    print(prevPermOpt1(arr2))  # Output: [1, 1, 5]

    # Test Case 3
    arr3 = [1, 9, 4, 6, 7]
    print(prevPermOpt1(arr3))  # Output: [1, 7, 4, 6, 9]

    # Test Case 4
    arr4 = [3, 1, 1, 3]
    print(prevPermOpt1(arr4))  # Output: [1, 3, 1, 3]

    # Test Case 5
    arr5 = [5, 3, 1]
    print(prevPermOpt1(arr5))  # Output: [5, 1, 3]

"""
Time Complexity Analysis:
- Step 1: Finding the first decreasing element from the right takes O(n).
- Step 2: Finding the largest index `j` such that arr[j] < arr[i] takes O(n).
- Step 3: Adjusting `j` to the leftmost occurrence of arr[j] takes O(n) in the worst case.
- Step 4: Swapping two elements is O(1).
Overall, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""