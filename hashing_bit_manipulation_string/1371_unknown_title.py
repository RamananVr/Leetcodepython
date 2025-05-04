"""
LeetCode Problem #1371: Find the Longest Substring Containing Vowels in Even Counts

Problem Statement:
Given the string `s`, return the size of the longest substring containing each vowel 
('a', 'e', 'i', 'o', 'u') an even number of times. 

This problem can be solved using a bitmask to represent the parity (even or odd) of 
the counts of vowels. Each vowel corresponds to a specific bit in the bitmask:
- 'a' -> bit 0
- 'e' -> bit 1
- 'i' -> bit 2
- 'o' -> bit 3
- 'u' -> bit 4

The goal is to find the longest substring where the bitmask is the same at two indices, 
indicating that the counts of vowels between those indices are even.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of lowercase English letters.

Example:
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains all vowels in even counts.

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains all vowels in even counts.

Input: s = "bcbcbc"
Output: 6
Explanation: The entire string is the longest substring since it contains no vowels.

"""

def findTheLongestSubstring(s: str) -> int:
    # Map vowels to their respective bit positions
    vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    # Initialize the bitmask and a dictionary to store the first occurrence of each bitmask
    bitmask = 0
    first_occurrence = {0: -1}  # Bitmask 0 is initialized at index -1
    max_length = 0

    for i, char in enumerate(s):
        # If the character is a vowel, toggle the corresponding bit in the bitmask
        if char in vowel_to_bit:
            bitmask ^= (1 << vowel_to_bit[char])
        
        # If the current bitmask has been seen before, calculate the length of the substring
        if bitmask in first_occurrence:
            max_length = max(max_length, i - first_occurrence[bitmask])
        else:
            # Otherwise, store the first occurrence of this bitmask
            first_occurrence[bitmask] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "eleetminicoworoep"
    print(findTheLongestSubstring(s1))  # Output: 13

    # Test Case 2
    s2 = "leetcodeisgreat"
    print(findTheLongestSubstring(s2))  # Output: 5

    # Test Case 3
    s3 = "bcbcbc"
    print(findTheLongestSubstring(s3))  # Output: 6

    # Test Case 4
    s4 = "aeiou"
    print(findTheLongestSubstring(s4))  # Output: 0

    # Test Case 5
    s5 = "aabbccddeeiioouu"
    print(findTheLongestSubstring(s5))  # Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, performing constant-time operations 
  for each character. Thus, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The space complexity is O(2^5) = O(32), which is constant, as the bitmask can have at most 
  32 unique values (since there are 5 vowels, and each bitmask represents a combination of 
  their parities). Additionally, the `first_occurrence` dictionary stores at most 32 entries.

Topic: Hashing, Bit Manipulation, String
"""