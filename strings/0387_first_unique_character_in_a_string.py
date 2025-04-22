"""
LeetCode Question #387: First Unique Character in a String

Problem Statement:
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
- 1 <= s.length <= 10^5
- `s` consists of only lowercase English letters.
"""

def firstUniqChar(s: str) -> int:
    """
    Finds the index of the first non-repeating character in the string `s`.
    If no such character exists, returns -1.
    """
    # Step 1: Count the frequency of each character in the string
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find the first character with a frequency of 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    # Step 3: If no unique character is found, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetcode"
    print(firstUniqChar(s1))  # Output: 0

    # Test Case 2
    s2 = "loveleetcode"
    print(firstUniqChar(s2))  # Output: 2

    # Test Case 3
    s3 = "aabb"
    print(firstUniqChar(s3))  # Output: -1

    # Test Case 4
    s4 = "abcabcdd"
    print(firstUniqChar(s4))  # Output: -1

    # Test Case 5
    s5 = "z"
    print(firstUniqChar(s5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters in the string takes O(n), where `n` is the length of the string.
- Iterating through the string to find the first unique character also takes O(n).
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(1) because the `char_count` dictionary stores at most 26 key-value pairs (one for each lowercase English letter).
- Thus, the space usage is constant with respect to the input size.

Topic: Strings
"""