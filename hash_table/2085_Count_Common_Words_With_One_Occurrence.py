"""
LeetCode Problem #2085: Count Common Words With One Occurrence

Problem Statement:
Given two string arrays `words1` and `words2`, return the number of strings that appear exactly once in each of the two arrays.

Example 1:
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays.
- "amazing" appears exactly once in each of the two arrays.
- "is" appears in both arrays but more than once in words1.
- "as" appears only in words1.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

Example 2:
Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation:
There are no strings that appear exactly once in each of the two arrays.

Example 3:
Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation:
- "ab" appears exactly once in each of the two arrays.
- "a" appears more than once in words2.
Thus, there is 1 string that appears exactly once in each of the two arrays.

Constraints:
- 1 <= words1.length, words2.length <= 1000
- 1 <= words1[i].length, words2[j].length <= 30
- words1[i] and words2[j] consist of lowercase English letters.
"""

# Python Solution
from collections import Counter

def countWords(words1, words2):
    """
    Count the number of strings that appear exactly once in both words1 and words2.

    :param words1: List[str] - First list of words
    :param words2: List[str] - Second list of words
    :return: int - Number of strings that appear exactly once in both lists
    """
    # Count occurrences of each word in both lists
    count1 = Counter(words1)
    count2 = Counter(words2)
    
    # Find words that appear exactly once in both lists
    return sum(1 for word in count1 if count1[word] == 1 and count2.get(word, 0) == 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["leetcode", "is", "amazing", "as", "is"]
    words2 = ["amazing", "leetcode", "is"]
    print(countWords(words1, words2))  # Output: 2

    # Test Case 2
    words1 = ["b", "bb", "bbb"]
    words2 = ["a", "aa", "aaa"]
    print(countWords(words1, words2))  # Output: 0

    # Test Case 3
    words1 = ["a", "ab"]
    words2 = ["a", "a", "a", "ab"]
    print(countWords(words1, words2))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting occurrences in `words1` and `words2` takes O(n1 + n2), where n1 and n2 are the lengths of `words1` and `words2`.
- Iterating through the keys of `count1` takes O(k1), where k1 is the number of unique words in `words1`.
- Overall, the time complexity is O(n1 + n2 + k1).

Space Complexity:
- The space complexity is O(k1 + k2), where k1 and k2 are the number of unique words in `words1` and `words2`, respectively.
- This is due to the storage of the `Counter` objects for both lists.
"""

# Topic: Hash Table