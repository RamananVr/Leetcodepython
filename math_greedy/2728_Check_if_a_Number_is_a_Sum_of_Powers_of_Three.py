"""
LeetCode Problem #2728: Check if a Number is a Sum of Powers of Three

Problem Statement:
Given an integer `n`, return `true` if it is possible to represent `n` as the sum of distinct powers of three. Otherwise, return `false`.

An integer `x` is a power of three if there exists an integer `k` such that `x == 3^k`.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 3^1 + 3^2 = 3 + 9.

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 3^0 + 3^2 + 3^4 = 1 + 9 + 81.

Example 3:
Input: n = 21
Output: false
Explanation: It is not possible to represent 21 as the sum of distinct powers of three.

Constraints:
- 1 <= n <= 10^7
"""

def checkPowersOfThree(n: int) -> bool:
    """
    Determines if a number can be represented as the sum of distinct powers of three.

    Args:
    n (int): The input number.

    Returns:
    bool: True if the number can be represented as the sum of distinct powers of three, False otherwise.
    """
    while n > 0:
        if n % 3 == 2:  # If the remainder is 2, it's not possible to represent n as a sum of powers of 3
            return False
        n //= 3  # Reduce n by dividing it by 3
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 12
    print(f"Input: {n1}, Output: {checkPowersOfThree(n1)}")  # Expected: True

    # Test Case 2
    n2 = 91
    print(f"Input: {n2}, Output: {checkPowersOfThree(n2)}")  # Expected: True

    # Test Case 3
    n3 = 21
    print(f"Input: {n3}, Output: {checkPowersOfThree(n3)}")  # Expected: False

    # Additional Test Case 4
    n4 = 1
    print(f"Input: {n4}, Output: {checkPowersOfThree(n4)}")  # Expected: True

    # Additional Test Case 5
    n5 = 10**7
    print(f"Input: {n5}, Output: {checkPowersOfThree(n5)}")  # Expected: False

"""
Time Complexity Analysis:
- The algorithm repeatedly divides `n` by 3 until `n` becomes 0.
- The number of iterations is proportional to the number of digits in the base-3 representation of `n`.
- For a number `n`, the number of digits in base-3 is approximately O(log3(n)).
- Therefore, the time complexity is O(log3(n)).

Space Complexity Analysis:
- The algorithm uses a constant amount of space, as no additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Math, Greedy
"""