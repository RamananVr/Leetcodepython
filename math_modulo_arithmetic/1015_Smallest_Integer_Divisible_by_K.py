"""
LeetCode Problem #1015: Smallest Integer Divisible by K

Problem Statement:
Given a positive integer K, you need to find the smallest positive integer N such that:
- N is divisible by K
- N only contains the digit 1

Return the length of N. If there is no such N, return -1.

Note:
- 1 <= K <= 10^5

Example:
- Input: K = 1
  Output: 1
  Explanation: The smallest N is 1, which has a length of 1.

- Input: K = 2
  Output: -1
  Explanation: There is no such N divisible by 2.

- Input: K = 3
  Output: 3
  Explanation: The smallest N is 111, which has a length of 3.

Constraints:
- The result is guaranteed to fit within a 32-bit signed integer if it exists.
"""

def smallestRepunitDivByK(K: int) -> int:
    """
    Finds the smallest positive integer N such that:
    - N is divisible by K
    - N only contains the digit 1

    Returns the length of N, or -1 if no such N exists.
    """
    if K % 2 == 0 or K % 5 == 0:
        return -1  # N cannot exist if K is divisible by 2 or 5

    remainder = 0
    for length in range(1, K + 1):  # At most, we will check K iterations
        remainder = (remainder * 10 + 1) % K
        if remainder == 0:
            return length

    return -1  # If no solution is found (should not happen for valid inputs)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    K = 1
    print(smallestRepunitDivByK(K))  # Output: 1

    # Test Case 2
    K = 2
    print(smallestRepunitDivByK(K))  # Output: -1

    # Test Case 3
    K = 3
    print(smallestRepunitDivByK(K))  # Output: 3

    # Test Case 4
    K = 7
    print(smallestRepunitDivByK(K))  # Output: 6

    # Test Case 5
    K = 13
    print(smallestRepunitDivByK(K))  # Output: 6

"""
Time Complexity:
- The algorithm runs in O(K) time in the worst case. This is because we iterate at most K times to find a solution.
- Each iteration involves a constant-time operation to compute the new remainder.

Space Complexity:
- The algorithm uses O(1) additional space. We only store the current remainder and the loop counter.

Topic: Math, Modulo Arithmetic
"""