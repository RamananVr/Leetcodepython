"""
LeetCode Problem #1299: Replace Elements with Greatest Element on Right Side

Problem Statement:
Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.

You need to do this in-place and in O(n) time complexity.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Example 2:
Input: arr = [400]
Output: [-1]

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i] <= 10^5
"""

def replaceElements(arr):
    """
    Replace each element in the array with the greatest element to its right.
    The last element is replaced with -1.

    :param arr: List[int] - Input array
    :return: List[int] - Modified array
    """
    n = len(arr)
    if n == 1:
        return [-1]
    
    # Initialize the greatest element to the right as -1
    greatest = -1
    
    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Store the current element before overwriting
        current = arr[i]
        # Replace the current element with the greatest element to its right
        arr[i] = greatest
        # Update the greatest element
        greatest = max(greatest, current)
    
    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [17, 18, 5, 4, 6, 1]
    print("Input:", arr1)
    print("Output:", replaceElements(arr1))  # Expected: [18, 6, 6, 6, 1, -1]

    # Test Case 2
    arr2 = [400]
    print("Input:", arr2)
    print("Output:", replaceElements(arr2))  # Expected: [-1]

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    print("Input:", arr3)
    print("Output:", replaceElements(arr3))  # Expected: [5, 5, 5, 5, -1]

    # Test Case 4
    arr4 = [10, 9, 8, 7]
    print("Input:", arr4)
    print("Output:", replaceElements(arr4))  # Expected: [9, 8, 7, -1]

# Time Complexity Analysis:
# The algorithm traverses the array once from right to left, performing O(1) operations for each element.
# Therefore, the time complexity is O(n), where n is the length of the array.

# Space Complexity Analysis:
# The algorithm uses a constant amount of extra space (for the `greatest` variable).
# Therefore, the space complexity is O(1).

# Topic: Arrays