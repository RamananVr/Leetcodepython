"""
LeetCode Problem #1897: Redistribute Characters to Make All Strings Equal

Problem Statement:
You are given an array of strings `words` (0-indexed). In one operation, you can take any character from any string in `words` and move it to any position in any other string in `words`.

Return `true` if you can make every string in `words` equal using any number of operations, and `false` otherwise.

Example 1:
Input: words = ["abc", "aabc", "bc"]
Output: true
Explanation: Move one 'a' from "aabc" to "bc" to make all strings equal.

Example 2:
Input: words = ["ab", "a"]
Output: false
Explanation: It is impossible to make all strings equal.

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.
"""

# Solution
def makeEqual(words):
    """
    Determines if it is possible to redistribute characters to make all strings in the array equal.

    :param words: List[str] - List of strings
    :return: bool - True if redistribution is possible, False otherwise
    """
    from collections import Counter

    # Count the frequency of all characters across all strings
    total_count = Counter()
    for word in words:
        total_count.update(word)

    # Check if each character's frequency is divisible by the number of words
    num_words = len(words)
    for char, count in total_count.items():
        if count % num_words != 0:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abc", "aabc", "bc"]
    print(makeEqual(words1))  # Output: True

    # Test Case 2
    words2 = ["ab", "a"]
    print(makeEqual(words2))  # Output: False

    # Test Case 3
    words3 = ["aaa", "aaa", "aaa"]
    print(makeEqual(words3))  # Output: True

    # Test Case 4
    words4 = ["a", "b", "c"]
    print(makeEqual(words4))  # Output: False

    # Test Case 5
    words5 = ["abc", "abc", "abc"]
    print(makeEqual(words5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters across all strings takes O(n * m), 
  where `n` is the number of strings and `m` is the average length of the strings.
- Checking divisibility for each character takes O(k), where `k` is the number of unique characters.
- Overall time complexity: O(n * m + k).

Space Complexity:
- The `Counter` object stores the frequency of all characters, which requires O(k) space, 
  where `k` is the number of unique characters.
- Overall space complexity: O(k).

Topic: Strings
"""