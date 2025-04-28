"""
LeetCode Problem #2310: Sum of Numbers With Units Digit K

Problem Statement:
Given two integers `num` and `k`, return the minimum number of non-negative integers whose sum is equal to `num` and each of which has a units digit of `k`. If it is not possible to form such a sum, return -1.

A number has a units digit of `k` if it is of the form `10 * x + k` for some non-negative integer `x`.

Example 1:
Input: num = 58, k = 9
Output: 2
Explanation: 
    - The two numbers can be 9 and 49.
    - 9 + 49 = 58.
    - Both numbers have a units digit of 9.

Example 2:
Input: num = 37, k = 2
Output: -1
Explanation: 
    - It is not possible to form 37 using any numbers with a units digit of 2.

Example 3:
Input: num = 0, k = 7
Output: 0
Explanation: 
    - No numbers are needed to sum up to 0.

Constraints:
- 0 <= num <= 10^5
- 0 <= k <= 9
"""

def minimumNumbers(num: int, k: int) -> int:
    """
    Returns the minimum number of non-negative integers with units digit k
    that sum up to num. If not possible, returns -1.
    """
    if num == 0:
        return 0  # No numbers are needed to sum up to 0.

    # Iterate over the possible count of numbers (1 to 10).
    for count in range(1, 11):
        # Check if the sum can be formed with `count` numbers.
        if (count * k) % 10 == num % 10 and count * k <= num:
            return count

    return -1  # If no valid count is found, return -1.

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1, k1 = 58, 9
    print(minimumNumbers(num1, k1))  # Output: 2

    # Test Case 2
    num2, k2 = 37, 2
    print(minimumNumbers(num2, k2))  # Output: -1

    # Test Case 3
    num3, k3 = 0, 7
    print(minimumNumbers(num3, k3))  # Output: 0

    # Test Case 4
    num4, k4 = 20, 5
    print(minimumNumbers(num4, k4))  # Output: 4

    # Test Case 5
    num5, k5 = 10, 0
    print(minimumNumbers(num5, k5))  # Output: 1

"""
Time Complexity Analysis:
- The loop iterates at most 10 times (from 1 to 10).
- Each iteration involves constant-time operations (modulus and multiplication).
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Therefore, the space complexity is O(1).

Topic: Math
"""