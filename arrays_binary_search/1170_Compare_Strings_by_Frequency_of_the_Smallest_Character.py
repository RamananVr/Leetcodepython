"""
LeetCode Problem #1170: Compare Strings by Frequency of the Smallest Character

Problem Statement:
Let the function `f(s)` be defined as the frequency of the smallest character in a string `s`. 
For example, if `s = "dcce"`, then `f(s) = 2` because the smallest character is `'c'` and it appears 2 times.

Given two string arrays `queries` and `words`, return an integer array `answer`, where each `answer[i]` is the number of words such that `f(queries[i]) < f(w)` for each word `w` in `words`.

Example:
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: 
f("cbd") = 1 because the smallest character is 'b' and it appears once.
f("zaaaz") = 3 because the smallest character is 'a' and it appears three times.
Since 1 < 3, there is 1 word in `words` that satisfies this condition.

Constraints:
- 1 <= queries.length <= 2000
- 1 <= words.length <= 2000
- 1 <= queries[i].length, words[i].length <= 10
- queries[i][j], words[i][j] are English lowercase letters.
"""

from typing import List

def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
    def f(s: str) -> int:
        """Helper function to calculate the frequency of the smallest character in a string."""
        return s.count(min(s))
    
    # Calculate f(w) for all words and sort them
    word_frequencies = sorted(f(word) for word in words)
    
    def count_greater(freq: int) -> int:
        """Helper function to count how many elements in word_frequencies are greater than freq."""
        # Use binary search to find the first index where word_frequencies[index] > freq
        left, right = 0, len(word_frequencies)
        while left < right:
            mid = (left + right) // 2
            if word_frequencies[mid] > freq:
                right = mid
            else:
                left = mid + 1
        return len(word_frequencies) - left
    
    # Calculate the result for each query
    return [count_greater(f(query)) for query in queries]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    queries = ["cbd"]
    words = ["zaaaz"]
    print(numSmallerByFrequency(queries, words))  # Output: [1]

    # Test Case 2
    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]
    print(numSmallerByFrequency(queries, words))  # Output: [1, 2]

    # Test Case 3
    queries = ["a", "b", "c"]
    words = ["aaa", "bbb", "ccc"]
    print(numSmallerByFrequency(queries, words))  # Output: [3, 3, 3]

    # Test Case 4
    queries = ["xyz", "abc"]
    words = ["a", "aa", "aaa"]
    print(numSmallerByFrequency(queries, words))  # Output: [0, 3]

"""
Time Complexity:
- Calculating f(s) for each word in `words` takes O(n * m), where n = len(words) and m is the average length of a word.
- Sorting `word_frequencies` takes O(n log n).
- For each query, calculating f(query) takes O(m), and performing binary search on `word_frequencies` takes O(log n).
- Total complexity: O(n * m + n log n + q * (m + log n)), where q = len(queries).

Space Complexity:
- The space complexity is O(n) for storing `word_frequencies`.

Topic: Arrays, Binary Search
"""