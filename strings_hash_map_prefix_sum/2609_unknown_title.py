"""
LeetCode Problem #2609: Find the Longest Balanced Substring of a Binary String

Problem Statement:
You are given a binary string `s` consisting only of characters '0' and '1'.

A substring of `s` is considered balanced if the number of '0's in the substring is equal to the number of '1's.

Return the length of the longest balanced substring of `s`.

If no balanced substring exists, return 0.

Constraints:
- 1 <= len(s) <= 10^5
- `s` consists only of '0' and '1'.

Example:
Input: s = "00110011"
Output: 8
Explanation: The entire string is balanced.

Input: s = "10101"
Output: 4
Explanation: The longest balanced substring is "1010".
"""

def findTheLongestBalancedSubstring(s: str) -> int:
    """
    Finds the length of the longest balanced substring in a binary string.

    :param s: A binary string consisting of '0' and '1'.
    :return: The length of the longest balanced substring.
    """
    max_length = 0
    count = 0
    balance_map = {0: -1}  # Maps balance to the earliest index where it occurs

    for i, char in enumerate(s):
        # Increment or decrement the balance based on the character
        if char == '0':
            count -= 1
        else:
            count += 1

        # If the balance has been seen before, calculate the length of the substring
        if count in balance_map:
            max_length = max(max_length, i - balance_map[count])
        else:
            # Store the first occurrence of this balance
            balance_map[count] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "00110011"
    print(findTheLongestBalancedSubstring(s1))  # Output: 8

    # Test Case 2
    s2 = "10101"
    print(findTheLongestBalancedSubstring(s2))  # Output: 4

    # Test Case 3
    s3 = "000111"
    print(findTheLongestBalancedSubstring(s3))  # Output: 6

    # Test Case 4
    s4 = "1111"
    print(findTheLongestBalancedSubstring(s4))  # Output: 0

    # Test Case 5
    s5 = "010101"
    print(findTheLongestBalancedSubstring(s5))  # Output: 6

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing O(1) operations for each character.
- Thus, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The algorithm uses a dictionary to store the balance values and their indices.
- In the worst case, the dictionary could store up to n unique balance values.
- Thus, the space complexity is O(n).

Topic: Strings, Hash Map, Prefix Sum
"""