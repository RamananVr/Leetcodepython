"""
LeetCode Problem #2255: Count Prefixes of a Given String

Problem Statement:
You are given a string array `words` and a string `s`. A string `word` is a prefix of `s` if `s` starts with `word`.

- For example, "a" is a prefix of "abc", and "abc" is a prefix of "abc", but "bc" is not a prefix of "abc".

Return the number of strings in `words` that are a prefix of `s`.

Constraints:
1. 1 <= words.length <= 1000
2. 1 <= words[i].length, s.length <= 100
3. words[i] and s consist of only lowercase English letters.
"""

def countPrefixes(words, s):
    """
    Function to count the number of strings in `words` that are prefixes of `s`.

    :param words: List[str] - List of words to check as prefixes.
    :param s: str - The target string.
    :return: int - The count of words that are prefixes of `s`.
    """
    count = 0
    for word in words:
        if s.startswith(word):
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["a", "b", "c", "ab", "bc", "abc"]
    s1 = "abc"
    print(countPrefixes(words1, s1))  # Output: 3

    # Test Case 2
    words2 = ["a", "ab", "abc", "abcd"]
    s2 = "abcde"
    print(countPrefixes(words2, s2))  # Output: 3

    # Test Case 3
    words3 = ["x", "y", "z"]
    s3 = "abc"
    print(countPrefixes(words3, s3))  # Output: 0

    # Test Case 4
    words4 = ["apple", "app", "ap", "a"]
    s4 = "applepie"
    print(countPrefixes(words4, s4))  # Output: 4

    # Test Case 5
    words5 = ["hello", "he", "h", "world"]
    s5 = "hello"
    print(countPrefixes(words5, s5))  # Output: 3

"""
Time Complexity Analysis:
- Let `n` be the number of words in the `words` list.
- Let `m` be the average length of the words in `words`.
- Let `k` be the length of the string `s`.

The `startswith` method checks if a string starts with a given prefix, which takes O(m) time in the worst case.
We iterate through all `n` words in the `words` list, so the total time complexity is O(n * m).

Space Complexity Analysis:
- The space complexity is O(1) as we are not using any additional data structures that scale with the input size.

Topic: Strings
"""