"""
LeetCode Problem #830: Positions of Large Groups

Problem Statement:
In a string `s` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `s = "abbxxxxzyy"` has the groups `["a", "bb", "xxxx", "z", "yy"]`.

A group is identified as "large" if it has 3 or more consecutive characters. Return a list of the starting and ending positions of every large group sorted in increasing order by their starting position.

Example:
Input: s = "abbxxxxzzy"
Output: [[3, 6]]
Explanation: "xxxx" is the only large group, starting at index 3 and ending at index 6.

Constraints:
- 1 <= s.length <= 10^4
- s contains only lowercase English letters.
"""

# Python Solution
def largeGroupPositions(s: str):
    """
    Finds the starting and ending positions of all large groups in the string.

    :param s: Input string containing lowercase English letters.
    :return: List of [start, end] positions for each large group.
    """
    result = []
    n = len(s)
    i = 0

    while i < n:
        start = i
        # Move `i` forward while the current character matches the next one
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        # Check if the group size is large (3 or more characters)
        if i - start + 1 >= 3:
            result.append([start, i])
        i += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abbxxxxzzy"
    print(largeGroupPositions(s1))  # Output: [[3, 6]]

    # Test Case 2
    s2 = "abc"
    print(largeGroupPositions(s2))  # Output: []

    # Test Case 3
    s3 = "abcdddeeeeaabbbcd"
    print(largeGroupPositions(s3))  # Output: [[3, 5], [6, 9], [12, 14]]

    # Test Case 4
    s4 = "aaa"
    print(largeGroupPositions(s4))  # Output: [[0, 2]]

    # Test Case 5
    s5 = "aabbcc"
    print(largeGroupPositions(s5))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the string once, making it O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(k), where k is the number of large groups in the string. The result list stores the start and end indices of each large group.
- No additional space is used apart from the result list.

Overall: Time Complexity = O(n), Space Complexity = O(k)
"""

# Topic: Strings