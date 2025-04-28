"""
LeetCode Problem #734: Sentence Similarity

Problem Statement:
We are given two sentences `sentence1` and `sentence2` each represented as a list of strings. 
A word `a` in sentence1 is similar to a word `b` in sentence2 if:
- `a == b`, or
- `(a, b)` or `(b, a)` is in the list of similar word pairs `similarPairs`.

Return true if `sentence1` and `sentence2` are similar, otherwise return false.

Two sentences are similar if:
- They have the same length, and
- Each corresponding pair of words between the two sentences is similar.

Example 1:
Input: sentence1 = ["great", "acting", "skills"], 
       sentence2 = ["fine", "drama", "talent"], 
       similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
Output: true

Example 2:
Input: sentence1 = ["great"], 
       sentence2 = ["great"], 
       similarPairs = []
Output: true

Example 3:
Input: sentence1 = ["great"], 
       sentence2 = ["doubleplus", "good"], 
       similarPairs = [["great", "good"]]
Output: false

Constraints:
- The length of sentence1 and sentence2 will not exceed 1000.
- The length of similarPairs will not exceed 2000.
- The length of each word in the sentences and the similarPairs will not exceed 20.
"""

def areSentencesSimilar(sentence1, sentence2, similarPairs):
    """
    Determines if two sentences are similar based on the given similar word pairs.

    :param sentence1: List[str] - First sentence as a list of words.
    :param sentence2: List[str] - Second sentence as a list of words.
    :param similarPairs: List[List[str]] - List of similar word pairs.
    :return: bool - True if the sentences are similar, False otherwise.
    """
    if len(sentence1) != len(sentence2):
        return False

    # Create a set for quick lookup of similar pairs
    similar_set = set()
    for pair in similarPairs:
        similar_set.add((pair[0], pair[1]))
        similar_set.add((pair[1], pair[0]))

    # Check each pair of words in the sentences
    for word1, word2 in zip(sentence1, sentence2):
        if word1 != word2 and (word1, word2) not in similar_set:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

    # Test Case 2
    sentence1 = ["great"]
    sentence2 = ["great"]
    similarPairs = []
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

    # Test Case 3
    sentence1 = ["great"]
    sentence2 = ["doubleplus", "good"]
    similarPairs = [["great", "good"]]
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: False

    # Test Case 4
    sentence1 = ["great", "skills"]
    sentence2 = ["fine", "talent"]
    similarPairs = [["great", "fine"], ["skills", "talent"]]
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: True

    # Test Case 5
    sentence1 = ["great", "skills"]
    sentence2 = ["fine", "talent"]
    similarPairs = [["great", "fine"]]
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the `similar_set` takes O(len(similarPairs)).
- Comparing the sentences takes O(len(sentence1)) since we iterate through the words in the sentences.
- Overall time complexity: O(len(similarPairs) + len(sentence1)).

Space Complexity:
- The `similar_set` uses O(len(similarPairs)) space to store the pairs.
- Overall space complexity: O(len(similarPairs)).

Topic: Hash Table
"""