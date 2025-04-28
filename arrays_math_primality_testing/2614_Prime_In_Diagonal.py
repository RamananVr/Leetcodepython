"""
LeetCode Problem #2614: Prime In Diagonal

Problem Statement:
You are given a 2D integer array `nums` of size `n x n`. Return the largest prime number that lies on at least one of the diagonals of `nums`. In case, no prime number is present on any of the diagonals, return 0.

Note:
- An integer is prime if it is greater than 1 and has no divisors other than 1 and itself.
- The primary diagonal of `nums` is the set of indices `(i, i)` where `0 <= i < n`.
- The secondary diagonal of `nums` is the set of indices `(i, n - i - 1)` where `0 <= i < n`.

Constraints:
- `1 <= nums.length == nums[i].length <= 100`
- `1 <= nums[i][j] <= 4 * 10^6`
"""

# Solution
from math import isqrt

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def diagonalPrime(nums):
    """
    Function to find the largest prime number on the diagonals of a 2D array.
    """
    n = len(nums)
    max_prime = 0

    for i in range(n):
        # Check primary diagonal element
        if is_prime(nums[i][i]):
            max_prime = max(max_prime, nums[i][i])
        # Check secondary diagonal element
        if is_prime(nums[i][n - i - 1]):
            max_prime = max(max_prime, nums[i][n - i - 1])

    return max_prime

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [
        [1, 2, 3],
        [5, 6, 7],
        [9, 10, 11]
    ]
    print(diagonalPrime(nums1))  # Output: 11

    # Test Case 2
    nums2 = [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]
    print(diagonalPrime(nums2))  # Output: 2

    # Test Case 3
    nums3 = [
        [15, 28, 33],
        [49, 51, 57],
        [91, 93, 95]
    ]
    print(diagonalPrime(nums3))  # Output: 0

    # Test Case 4
    nums4 = [
        [17, 22, 19],
        [23, 29, 31],
        [37, 41, 43]
    ]
    print(diagonalPrime(nums4))  # Output: 43

"""
Time Complexity:
- Checking if a number is prime takes O(sqrt(k)), where k is the number being checked.
- For each diagonal element, we perform a primality check. Since there are at most 2n diagonal elements in an n x n matrix, the total time complexity is O(n * sqrt(k)), where k is the maximum value in the matrix.

Space Complexity:
- The space complexity is O(1) as we are using a constant amount of extra space.

Topic: Arrays, Math, Primality Testing
"""