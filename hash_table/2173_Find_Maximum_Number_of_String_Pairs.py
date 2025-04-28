"""
LeetCode Problem #2173: Find Maximum Number of String Pairs

Problem Statement:
You are given an array of strings `words`. Each string in `words` consists of lowercase English letters only.

A pair of strings `(words[i], words[j])` is called a "string pair" if:
1. `0 <= i < j < len(words)`, and
2. The string `words[i]` is equal to the reverse of the string `words[j]`.

Return the maximum number of string pairs that can be formed from the array `words`.

Example 1:
Input: words = ["cd", "ac", "dc", "ca", "zz"]
Output: 2
Explanation: In this example, we can form 2 string pairs:
- Pair 1: (words[0], words[2]) -> "cd" and "dc"
- Pair 2: (words[1], words[3]) -> "ac" and "ca"

Example 2:
Input: words = ["ab", "ba", "cc"]
Output: 1
Explanation: In this example, we can form 1 string pair:
- Pair 1: (words[0], words[1]) -> "ab" and "ba"

Example 3:
Input: words = ["aa", "ab", "bb", "ba"]
Output: 1
Explanation: In this example, we can form 1 string pair:
- Pair 1: (words[1], words[3]) -> "ab" and "ba"

Constraints:
- 1 <= words.length <= 10^5
- words[i].length == 2
- words[i] consists of lowercase English letters.
"""

def maximumNumberOfStringPairs(words):
    """
    Function to find the maximum number of string pairs in the given list of words.

    :param words: List[str] - List of strings where each string has a length of 2.
    :return: int - Maximum number of string pairs.
    """
    reverse_count = {}
    pairs = 0

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in reverse_count and reverse_count[reversed_word] > 0:
            pairs += 1
            reverse_count[reversed_word] -= 1
        else:
            reverse_count[word] = reverse_count.get(word, 0) + 1

    return pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["cd", "ac", "dc", "ca", "zz"]
    print(maximumNumberOfStringPairs(words1))  # Output: 2

    # Test Case 2
    words2 = ["ab", "ba", "cc"]
    print(maximumNumberOfStringPairs(words2))  # Output: 1

    # Test Case 3
    words3 = ["aa", "ab", "bb", "ba"]
    print(maximumNumberOfStringPairs(words3))  # Output: 1

    # Test Case 4
    words4 = ["ab", "ba", "ab", "ba"]
    print(maximumNumberOfStringPairs(words4))  # Output: 2

    # Test Case 5
    words5 = ["xy", "yx", "xy", "yx", "zz", "zz"]
    print(maximumNumberOfStringPairs(words5))  # Output: 3

"""
Time Complexity Analysis:
- Iterating through the `words` list takes O(n), where n is the length of the list.
- Dictionary operations (insertion, lookup, and update) are O(1) on average.
- Thus, the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique strings in the `words` list.
- In the worst case, all strings in `words` are unique, so the space complexity is O(n).

Topic: Hash Table
"""