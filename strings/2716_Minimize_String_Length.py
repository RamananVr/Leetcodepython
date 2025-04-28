"""
LeetCode Problem #2716: Minimize String Length

Problem Statement:
Given a string `s`, you are allowed to perform the following operation any number of times:
- Choose a character from `s` and remove all occurrences of it.

Return the minimum possible length of the string after performing the above operation any number of times.

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
"""

# Solution
def minimizeStringLength(s: str) -> int:
    """
    This function returns the minimum possible length of the string after removing all occurrences
    of any character any number of times.

    Args:
    s (str): The input string consisting of lowercase English letters.

    Returns:
    int: The minimum possible length of the string.
    """
    # The minimum length of the string is equal to the number of unique characters in the string.
    return len(set(s))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaabbbccc"
    print(minimizeStringLength(s1))  # Expected Output: 3 (unique characters: 'a', 'b', 'c')

    # Test Case 2
    s2 = "abc"
    print(minimizeStringLength(s2))  # Expected Output: 3 (unique characters: 'a', 'b', 'c')

    # Test Case 3
    s3 = "aaaa"
    print(minimizeStringLength(s3))  # Expected Output: 1 (unique character: 'a')

    # Test Case 4
    s4 = "leetcode"
    print(minimizeStringLength(s4))  # Expected Output: 6 (unique characters: 'l', 'e', 't', 'c', 'o', 'd')

    # Test Case 5
    s5 = "aabbccddeeff"
    print(minimizeStringLength(s5))  # Expected Output: 6 (unique characters: 'a', 'b', 'c', 'd', 'e', 'f')

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses the `set()` operation to find unique characters in the string `s`.
- Constructing a set from a string takes O(n), where `n` is the length of the string.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is O(u), where `u` is the number of unique characters in the string.
- In the worst case, `u` can be equal to `n` (if all characters in the string are unique).
- Therefore, the space complexity is O(n).

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Strings