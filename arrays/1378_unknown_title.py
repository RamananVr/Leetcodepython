"""
LeetCode Problem #1378: Replace Elements with Greatest Element on Right Side

Problem Statement:
Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.

After doing so, return the array.

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

# Solution
def replaceElements(arr):
    """
    Replace each element in the array with the greatest element to its right.
    The last element is replaced with -1.

    :param arr: List[int] - Input array
    :return: List[int] - Modified array
    """
    n = len(arr)
    max_right = -1  # Initialize the maximum element on the right as -1
    for i in range(n - 1, -1, -1):  # Traverse the array from right to left
        new_max = max(max_right, arr[i])  # Update the maximum element
        arr[i] = max_right  # Replace the current element with the max on the right
        max_right = new_max  # Update max_right for the next iteration
    return arr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [17, 18, 5, 4, 6, 1]
    print(replaceElements(arr1))  # Expected Output: [18, 6, 6, 6, 1, -1]

    # Test Case 2
    arr2 = [400]
    print(replaceElements(arr2))  # Expected Output: [-1]

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    print(replaceElements(arr3))  # Expected Output: [5, 5, 5, 5, -1]

    # Test Case 4
    arr4 = [10, 9, 8, 7, 6]
    print(replaceElements(arr4))  # Expected Output: [9, 8, 7, 6, -1]

    # Test Case 5
    arr5 = [100, 200, 300, 400, 500]
    print(replaceElements(arr5))  # Expected Output: [500, 500, 500, 500, -1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array once from right to left, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm modifies the input array in place and does not use any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""