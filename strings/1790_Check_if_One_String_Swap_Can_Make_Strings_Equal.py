"""
LeetCode Problem #1790: Check if One String Swap Can Make Strings Equal

Problem Statement:
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices i and j 
(0-indexed) in a string and swap the characters at s1[i] and s1[j].

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. 
Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: Swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no swap is needed.

Example 4:
Input: s1 = "abcd", s2 = "dcba"
Output: false

Constraints:
- s1.length == s2.length
- 1 <= s1.length <= 100
- s1 and s2 consist of only lowercase English letters.
"""

def areAlmostEqual(s1: str, s2: str) -> bool:
    """
    Check if one string swap can make the two strings equal.

    :param s1: First string
    :param s2: Second string
    :return: True if the strings can be made equal with at most one swap, False otherwise
    """
    # If the strings are already equal, no swap is needed
    if s1 == s2:
        return True

    # Find the indices where the characters differ
    diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]

    # There must be exactly two differences, and swapping them should make the strings equal
    return len(diff) == 2 and diff[0] == diff[1][::-1]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "bank"
    s2 = "kanb"
    print(areAlmostEqual(s1, s2))  # Output: True

    # Test Case 2
    s1 = "attack"
    s2 = "defend"
    print(areAlmostEqual(s1, s2))  # Output: False

    # Test Case 3
    s1 = "kelb"
    s2 = "kelb"
    print(areAlmostEqual(s1, s2))  # Output: True

    # Test Case 4
    s1 = "abcd"
    s2 = "dcba"
    print(areAlmostEqual(s1, s2))  # Output: False

    # Test Case 5
    s1 = "aa"
    s2 = "aa"
    print(areAlmostEqual(s1, s2))  # Output: True


"""
Time Complexity Analysis:
- The function iterates through the strings once to find the differing characters.
- This takes O(n) time, where n is the length of the strings.

Space Complexity Analysis:
- The function uses a list to store the differing character pairs, which can have at most two elements.
- This takes O(1) additional space.

Overall:
Time Complexity: O(n)
Space Complexity: O(1)

Topic: Strings
"""