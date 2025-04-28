"""
LeetCode Problem #893: Groups of Special-Equivalent Strings

Problem Statement:
You are given an array of strings `words`. A string `A` is special-equivalent to a string `B` if after any number of moves, 
you can make `A` equal to `B`.

A move consists of choosing two indices `i` and `j` (i != j) and swapping the characters at `A[i]` and `A[j]`.

Two strings are special-equivalent if they can be made equal by performing some number of moves on the characters at 
even indices separately from the characters at odd indices.

For example, "abcd" and "cdab" are special-equivalent because we can swap the characters at even indices 
(0 and 2) and the characters at odd indices (1 and 3) separately: "abcd" -> "cbad" -> "cdab".

A group of special-equivalent strings from `words` is a set of strings that are all special-equivalent to each other.

Return the number of groups of special-equivalent strings in `words`.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 20
- All words[i] have the same length.
- All words[i] consist of lowercase English letters.

Example:
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation:
- One group is ["abcd", "cdab", "cbad"].
- Another group is ["xyzz", "zzxy"].
- The last group is ["zzyx"].
Thus, there are 3 groups.
"""

# Python Solution
def numSpecialEquivGroups(words):
    """
    Returns the number of groups of special-equivalent strings in the input list `words`.

    :param words: List[str] - List of strings
    :return: int - Number of groups of special-equivalent strings
    """
    def encode(word):
        # Separate even and odd indexed characters, sort them, and return as a tuple
        even_chars = sorted(word[0::2])
        odd_chars = sorted(word[1::2])
        return (tuple(even_chars), tuple(odd_chars))
    
    # Use a set to store unique encodings
    unique_groups = set(encode(word) for word in words)
    return len(unique_groups)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    print(numSpecialEquivGroups(words1))  # Output: 3

    # Test Case 2
    words2 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    print(numSpecialEquivGroups(words2))  # Output: 3

    # Test Case 3
    words3 = ["a", "b", "c", "a", "c", "c"]
    print(numSpecialEquivGroups(words3))  # Output: 3

    # Test Case 4
    words4 = ["aa", "bb", "ab", "ba"]
    print(numSpecialEquivGroups(words4))  # Output: 4

    # Test Case 5
    words5 = ["abcabc", "cbaabc", "abcabc", "cbacba"]
    print(numSpecialEquivGroups(words5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Encoding each word involves separating even and odd indexed characters and sorting them.
  For a word of length `L`, this takes O(L log L).
- If there are `N` words, the total time complexity is O(N * L log L).

Space Complexity:
- The space complexity is dominated by the storage of the set of unique encodings.
  In the worst case, there are `N` unique encodings, each of size proportional to the length of the word `L`.
  Thus, the space complexity is O(N * L).
"""

# Topic: Strings, Hashing