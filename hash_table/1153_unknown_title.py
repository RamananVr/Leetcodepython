"""
LeetCode Problem #1153: String Transforms Into Another String

Problem Statement:
Given two strings str1 and str2 of the same length, determine if str1 can be transformed into str2 by performing zero or more character-to-character mappings.

Each mapping must be a one-to-one mapping (i.e., no two characters in str1 can map to the same character in str2), and a character can map to itself.

Return true if and only if str1 can be transformed into str2.

Constraints:
- str1 and str2 are of the same length.
- Both strings contain only lowercase English letters.

Example 1:
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'a' -> 'c', 'b' -> 'd', 'c' -> 'e'.

Example 2:
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 into str2.

Example 3:
Input: str1 = "aabcc", str2 = "ccdaa"
Output: false
Explanation: 'a' cannot map to both 'c' and 'd'.

Follow-up:
- You may assume that the strings are of the same length and contain only lowercase English letters.
"""

def canConvert(str1: str, str2: str) -> bool:
    """
    Determines if str1 can be transformed into str2 using one-to-one character mappings.
    """
    # If the strings are already equal, no transformation is needed
    if str1 == str2:
        return True

    # Create a mapping from characters in str1 to characters in str2
    mapping = {}
    for c1, c2 in zip(str1, str2):
        if c1 in mapping:
            # If the mapping is inconsistent, return False
            if mapping[c1] != c2:
                return False
        else:
            mapping[c1] = c2

    # Check if there are enough "spare" characters to allow transformation
    # If str2 uses all 26 characters, we cannot perform the transformation
    return len(set(str2)) < 26


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    str1 = "aabcc"
    str2 = "ccdee"
    print(canConvert(str1, str2))  # Output: True

    # Test Case 2
    str1 = "leetcode"
    str2 = "codeleet"
    print(canConvert(str1, str2))  # Output: False

    # Test Case 3
    str1 = "aabcc"
    str2 = "ccdaa"
    print(canConvert(str1, str2))  # Output: False

    # Test Case 4
    str1 = "abc"
    str2 = "bcd"
    print(canConvert(str1, str2))  # Output: True

    # Test Case 5
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "bcdefghijklmnopqrstuvwxyza"
    print(canConvert(str1, str2))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the characters of str1 and str2 once, which takes O(n) time, where n is the length of the strings.
- Checking the size of the set of characters in str2 takes O(26) = O(1) since there are at most 26 unique lowercase English letters.

Overall time complexity: O(n).

Space Complexity:
- The mapping dictionary stores at most 26 key-value pairs (one for each unique character in str1), which takes O(1) space.
- The set of characters in str2 also takes O(1) space since there are at most 26 unique characters.

Overall space complexity: O(1).

Topic: Hash Table
"""