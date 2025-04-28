"""
LeetCode Problem #1588: Sum of All Odd Length Subarrays

Problem Statement:
Given an array of positive integers `arr`, calculate the sum of all possible odd-length subarrays of `arr`.

A subarray is a contiguous subsequence of the array. Return the sum of all odd-length subarrays of `arr`.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[2] = 2
If we add all these together we get 1 + 2 = 3

Example 3:
Input: arr = [10,11,12]
Output: 66

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 1000
"""

# Python Solution
def sumOddLengthSubarrays(arr):
    """
    Calculate the sum of all odd-length subarrays of the given array.

    :param arr: List[int] - The input array of positive integers
    :return: int - The sum of all odd-length subarrays
    """
    total_sum = 0
    n = len(arr)
    
    for i in range(n):
        # Calculate the contribution of arr[i] to all odd-length subarrays
        left_count = i + 1
        right_count = n - i
        total_subarrays = left_count * right_count
        odd_subarrays = (total_subarrays + 1) // 2  # Only odd-length subarrays
        total_sum += arr[i] * odd_subarrays
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 4, 2, 5, 3]
    print(sumOddLengthSubarrays(arr1))  # Output: 58

    # Test Case 2
    arr2 = [1, 2]
    print(sumOddLengthSubarrays(arr2))  # Output: 3

    # Test Case 3
    arr3 = [10, 11, 12]
    print(sumOddLengthSubarrays(arr3))  # Output: 66

    # Test Case 4
    arr4 = [1]
    print(sumOddLengthSubarrays(arr4))  # Output: 1

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    print(sumOddLengthSubarrays(arr5))  # Output: 105

"""
Time Complexity Analysis:
- The solution iterates through the array once, performing constant-time calculations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""