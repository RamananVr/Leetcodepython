"""
LeetCode Problem #1228: Missing Number In Arithmetic Progression

Problem Statement:
In some array `arr`, the values were in arithmetic progression: the values `arr[i+1] - arr[i]` are all equal for every `i`. A value from `arr` was removed that was not the first or last value in the array.

Given `arr`, return the removed value.

Example 1:
Input: arr = [5, 7, 11, 13]
Output: 9
Explanation: The original array was [5, 7, 9, 11, 13].

Example 2:
Input: arr = [15, 13, 12]
Output: 14
Explanation: The original array was [15, 14, 13, 12].

Constraints:
- 3 <= arr.length <= 1000
- 0 <= arr[i] <= 10^5
"""

def missingNumber(arr):
    """
    Finds the missing number in an arithmetic progression.

    :param arr: List[int] - The input array with one missing number.
    :return: int - The missing number in the arithmetic progression.
    """
    # Calculate the common difference (d) of the arithmetic progression
    n = len(arr)
    d = (arr[-1] - arr[0]) // n

    # Iterate through the array to find the missing number
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != d:
            return arr[i - 1] + d

    # If no missing number is found (shouldn't happen per constraints)
    return -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [5, 7, 11, 13]
    print(missingNumber(arr1))  # Output: 9

    # Test Case 2
    arr2 = [15, 13, 12]
    print(missingNumber(arr2))  # Output: 14

    # Test Case 3
    arr3 = [1, 3, 7, 9]
    print(missingNumber(arr3))  # Output: 5

    # Test Case 4
    arr4 = [10, 20, 40]
    print(missingNumber(arr4))  # Output: 30

    # Test Case 5
    arr5 = [2, 4, 8, 10]
    print(missingNumber(arr5))  # Output: 6


"""
Time Complexity Analysis:
- Calculating the common difference `d` takes O(1).
- Iterating through the array to find the missing number takes O(n), where n is the length of the array.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Overall space complexity: O(1).

Topic: Arrays
"""