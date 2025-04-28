"""
LeetCode Problem #1492: The kth Factor of n

Problem Statement:
Given two positive integers `n` and `k`, return the `kth` factor of `n`. 
A factor of `n` is a positive integer `i` such that `n % i == 0`.

If there are fewer than `k` factors, return `-1`.

Example 1:
Input: n = 12, k = 3
Output: 3
Explanation: Factors of 12 are 1, 2, 3, 4, 6, 12. The 3rd factor is 3.

Example 2:
Input: n = 7, k = 2
Output: 7
Explanation: Factors of 7 are 1, 7. The 2nd factor is 7.

Example 3:
Input: n = 4, k = 4
Output: -1
Explanation: Factors of 4 are 1, 2, 4. There is no 4th factor.

Constraints:
- 1 <= k <= 1000
- 1 <= n <= 1000
"""

def kthFactor(n: int, k: int) -> int:
    """
    Finds the kth factor of n. If there are fewer than k factors, returns -1.
    
    :param n: The integer whose factors are to be considered.
    :param k: The position of the factor to return.
    :return: The kth factor of n, or -1 if there are fewer than k factors.
    """
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if count == k:
                return i
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 12, 3
    print(kthFactor(n1, k1))  # Output: 3

    # Test Case 2
    n2, k2 = 7, 2
    print(kthFactor(n2, k2))  # Output: 7

    # Test Case 3
    n3, k3 = 4, 4
    print(kthFactor(n3, k3))  # Output: -1

    # Test Case 4
    n4, k4 = 1, 1
    print(kthFactor(n4, k4))  # Output: 1

    # Test Case 5
    n5, k5 = 1000, 10
    print(kthFactor(n5, k5))  # Output: 20

"""
Time Complexity:
- The loop runs from 1 to n, so the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) since no additional data structures are used.

Topic: Math
"""