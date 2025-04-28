"""
LeetCode Question #1447: Simplified Fractions

Problem Statement:
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator 
is less-than-or-equal-to n. You can return the answer in any order.

A fraction is simplified if there is no common divisor other than 1 between the numerator and the denominator.

Example 1:
Input: n = 2
Output: ["1/2"]

Example 2:
Input: n = 3
Output: ["1/2", "1/3", "2/3"]

Example 3:
Input: n = 4
Output: ["1/2", "1/3", "1/4", "2/3", "3/4"]

Constraints:
1 <= n <= 100
"""

from math import gcd

def simplifiedFractions(n: int) -> list[str]:
    """
    Generate all simplified fractions between 0 and 1 (exclusive) with denominators <= n.

    :param n: Maximum denominator value.
    :return: List of simplified fractions as strings.
    """
    result = []
    for denominator in range(2, n + 1):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:  # Check if the fraction is simplified
                result.append(f"{numerator}/{denominator}")
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    print(simplifiedFractions(n))  # Output: ["1/2"]

    # Test Case 2
    n = 3
    print(simplifiedFractions(n))  # Output: ["1/2", "1/3", "2/3"]

    # Test Case 3
    n = 4
    print(simplifiedFractions(n))  # Output: ["1/2", "1/3", "1/4", "2/3", "3/4"]

    # Test Case 4
    n = 5
    print(simplifiedFractions(n))  # Output: ["1/2", "1/3", "1/4", "1/5", "2/3", "2/5", "3/4", "3/5", "4/5"]

    # Test Case 5
    n = 1
    print(simplifiedFractions(n))  # Output: []


"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs for `n - 1` iterations (denominator from 2 to n).
- The inner loop runs for `denominator - 1` iterations (numerator from 1 to denominator - 1).
- For each pair of numerator and denominator, we compute the gcd, which takes O(log(min(numerator, denominator))) time.
- In the worst case, the total number of iterations is approximately O(n^2), and each gcd computation takes O(log(n)).
- Therefore, the overall time complexity is O(n^2 * log(n)).

Space Complexity:
- The space complexity is O(k), where k is the number of simplified fractions generated, as we store the results in a list.
- The gcd computation uses O(1) additional space.
- Therefore, the overall space complexity is O(k).

Topic: Math
"""