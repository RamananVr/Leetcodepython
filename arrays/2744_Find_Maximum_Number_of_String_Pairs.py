"""
LeetCode Problem #2744: Find Maximum Number of String Pairs

Problem Statement:
You are given a 0-indexed array `words` consisting of distinct strings.

The string pairs are defined as follows:
- A pair `(words[i], words[j])` is a string pair if:
  - `0 <= i < j < words.length`
  - `words[i]` is equal to the reverse of `words[j]`.

Return the maximum number of string pairs that can be formed from the array `words`.

Example:
Input: words = ["cd", "ac", "dc", "ca", "zz"]
Output: 2
Explanation: In this example, we can form two pairs:
- Pair 1: ("cd", "dc") because "dc" is the reverse of "cd".
- Pair 2: ("ac", "ca") because "ca" is the reverse of "ac".

Constraints:
- 1 <= words.length <= 50
- words[i].length == 2
- words consists of distinct strings.
"""

# Solution
def maximumNumberOfStringPairs(words):
    """
    Finds the maximum number of string pairs where one string is the reverse of the other.

    :param words: List[str] - A list of distinct strings.
    :return: int - The maximum number of string pairs.
    """
    reverse_set = set()
    count = 0

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in reverse_set:
            count += 1
        else:
            reverse_set.add(word)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["cd", "ac", "dc", "ca", "zz"]
    print(maximumNumberOfStringPairs(words1))  # Output: 2

    # Test Case 2
    words2 = ["ab", "ba", "cc", "dd", "ee"]
    print(maximumNumberOfStringPairs(words2))  # Output: 1

    # Test Case 3
    words3 = ["xy", "yx", "pq", "qp", "mn"]
    print(maximumNumberOfStringPairs(words3))  # Output: 2

    # Test Case 4
    words4 = ["aa", "bb", "cc", "dd"]
    print(maximumNumberOfStringPairs(words4))  # Output: 0

    # Test Case 5
    words5 = ["ab", "cd", "ef", "gh"]
    print(maximumNumberOfStringPairs(words5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `words` list once, performing constant-time operations for each word.
- Therefore, the time complexity is O(n), where n is the length of the `words` list.

Space Complexity:
- The function uses a set to store the words, which in the worst case can contain all n words.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays