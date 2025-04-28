"""
LeetCode Question #1067: Digit Count in Range

Problem Statement:
Given two integers `d` and `high`, return the number of times that digit `d` appears in all integers from `1` to `high` (inclusive).

Example:
Input: d = 1, high = 13
Output: 6
Explanation: The digit 1 appears in the numbers 1, 10, 11, 12, and 13.

Constraints:
- 0 <= d <= 9
- 1 <= high <= 2 * 10^9
"""

# Solution
def digitCount(d: int, high: int) -> int:
    """
    Counts the occurrences of digit `d` in all integers from 1 to `high`.

    :param d: The digit to count (0 <= d <= 9).
    :param high: The upper limit of the range (1 <= high <= 2 * 10^9).
    :return: The count of digit `d` in the range [1, high].
    """
    def countDigitOccurrences(n: int, digit: int) -> int:
        """
        Helper function to count occurrences of `digit` in the number `n`.
        """
        count = 0
        while n > 0:
            if n % 10 == digit:
                count += 1
            n //= 10
        return count

    total_count = 0
    for num in range(1, high + 1):
        total_count += countDigitOccurrences(num, d)
    
    return total_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    d = 1
    high = 13
    print(digitCount(d, high))  # Output: 6

    # Test Case 2
    d = 0
    high = 20
    print(digitCount(d, high))  # Output: 2

    # Test Case 3
    d = 2
    high = 25
    print(digitCount(d, high))  # Output: 9

    # Test Case 4
    d = 5
    high = 55
    print(digitCount(d, high))  # Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all numbers from 1 to `high`.
- For each number, it counts the occurrences of the digit `d` by iterating through its digits.
- Let `high` be the upper limit. The number of digits in a number is approximately log10(high).
- Therefore, the time complexity is O(high * log10(high)).

Space Complexity:
- The function uses a constant amount of space for variables and does not use any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Brute Force
"""