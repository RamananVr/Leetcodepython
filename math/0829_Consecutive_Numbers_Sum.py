"""
LeetCode Problem #829: Consecutive Numbers Sum

Problem Statement:
Given an integer `n`, return the number of ways you can write `n` as the sum of consecutive positive integers.

In other words, find the number of unique integer sequences such that:
    n = k + (k+1) + (k+2) + ... + (k+m-1)
Where `k` and `m` are positive integers, and `m` is the length of the sequence.

Constraints:
- 1 <= n <= 10^9

Example:
Input: n = 5
Output: 2
Explanation: 5 can be written as:
- 5 = 5 (a single number)
- 5 = 2 + 3 (a sum of two consecutive numbers)

Input: n = 9
Output: 3
Explanation: 9 can be written as:
- 9 = 9 (a single number)
- 9 = 4 + 5
- 9 = 2 + 3 + 4

Input: n = 15
Output: 4
Explanation: 15 can be written as:
- 15 = 15 (a single number)
- 15 = 7 + 8
- 15 = 4 + 5 + 6
- 15 = 1 + 2 + 3 + 4 + 5
"""

def consecutiveNumbersSum(n: int) -> int:
    """
    Returns the number of ways to write n as the sum of consecutive positive integers.
    """
    count = 0
    m = 1  # Length of the sequence

    while m * (m + 1) // 2 <= n:
        # Check if n - m * (m + 1) // 2 is divisible by m
        if (n - m * (m + 1) // 2) % m == 0:
            count += 1
        m += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    print(f"Input: n = {n1}")
    print(f"Output: {consecutiveNumbersSum(n1)}")  # Expected Output: 2

    # Test Case 2
    n2 = 9
    print(f"Input: n = {n2}")
    print(f"Output: {consecutiveNumbersSum(n2)}")  # Expected Output: 3

    # Test Case 3
    n3 = 15
    print(f"Input: n = {n3}")
    print(f"Output: {consecutiveNumbersSum(n3)}")  # Expected Output: 4

    # Test Case 4
    n4 = 1
    print(f"Input: n = {n4}")
    print(f"Output: {consecutiveNumbersSum(n4)}")  # Expected Output: 1

    # Test Case 5
    n5 = 100
    print(f"Input: n = {n5}")
    print(f"Output: {consecutiveNumbersSum(n5)}")  # Expected Output: 3

"""
Time Complexity:
- The while loop iterates as long as m * (m + 1) // 2 <= n. 
  This means m grows approximately as O(sqrt(2n)), so the time complexity is O(sqrt(n)).

Space Complexity:
- The algorithm uses a constant amount of space, so the space complexity is O(1).

Topic: Math
"""