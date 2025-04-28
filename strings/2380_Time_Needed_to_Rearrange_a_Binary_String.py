"""
LeetCode Problem #2380: Time Needed to Rearrange a Binary String

Problem Statement:
You are given a binary string `s` consisting only of characters '0' and '1'. In one second, all occurrences of "01" in the string can be simultaneously replaced with "10". This process is repeated until no more "01" can be found.

Return the number of seconds needed to complete this process.

Example 1:
Input: s = "0110101"
Output: 4
Explanation:
After 1 second: "1011010"
After 2 seconds: "1101100"
After 3 seconds: "1110010"
After 4 seconds: "1111000"
No more "01" can be found, so the process stops after 4 seconds.

Example 2:
Input: s = "11100"
Output: 0
Explanation:
No "01" can be found, so the process stops immediately.

Constraints:
- 1 <= s.length <= 1000
- s[i] is either '0' or '1'.
"""

def seconds_to_rearrange_binary_string(s: str) -> int:
    """
    Calculate the number of seconds needed to rearrange the binary string
    such that no "01" remains.

    :param s: A binary string consisting of '0' and '1'.
    :return: The number of seconds needed to complete the process.
    """
    seconds = 0
    while "01" in s:
        s = s.replace("01", "10")
        seconds += 1
    return seconds

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "0110101"
    print(seconds_to_rearrange_binary_string(s1))  # Output: 4

    # Test Case 2
    s2 = "11100"
    print(seconds_to_rearrange_binary_string(s2))  # Output: 0

    # Test Case 3
    s3 = "000111"
    print(seconds_to_rearrange_binary_string(s3))  # Output: 3

    # Test Case 4
    s4 = "101010"
    print(seconds_to_rearrange_binary_string(s4))  # Output: 5

    # Test Case 5
    s5 = "0"
    print(seconds_to_rearrange_binary_string(s5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `replace` operation scans the string to find occurrences of "01" and replaces them with "10".
- In the worst case, the string length is reduced by 1 "01" pair per second, leading to O(n^2) complexity.
- Specifically, for a string of length n, the first iteration takes O(n), the second iteration takes O(n-1), and so on.
- This results in a total complexity of O(n^2).

Space Complexity:
- The space complexity is O(n), as the string `s` is modified in-place and no additional data structures are used.

Topic: Strings
"""