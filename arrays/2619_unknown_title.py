"""
LeetCode Problem #2619: Array Prototype Last

Problem Statement:
Write a function that accepts an array and returns its last element. 
If the array is empty, it should return -1.

Example 1:
Input: arr = [1, 2, 3]
Output: 3

Example 2:
Input: arr = []
Output: -1

Constraints:
- The input array can contain integers, strings, or other data types.
- The function should handle empty arrays gracefully.
"""

# Solution
def last_element(arr):
    """
    Returns the last element of the array. If the array is empty, returns -1.

    :param arr: List of elements
    :return: Last element of the array or -1 if the array is empty
    """
    return arr[-1] if arr else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Non-empty array
    arr1 = [1, 2, 3]
    print(last_element(arr1))  # Output: 3

    # Test Case 2: Empty array
    arr2 = []
    print(last_element(arr2))  # Output: -1

    # Test Case 3: Array with one element
    arr3 = [42]
    print(last_element(arr3))  # Output: 42

    # Test Case 4: Array with mixed data types
    arr4 = [1, "hello", 3.14, True]
    print(last_element(arr4))  # Output: True

    # Test Case 5: Array with nested lists
    arr5 = [[1, 2], [3, 4], [5, 6]]
    print(last_element(arr5))  # Output: [5, 6]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Accessing the last element of a list using arr[-1] is an O(1) operation.
- Checking if the array is empty (using `if arr`) is also O(1).
- Therefore, the overall time complexity is O(1).

Space Complexity:
- The function does not use any additional space apart from a constant amount of memory for the return value.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays