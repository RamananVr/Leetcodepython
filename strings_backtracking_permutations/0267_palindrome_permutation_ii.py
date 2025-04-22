"""
LeetCode Question #267: Palindrome Permutation II

Problem Statement:
Given a string `s`, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be formed.

A string is a palindrome if it reads the same forward and backward. A permutation of a string is a rearrangement of its characters.

Example 1:
Input: s = "aabb"
Output: ["abba", "baab"]

Example 2:
Input: s = "abc"
Output: []

Constraints:
- 1 <= s.length <= 16
- s consists of only lowercase English letters.
"""

from collections import Counter
from itertools import permutations

def generatePalindromes(s: str) -> list:
    # Step 1: Count the frequency of each character
    char_count = Counter(s)
    
    # Step 2: Check if a palindrome can be formed
    odd_count = 0
    odd_char = ""
    half_string = []
    
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char
        # Add half of the characters to the half_string
        half_string.extend(char * (count // 2))
    
    # If more than one character has an odd frequency, a palindrome is not possible
    if odd_count > 1:
        return []
    
    # Step 3: Generate all unique permutations of the half_string
    half_permutations = set(permutations(half_string))
    
    # Step 4: Construct palindromes from the half permutations
    palindromes = []
    for half in half_permutations:
        half_str = ''.join(half)
        if odd_count == 1:
            # Add the odd character in the middle
            palindromes.append(half_str + odd_char + half_str[::-1])
        else:
            # No odd character, just mirror the half string
            palindromes.append(half_str + half_str[::-1])
    
    return palindromes

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabb"
    print("Input:", s1)
    print("Output:", generatePalindromes(s1))  # Expected: ["abba", "baab"]

    # Test Case 2
    s2 = "abc"
    print("Input:", s2)
    print("Output:", generatePalindromes(s2))  # Expected: []

    # Test Case 3
    s3 = "aaa"
    print("Input:", s3)
    print("Output:", generatePalindromes(s3))  # Expected: ["aaa"]

    # Test Case 4
    s4 = "aabbcc"
    print("Input:", s4)
    print("Output:", generatePalindromes(s4))  # Expected: ["abcacba", "bacdcab", ...]

"""
Time Complexity Analysis:
1. Counting character frequencies: O(n), where n is the length of the string `s`.
2. Generating permutations of the half string: O((n/2)!), where n/2 is the length of the half string.
3. Constructing palindromes: O((n/2)!) since we iterate over all permutations.

Overall Time Complexity: O(n + (n/2)!) ≈ O((n/2)!) for large n.

Space Complexity Analysis:
1. Space for the character count dictionary: O(k), where k is the number of unique characters in `s`.
2. Space for storing permutations: O((n/2)!) for the set of permutations.
3. Space for the result list: O((n/2)!) for storing palindromes.

Overall Space Complexity: O((n/2)!) for large n.

Topic: Strings, Backtracking, Permutations
"""