"""
LeetCode Problem #1400: Construct K Palindrome Strings

Problem Statement:
Given a string `s` and an integer `k`, return `true` if you can use all the characters in `s` to construct `k` palindrome strings or `false` otherwise.

A string is a palindrome if it reads the same forward and backward.

Constraints:
1. 1 <= s.length <= 10^5
2. s consists of lowercase English letters.
3. 1 <= k <= 10^5
"""

def canConstruct(s: str, k: int) -> bool:
    """
    Determines if it is possible to construct k palindrome strings using all characters in s.

    Args:
    s (str): The input string.
    k (int): The number of palindrome strings to construct.

    Returns:
    bool: True if k palindrome strings can be constructed, False otherwise.
    """
    # If k is greater than the length of the string, it's impossible to construct k palindromes
    if k > len(s):
        return False

    # Count the frequency of each character
    from collections import Counter
    char_count = Counter(s)

    # Count the number of characters with odd frequencies
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # To construct k palindromes, the number of odd frequency characters must not exceed k
    return odd_count <= k


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case where k = 3 and it's possible to construct 3 palindromes
    s1, k1 = "annabelle", 3
    print(canConstruct(s1, k1))  # Expected output: True

    # Test Case 2: Impossible to construct k palindromes because k > len(s)
    s2, k2 = "leetcode", 9
    print(canConstruct(s2, k2))  # Expected output: False

    # Test Case 3: All characters can form a single palindrome
    s3, k3 = "racecar", 1
    print(canConstruct(s3, k3))  # Expected output: True

    # Test Case 4: Each character must form its own palindrome
    s4, k4 = "aaa", 3
    print(canConstruct(s4, k4))  # Expected output: True

    # Test Case 5: Not enough palindromes can be formed due to odd character counts
    s5, k5 = "abc", 2
    print(canConstruct(s5, k5))  # Expected output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting character frequencies using `Counter` takes O(n), where n is the length of the string `s`.
- Summing the odd frequencies takes O(26) = O(1) since there are at most 26 lowercase English letters.
- Overall time complexity: O(n).

Space Complexity:
- The `Counter` object stores at most 26 key-value pairs (one for each lowercase English letter).
- Overall space complexity: O(1) (constant space usage relative to the input size).

Topic: Strings
"""