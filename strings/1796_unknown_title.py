"""
LeetCode Problem #1796: Second Largest Digit in a String

Problem Statement:
Given an alphanumeric string `s`, return the second largest numerical digit that appears in `s`, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters and/or digits.
"""

def second_highest(s: str) -> int:
    """
    Finds the second largest numerical digit in the given alphanumeric string.

    :param s: A string consisting of lowercase English letters and digits.
    :return: The second largest numerical digit, or -1 if it does not exist.
    """
    # Use a set to store unique digits found in the string
    digits = set()

    # Iterate through the string and add digits to the set
    for char in s:
        if char.isdigit():
            digits.add(int(char))

    # Convert the set to a sorted list in descending order
    sorted_digits = sorted(digits, reverse=True)

    # Return the second largest digit if it exists, otherwise return -1
    return sorted_digits[1] if len(sorted_digits) > 1 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "dfa12321afd"
    print(second_highest(s1))  # Output: 2

    # Test Case 2
    s2 = "abc1111"
    print(second_highest(s2))  # Output: -1

    # Test Case 3
    s3 = "abc123456789"
    print(second_highest(s3))  # Output: 8

    # Test Case 4
    s4 = "a1b2c3d4e5f6g7h8i9j0"
    print(second_highest(s4))  # Output: 8

    # Test Case 5
    s5 = "no_digits_here"
    print(second_highest(s5))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- O(n): We iterate through the string `s` once to extract digits, where `n` is the length of the string.
- O(k log k): Sorting the unique digits, where `k` is the number of unique digits (at most 10 since there are only 10 possible digits).
- Overall: O(n + k log k), which simplifies to O(n) since `k` is a constant (at most 10).

Space Complexity:
- O(k): We use a set to store unique digits, where `k` is the number of unique digits (at most 10).
- Overall: O(1) since `k` is a constant.

Topic: Strings
"""