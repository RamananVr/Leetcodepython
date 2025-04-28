"""
LeetCode Problem #1502: Can Make Arithmetic Progression From Sequence

Problem Statement:
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers `arr`, return `true` if the array can be rearranged to form an arithmetic progression. Otherwise, return `false`.

Example 1:
Input: arr = [3, 5, 1]
Output: true
Explanation: We can rearrange the array as [1, 3, 5], which forms an arithmetic progression.

Example 2:
Input: arr = [1, 2, 4]
Output: false
Explanation: There is no way to rearrange the array to form an arithmetic progression.

Constraints:
- 2 <= arr.length <= 1000
- -10^6 <= arr[i] <= 10^6
"""

def canMakeArithmeticProgression(arr):
    """
    Determines if the given array can be rearranged to form an arithmetic progression.

    :param arr: List[int] - The input array of integers.
    :return: bool - True if the array can be rearranged to form an arithmetic progression, False otherwise.
    """
    # Sort the array
    arr.sort()
    
    # Calculate the common difference
    diff = arr[1] - arr[0]
    
    # Check if all consecutive differences are the same
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 5, 1]
    print(canMakeArithmeticProgression(arr1))  # Output: True

    # Test Case 2
    arr2 = [1, 2, 4]
    print(canMakeArithmeticProgression(arr2))  # Output: False

    # Test Case 3
    arr3 = [7, 3, 1, 5]
    print(canMakeArithmeticProgression(arr3))  # Output: True

    # Test Case 4
    arr4 = [10, 20, 30, 40]
    print(canMakeArithmeticProgression(arr4))  # Output: True

    # Test Case 5
    arr5 = [1, 1, 1, 1]
    print(canMakeArithmeticProgression(arr5))  # Output: True

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Checking the differences takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation may require additional space depending on the sorting algorithm used.
- Overall space complexity: O(1) additional space if in-place sorting is used, otherwise O(n).

Topic: Arrays
"""