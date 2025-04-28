"""
LeetCode Problem #1915: Number of Wonderful Substrings

Problem Statement:
A string is called wonderful if it is possible to rearrange its characters to make it a palindrome. 
For example, the string "ccaa" is wonderful because we can rearrange it to "acca", which is a palindrome.

Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), 
return the number of wonderful non-empty substrings in word. If the same substring appears multiple times 
in different positions, it should be counted multiple times.

A substring is a contiguous sequence of characters in a string.

Constraints:
- 1 <= word.length <= 10^5
- word consists of characters from 'a' to 'j' only.
"""

# Python Solution
def wonderfulSubstrings(word: str) -> int:
    """
    This function calculates the number of wonderful substrings in the given string.
    """
    # Initialize a dictionary to store the frequency of each bitmask
    freq = {0: 1}
    mask = 0
    result = 0

    for char in word:
        # Update the mask by flipping the bit corresponding to the current character
        mask ^= 1 << (ord(char) - ord('a'))

        # Add the count of substrings with the same mask (even frequency for all characters)
        result += freq.get(mask, 0)

        # Check for masks with one bit flipped (odd frequency for one character)
        for i in range(10):
            result += freq.get(mask ^ (1 << i), 0)

        # Update the frequency of the current mask
        freq[mask] = freq.get(mask, 0) + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "aba"
    print(wonderfulSubstrings(word1))  # Expected Output: 4

    # Test Case 2
    word2 = "aabb"
    print(wonderfulSubstrings(word2))  # Expected Output: 9

    # Test Case 3
    word3 = "he"
    print(wonderfulSubstrings(word3))  # Expected Output: 2

    # Test Case 4
    word4 = "abcde"
    print(wonderfulSubstrings(word4))  # Expected Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- For each character, we also check up to 10 possible masks (one for each bit flip).
- Thus, the time complexity is O(n * 10) = O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(2^10) = O(1), as the frequency dictionary can store at most 2^10 = 1024 unique masks.
- This is constant space since the number of masks is independent of the input size.
"""

# Topic: Bit Manipulation, Hash Table