"""
LeetCode Problem #1551: Minimum Operations to Make Array Equal

Problem Statement:
You have an array `arr` of length `n` where `arr[i] = 2 * i + 1` for all valid values of `i` (i.e., 0 <= i < n).

In one operation, you can select two indices `x` and `y` where 0 <= x, y < n and subtract 1 from `arr[x]` and add 1 to `arr[y]` (i.e., perform `arr[x] -= 1` and `arr[y] += 1`). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer `n`, the length of the array, return the minimum number of operations needed to make all the elements of the array equal.

Constraints:
- 1 <= n <= 10^4

Example:
Input: n = 3
Output: 2
Explanation: The array is [1, 3, 5]. We can make all the elements equal to 3 in 2 operations:
1. Decrease the last element by 1 and increase the first element by 1: [2, 3, 4].
2. Decrease the last element by 1 and increase the first element by 1: [3, 3, 3].
"""

# Python Solution
def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations to make all elements of the array equal.

    :param n: Length of the array
    :return: Minimum number of operations
    """
    # The array is [1, 3, 5, ..., 2*n-1]
    # The target value for all elements is the median, which is n for odd n and n for even n.
    # The number of operations is the sum of differences between the target and the first half of the array.
    return (n // 2) * (n // 2 + n % 2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {minOperations(n)}")  # Expected Output: 2

    # Test Case 2
    n = 6
    print(f"Input: n = {n}")
    print(f"Output: {minOperations(n)}")  # Expected Output: 9

    # Test Case 3
    n = 1
    print(f"Input: n = {n}")
    print(f"Output: {minOperations(n)}")  # Expected Output: 0

    # Test Case 4
    n = 10
    print(f"Input: n = {n}")
    print(f"Output: {minOperations(n)}")  # Expected Output: 25

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution runs in O(1) time because it directly computes the result using a mathematical formula.

Space Complexity:
- The solution uses O(1) space as it does not require any additional data structures or memory allocation.

Overall, the solution is highly efficient in both time and space.
"""

# Topic: Arrays, Math