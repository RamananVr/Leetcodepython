"""
LeetCode Question #692: Top K Frequent Words

Problem Statement:
Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.
Return the answer sorted by frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny", and "day" are the four most frequent words, with "the" being the most frequent, followed by "is", "sunny", and "day".

Constraints:
- 1 <= words.length <= 500
- 1 <= words[i].length <= 10
- `words[i]` consists of lowercase English letters.
- k is in the range [1, the number of unique words in the input].

Follow-up:
Could you solve it in O(n log k) time complexity?
"""

# Solution
from collections import Counter
import heapq

def topKFrequent(words, k):
    """
    Find the k most frequent words in the given list of words.

    :param words: List[str] - List of words
    :param k: int - Number of top frequent words to return
    :return: List[str] - List of k most frequent words
    """
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Use a heap to store the words by frequency and lexicographical order
    # Python's heapq is a min-heap, so we use negative frequency for max-heap behavior
    heap = [(-freq, word) for word, freq in word_count.items()]
    heapq.heapify(heap)
    
    # Extract the top k elements from the heap
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2
    print(topKFrequent(words1, k1))  # Output: ["i", "love"]

    # Test Case 2
    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k2 = 4
    print(topKFrequent(words2, k2))  # Output: ["the", "is", "sunny", "day"]

    # Test Case 3
    words3 = ["a", "b", "c", "a", "b", "a"]
    k3 = 1
    print(topKFrequent(words3, k3))  # Output: ["a"]

    # Test Case 4
    words4 = ["apple", "banana", "apple", "orange", "banana", "apple"]
    k4 = 2
    print(topKFrequent(words4, k4))  # Output: ["apple", "banana"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of words using Counter takes O(n), where n is the length of the input list `words`.
- Creating the heap takes O(m log m), where m is the number of unique words.
- Extracting the top k elements from the heap takes O(k log m).
Overall, the time complexity is O(n + m log m + k log m), which simplifies to O(n + m log m) since k <= m.

Space Complexity:
- The Counter object takes O(m) space to store the frequency of each unique word.
- The heap takes O(m) space to store the unique words and their frequencies.
Overall, the space complexity is O(m).
"""

# Topic: Heap, Hash Table