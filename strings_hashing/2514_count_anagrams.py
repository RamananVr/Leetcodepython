"""
LeetCode Question #2514: Count Anagrams

Problem Statement:
You are given a string `s` containing lowercase English letters. You need to count the number of distinct anagrams of all substrings of `s`. 
Two substrings are considered different if their starting or ending indices are different, even if they are anagrams of each other.

Return the total number of distinct anagrams of all substrings of `s`.

Constraints:
- 1 <= s.length <= 1000
- `s` consists of lowercase English letters.

Example:
Input: s = "abc"
Output: 6
Explanation: The substrings of "abc" are:
- "a", "b", "c", "ab", "bc", "abc"
The distinct anagrams are: "a", "b", "c", "ab", "bc", "abc". Hence, the output is 6.
"""

from collections import Counter

def countAnagrams(s: str) -> int:
    """
    Function to count the number of distinct anagrams of all substrings of the input string `s`.
    """
    # Use a set to store unique anagram signatures
    anagram_signatures = set()
    
    # Iterate over all substrings of `s`
    for i in range(len(s)):
        char_count = [0] * 26  # Array to store character counts for the current substring
        for j in range(i, len(s)):
            # Update the character count for the current character
            char_count[ord(s[j]) - ord('a')] += 1
            # Convert the character count array to a tuple (anagram signature)
            anagram_signatures.add(tuple(char_count))
    
    # The size of the set gives the number of distinct anagrams
    return len(anagram_signatures)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(f"Input: {s1}, Output: {countAnagrams(s1)}")  # Expected Output: 6

    # Test Case 2
    s2 = "aaa"
    print(f"Input: {s2}, Output: {countAnagrams(s2)}")  # Expected Output: 3

    # Test Case 3
    s3 = "ababa"
    print(f"Input: {s3}, Output: {countAnagrams(s3)}")  # Expected Output: 10

    # Test Case 4
    s4 = "abcd"
    print(f"Input: {s4}, Output: {countAnagrams(s4)}")  # Expected Output: 10

    # Test Case 5
    s5 = "a"
    print(f"Input: {s5}, Output: {countAnagrams(s5)}")  # Expected Output: 1

"""
Time Complexity Analysis:
- The outer loop runs `n` times (for each starting index of the substring).
- The inner loop runs approximately `n/2` times on average (for each ending index of the substring).
- For each substring, we compute the character count array (O(26) = O(1)) and add it to the set.
- Overall, the time complexity is O(n^2), where `n` is the length of the string.

Space Complexity Analysis:
- The space complexity is O(n^2) in the worst case, as the set can store up to O(n^2) unique anagram signatures (one for each substring).

Topic: Strings, Hashing
"""