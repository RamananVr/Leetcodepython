"""
LeetCode Question #2010: Count Groups of Special-Equivalent Strings

Problem Statement:
You are given an array of strings `words`. A string `s` is called special-equivalent if it can be transformed into another string `t` by swapping characters at even indices with other characters at even indices, and swapping characters at odd indices with other characters at odd indices.

Two strings `s` and `t` are special-equivalent if they belong to the same group. A group is defined as a set of strings that are special-equivalent to each other.

Return the number of groups of special-equivalent strings in the array `words`.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 20
- words[i] consist of lowercase English letters.

Example:
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation:
- "abcd", "cdab", "cbad" are in the same group.
- "xyzz", "zzxy" are in the same group.
- "zzyx" is in its own group.

"""

# Solution
def numSpecialEquivGroups(words):
    """
    Count the number of groups of special-equivalent strings.

    :param words: List[str] - List of input strings
    :return: int - Number of special-equivalent groups
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
    words3 = ["a", "b", "c", "a", "c", "b"]
    print(numSpecialEquivGroups(words3))  # Output: 3

    # Test Case 4
    words4 = ["aa", "bb", "ab", "ba"]
    print(numSpecialEquivGroups(words4))  # Output: 4

    # Test Case 5
    words5 = ["abcd", "abcd", "abcd"]
    print(numSpecialEquivGroups(words5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Encoding each word involves sorting the even and odd indexed characters.
- Sorting takes O(k log k), where k is the length of the word (maximum 20).
- For n words, the total time complexity is O(n * k log k), where n is the number of words.

Space Complexity:
- The space complexity is O(n * k) for storing the unique encodings in the set, where n is the number of words and k is the maximum length of a word.
- Additionally, temporary space is used for sorting, which is O(k) per word.

Overall:
Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

# Topic: Strings, Hashing