"""
LeetCode Problem #696: Count Binary Substrings

Problem Statement:
Given a binary string `s`, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 0's and 1's: "0011", "01", "1100", "10", "0011", and "01".

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01".

Constraints:
- 1 <= s.length <= 10^5
- `s[i]` is either '0' or '1'.
"""

def countBinarySubstrings(s: str) -> int:
    """
    Count the number of binary substrings with equal consecutive 0's and 1's.

    :param s: A binary string
    :return: The count of valid binary substrings
    """
    # Initialize variables to track consecutive groups
    prev_group_length = 0
    curr_group_length = 1
    count = 0

    # Iterate through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Increment the current group length if the character is the same as the previous one
            curr_group_length += 1
        else:
            # Add the minimum of the previous and current group lengths to the count
            count += min(prev_group_length, curr_group_length)
            # Update the previous group length and reset the current group length
            prev_group_length = curr_group_length
            curr_group_length = 1

    # Add the last group comparison
    count += min(prev_group_length, curr_group_length)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "00110011"
    print(f"Input: {s1} -> Output: {countBinarySubstrings(s1)}")  # Expected: 6

    # Test Case 2
    s2 = "10101"
    print(f"Input: {s2} -> Output: {countBinarySubstrings(s2)}")  # Expected: 4

    # Test Case 3
    s3 = "000111000"
    print(f"Input: {s3} -> Output: {countBinarySubstrings(s3)}")  # Expected: 6

    # Test Case 4
    s4 = "01"
    print(f"Input: {s4} -> Output: {countBinarySubstrings(s4)}")  # Expected: 1

    # Test Case 5
    s5 = "1111"
    print(f"Input: {s5} -> Output: {countBinarySubstrings(s5)}")  # Expected: 0

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables (prev_group_length, curr_group_length, count).
- Therefore, the space complexity is O(1).

Topic: Strings
"""