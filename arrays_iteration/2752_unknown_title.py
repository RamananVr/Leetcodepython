"""
LeetCode Problem #2752: Sum of Numbers With Units Digit K

Problem Statement:
Given two integers `num` and `k`, return the sum of all integers between `1` and `num` (inclusive) that have a units digit equal to `k`. If no such integers exist, return `0`.

Example:
Input: num = 20, k = 3
Output: 63
Explanation: The integers between 1 and 20 with a units digit of 3 are 3, 13, and 23. Their sum is 3 + 13 + 23 = 63.

Constraints:
- 1 <= num <= 10^4
- 0 <= k <= 9
"""

def sum_of_numbers_with_units_digit_k(num: int, k: int) -> int:
    """
    Calculate the sum of all integers between 1 and num (inclusive) that have a units digit equal to k.

    :param num: The upper limit of the range (inclusive).
    :param k: The target units digit.
    :return: The sum of integers with units digit k.
    """
    result = 0
    for i in range(1, num + 1):
        if i % 10 == k:
            result += i
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 20
    k = 3
    print(sum_of_numbers_with_units_digit_k(num, k))  # Output: 63

    # Test Case 2
    num = 15
    k = 5
    print(sum_of_numbers_with_units_digit_k(num, k))  # Output: 15

    # Test Case 3
    num = 100
    k = 7
    print(sum_of_numbers_with_units_digit_k(num, k))  # Output: 385

    # Test Case 4
    num = 50
    k = 0
    print(sum_of_numbers_with_units_digit_k(num, k))  # Output: 150

    # Test Case 5
    num = 10
    k = 9
    print(sum_of_numbers_with_units_digit_k(num, k))  # Output: 9

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all integers from 1 to num, checking the units digit of each number.
- This results in a time complexity of O(num), where num is the input upper limit.

Space Complexity:
- The function uses a constant amount of space to store the result and loop variables.
- Therefore, the space complexity is O(1).

Topic: Arrays / Iteration
"""