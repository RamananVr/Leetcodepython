"""
LeetCode Problem #1119: Remove Vowels from a String

Problem Statement:
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the resulting string.

Example 1:
Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:
Input: s = "aeiou"
Output: ""

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
"""

# Solution
def removeVowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(char for char in s if char not in vowels)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetcodeisacommunityforcoders"
    print(removeVowels(s1))  # Expected Output: "ltcdscmmntyfrcdrs"

    # Test Case 2
    s2 = "aeiou"
    print(removeVowels(s2))  # Expected Output: ""

    # Test Case 3
    s3 = "hello"
    print(removeVowels(s3))  # Expected Output: "hll"

    # Test Case 4
    s4 = "programming"
    print(removeVowels(s4))  # Expected Output: "prgrmmng"

    # Test Case 5
    s5 = "xyz"
    print(removeVowels(s5))  # Expected Output: "xyz"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through each character in the string s, which has a length of n.
- Checking membership in the set of vowels is an O(1) operation.
- Therefore, the overall time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The space complexity is O(1) for the set of vowels, as it is a fixed size.
- The resulting string is stored in memory, but this is considered output space and does not count towards the algorithm's space complexity.
- Therefore, the space complexity is O(1).
"""

# Topic: Strings