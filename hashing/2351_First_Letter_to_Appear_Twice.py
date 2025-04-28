"""
LeetCode Problem #2351: First Letter to Appear Twice

Problem Statement:
Given a string `s` consisting of lowercase English letters, return the first letter to appear twice.

Note:
- A letter `a` appears twice before another letter `b` if the second occurrence of `a` is before the second occurrence of `b`.
- `s` will contain at least one letter that appears twice.

Example 1:
Input: s = "abccbaacz"
Output: "c"
Explanation: The letter 'c' is the first letter to appear twice, as it appears at indices 2 and 3.

Example 2:
Input: s = "abcdd"
Output: "d"
Explanation: The letter 'd' is the first letter to appear twice, as it appears at indices 3 and 4.

Constraints:
- 2 <= s.length <= 100
- `s` consists of lowercase English letters.
- There will be at least one letter that appears twice.
"""

def repeatedCharacter(s: str) -> str:
    """
    Finds the first letter to appear twice in the string `s`.

    :param s: A string consisting of lowercase English letters.
    :return: The first letter to appear twice.
    """
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return ""  # This line will never be reached due to the problem constraints.

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abccbaacz"
    print(repeatedCharacter(s1))  # Output: "c"

    # Test Case 2
    s2 = "abcdd"
    print(repeatedCharacter(s2))  # Output: "d"

    # Test Case 3
    s3 = "aabbcc"
    print(repeatedCharacter(s3))  # Output: "a"

    # Test Case 4
    s4 = "xyzyx"
    print(repeatedCharacter(s4))  # Output: "y"

"""
Time Complexity Analysis:
- The function iterates through the string `s` once, performing O(1) operations (set lookup and insertion) for each character.
- Let `n` be the length of the string `s`. The time complexity is O(n).

Space Complexity Analysis:
- The function uses a set to store seen characters. In the worst case, the set will contain all unique characters of `s`.
- Since `s` consists of lowercase English letters, the maximum size of the set is 26.
- Thus, the space complexity is O(1) (constant space).

Topic: Hashing
"""