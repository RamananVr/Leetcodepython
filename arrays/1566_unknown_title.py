"""
LeetCode Problem #1566: Detect Pattern of Length M Repeated K or More Times

Problem Statement:
Given an array of positive integers `arr`, find a pattern of length `m` that is repeated `k` or more times.

A pattern is a subarray (contiguous sub-sequence) of the array. A pattern is considered repeated `k` or more times if there exists `k` or more non-overlapping occurrences of the pattern in the array such that the `k` occurrences do not share any elements.

Return `True` if there exists a pattern of length `m` that is repeated `k` or more times, otherwise return `False`.

Constraints:
- `2 <= m <= arr.length`
- `1 <= k <= arr.length`
- `1 <= arr[i] <= 1000`

Example 1:
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: True
Explanation: The pattern (4) of length 1 is repeated 4 times. It is repeated 3 or more times.

Example 2:
Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: True
Explanation: The pattern (1,2) of length 2 is repeated 2 times. It is repeated 2 or more times.

Example 3:
Input: arr = [1,2,3,1,2], m = 2, k = 2
Output: False
Explanation: The pattern (1,2) of length 2 is repeated only once. It is not repeated 2 or more times.

Example 4:
Input: arr = [2,2,2,2], m = 2, k = 3
Output: False
Explanation: The pattern (2,2) of length 2 is repeated only twice. It is not repeated 3 or more times.
"""

def containsPattern(arr, m, k):
    """
    Function to check if there exists a pattern of length m that is repeated k or more times.

    :param arr: List[int] - The input array of integers.
    :param m: int - The length of the pattern to check.
    :param k: int - The minimum number of times the pattern should repeat.
    :return: bool - True if such a pattern exists, False otherwise.
    """
    n = len(arr)
    for i in range(n - m * k + 1):
        # Check if the pattern starting at index i is repeated k times
        pattern = arr[i:i + m]
        count = 0
        for j in range(i, i + m * k, m):
            if arr[j:j + m] == pattern:
                count += 1
            else:
                break
        if count == k:
            return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 4, 4, 4, 4]
    m1, k1 = 1, 3
    print(containsPattern(arr1, m1, k1))  # Output: True

    # Test Case 2
    arr2 = [1, 2, 1, 2, 1, 1, 1, 3]
    m2, k2 = 2, 2
    print(containsPattern(arr2, m2, k2))  # Output: True

    # Test Case 3
    arr3 = [1, 2, 3, 1, 2]
    m3, k3 = 2, 2
    print(containsPattern(arr3, m3, k3))  # Output: False

    # Test Case 4
    arr4 = [2, 2, 2, 2]
    m4, k4 = 2, 3
    print(containsPattern(arr4, m4, k4))  # Output: False

    # Test Case 5
    arr5 = [1, 1, 1, 1, 1]
    m5, k5 = 1, 5
    print(containsPattern(arr5, m5, k5))  # Output: True

"""
Time Complexity:
- The outer loop runs for `O(n - m * k + 1)` iterations, where `n` is the length of the array.
- The inner loop checks up to `k` patterns of length `m`, which takes `O(k * m)` time.
- Overall, the time complexity is `O((n - m * k + 1) * k * m)`, which simplifies to `O(n * k * m)` in the worst case.

Space Complexity:
- The space complexity is `O(m)` for storing the `pattern` subarray.

Topic: Arrays
"""