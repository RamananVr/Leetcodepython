"""
LeetCode Problem #2287: Rearrange Characters to Make Target String

Problem Statement:
You are given two strings `s` and `target`. You can take some letters from `s` and rearrange them to form new strings.
Return the maximum number of copies of `target` that can be formed by taking letters from `s` and rearranging them.

Constraints:
- `1 <= s.length, target.length <= 100`
- `s` and `target` consist of lowercase English letters.

Example:
Input: s = "ilovecodingonleetcode", target = "code"
Output: 2
Explanation: You can create two "code" strings from the letters in `s`.

Input: s = "abcba", target = "abc"
Output: 1
Explanation: You can create one "abc" string from the letters in `s`.

Input: s = "abbaccaddaeea", target = "aaaa"
Output: 1
Explanation: You can create one "aaaa" string from the letters in `s`.
"""

from collections import Counter

def rearrangeCharacters(s: str, target: str) -> int:
    """
    Function to calculate the maximum number of copies of `target` 
    that can be formed using letters from `s`.
    """
    # Count the frequency of each character in `s` and `target`
    s_count = Counter(s)
    target_count = Counter(target)
    
    # Calculate the maximum number of times `target` can be formed
    max_copies = float('inf')
    for char in target_count:
        if char in s_count:
            max_copies = min(max_copies, s_count[char] // target_count[char])
        else:
            return 0  # If a required character is missing, return 0
    
    return max_copies

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ilovecodingonleetcode"
    target1 = "code"
    print(rearrangeCharacters(s1, target1))  # Output: 2

    # Test Case 2
    s2 = "abcba"
    target2 = "abc"
    print(rearrangeCharacters(s2, target2))  # Output: 1

    # Test Case 3
    s3 = "abbaccaddaeea"
    target3 = "aaaa"
    print(rearrangeCharacters(s3, target3))  # Output: 1

    # Test Case 4
    s4 = "xyz"
    target4 = "abc"
    print(rearrangeCharacters(s4, target4))  # Output: 0

    # Test Case 5
    s5 = "aabbcc"
    target5 = "abc"
    print(rearrangeCharacters(s5, target5))  # Output: 1

"""
Time Complexity:
- Counting the characters in `s` and `target` takes O(n + m), where `n` is the length of `s` and `m` is the length of `target`.
- Iterating through the characters in `target_count` takes O(m).
- Overall time complexity: O(n + m).

Space Complexity:
- The `Counter` objects for `s` and `target` use O(n + m) space.
- Overall space complexity: O(n + m).

Topic: Hash Table / String Manipulation
"""