"""
LeetCode Problem #2839: Check if Strings Can be Made Equal With Operations I

Problem Statement:
You are given two strings `s1` and `s2`, both of length 4, consisting of lowercase English letters.

You can perform the following operation on any of the two strings:
- Swap the characters at indices 0 and 1, or swap the characters at indices 2 and 3.

Return `true` if you can make the strings equal using any number of operations, otherwise return `false`.

Example 1:
Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: You can swap the first two characters of s1 to get "bacd", then swap the last two characters to get "cdab".

Example 2:
Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: No sequence of operations can make the strings equal.

Constraints:
- `s1.length == 4`
- `s2.length == 4`
- `s1` and `s2` consist of lowercase English letters.
"""

# Python Solution
def canBeEqual(s1: str, s2: str) -> bool:
    # To make s1 equal to s2, the characters at indices [0, 1] and [2, 3] must match in any order.
    return sorted(s1[:2]) == sorted(s2[:2]) and sorted(s1[2:]) == sorted(s2[2:])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcd"
    s2 = "cdab"
    print(canBeEqual(s1, s2))  # Output: True

    # Test Case 2
    s1 = "abcd"
    s2 = "dacb"
    print(canBeEqual(s1, s2))  # Output: False

    # Test Case 3
    s1 = "aabb"
    s2 = "bbaa"
    print(canBeEqual(s1, s2))  # Output: True

    # Test Case 4
    s1 = "abcd"
    s2 = "abdc"
    print(canBeEqual(s1, s2))  # Output: True

    # Test Case 5
    s1 = "abcd"
    s2 = "abcd"
    print(canBeEqual(s1, s2))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the first two characters of `s1` and `s2` takes O(2) = O(1).
- Sorting the last two characters of `s1` and `s2` also takes O(2) = O(1).
- Therefore, the overall time complexity is O(1).

Space Complexity:
- The sorting operation uses constant space since the input size is fixed at 4 characters.
- Therefore, the space complexity is O(1).

Topic: Strings
"""