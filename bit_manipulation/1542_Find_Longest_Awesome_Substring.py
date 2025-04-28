"""
LeetCode Problem #1542: Find Longest Awesome Substring

Problem Statement:
Given a string `s`. An awesome substring is a non-empty substring of `s` such that we can make at most one 
character have an odd frequency after removing some characters (possibly zero). Return the length of the 
maximum length awesome substring of `s`.

Example:
Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can make all characters have even frequency 
except for '5'.

Constraints:
1. 1 <= s.length <= 10^5
2. s consists only of digits ('0' - '9').
"""

def longestAwesome(s: str) -> int:
    """
    Finds the length of the longest awesome substring in the given string `s`.
    """
    # Dictionary to store the first occurrence of each bitmask
    first_occurrence = {0: -1}
    max_length = 0
    current_mask = 0

    for i, char in enumerate(s):
        # Update the current bitmask by toggling the bit corresponding to the current digit
        digit = int(char)
        current_mask ^= (1 << digit)

        # Check if the current bitmask has been seen before
        if current_mask in first_occurrence:
            max_length = max(max_length, i - first_occurrence[current_mask])
        else:
            first_occurrence[current_mask] = i

        # Check all possible bitmasks with one bit toggled (to allow one odd frequency)
        for j in range(10):
            toggled_mask = current_mask ^ (1 << j)
            if toggled_mask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[toggled_mask])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "3242415"
    print(longestAwesome(s1))  # Output: 5

    # Test Case 2
    s2 = "12345678"
    print(longestAwesome(s2))  # Output: 1

    # Test Case 3
    s3 = "213123"
    print(longestAwesome(s3))  # Output: 6

    # Test Case 4
    s4 = "0000"
    print(longestAwesome(s4))  # Output: 4

    # Test Case 5
    s5 = "1"
    print(longestAwesome(s5))  # Output: 1

"""
Time Complexity:
- The algorithm iterates through the string `s` once, so the time complexity is O(n), where `n` is the length of the string.
- For each character, we check up to 10 possible toggled masks, which is a constant operation. Thus, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(2^10) = O(1024) = O(1) for the `first_occurrence` dictionary, as there are at most 2^10 possible bitmasks.
- Therefore, the space complexity is O(1) in practice.

Topic: Bit Manipulation
"""