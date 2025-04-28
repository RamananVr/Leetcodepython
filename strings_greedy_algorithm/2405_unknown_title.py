"""
LeetCode Problem #2405: Optimal Partition of String

Problem Statement:
Given a string `s`, partition the string into one or more substrings such that the characters in each substring are unique. Return the minimum number of substrings in such a partition.

Example:
Input: s = "abac"
Output: 2
Explanation: The string can be partitioned as ["ab", "ac"]. Each substring contains unique characters.

Input: s = "aabb"
Output: 2
Explanation: The string can be partitioned as ["ab", "ab"]. Each substring contains unique characters.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

# Solution
def partitionString(s: str) -> int:
    """
    Partition the string into substrings such that each substring contains unique characters.
    Return the minimum number of substrings.

    :param s: Input string
    :return: Minimum number of substrings
    """
    partitions = 0
    seen = set()

    for char in s:
        if char in seen:
            # Start a new partition
            partitions += 1
            seen.clear()
        seen.add(char)

    # Count the last partition
    return partitions + 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abac"
    print(partitionString(s1))  # Expected Output: 2

    # Test Case 2
    s2 = "aabb"
    print(partitionString(s2))  # Expected Output: 2

    # Test Case 3
    s3 = "abcdef"
    print(partitionString(s3))  # Expected Output: 1

    # Test Case 4
    s4 = "aaaa"
    print(partitionString(s4))  # Expected Output: 4

    # Test Case 5
    s5 = "abacaba"
    print(partitionString(s5))  # Expected Output: 4


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `s` once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(1) for the `seen` set, as it can contain at most 26 characters (all lowercase English letters).
- Thus, the space complexity is O(1).
"""

# Topic: Strings, Greedy Algorithm