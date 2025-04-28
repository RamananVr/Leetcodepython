"""
LeetCode Problem #1689: Partitioning Into Minimum Number Of Deci-Binary Numbers

Problem Statement:
A decimal number is called a deci-binary number if each of its digits is either 0 or 1 without 
leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string `n` that represents a positive decimal integer, return the minimum number of 
positive deci-binary numbers needed so that they sum up to `n`.

Constraints:
- 1 <= n.length <= 10^5
- n consists of only digits.
- n does not contain any leading zeros and represents a positive integer.

Example:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Input: n = "82734"
Output: 8

Input: n = "27346209830709182346"
Output: 9
"""

# Python Solution
def minPartitions(n: str) -> int:
    """
    Returns the minimum number of deci-binary numbers needed to sum up to the given number `n`.

    :param n: A string representing a positive decimal integer.
    :return: An integer representing the minimum number of deci-binary numbers.
    """
    # The minimum number of deci-binary numbers required is equal to the maximum digit in `n`.
    return max(map(int, n))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = "32"
    print(f"Input: {n1}, Output: {minPartitions(n1)}")  # Expected Output: 3

    # Test Case 2
    n2 = "82734"
    print(f"Input: {n2}, Output: {minPartitions(n2)}")  # Expected Output: 8

    # Test Case 3
    n3 = "27346209830709182346"
    print(f"Input: {n3}, Output: {minPartitions(n3)}")  # Expected Output: 9

    # Test Case 4
    n4 = "11111"
    print(f"Input: {n4}, Output: {minPartitions(n4)}")  # Expected Output: 1

    # Test Case 5
    n5 = "0"
    print(f"Input: {n5}, Output: {minPartitions(n5)}")  # Expected Output: 0 (Invalid input as per constraints)

"""
Time Complexity Analysis:
- The function iterates through all the digits of the string `n` to find the maximum digit.
- Let `L` be the length of the string `n`. The time complexity is O(L).

Space Complexity Analysis:
- The function uses a constant amount of extra space, as it only stores the maximum digit.
- The space complexity is O(1).

Topic: Strings
"""