"""
LeetCode Problem #737: Sentence Similarity II

Problem Statement:
We are given two sentences, `sentence1` and `sentence2`, each represented as a list of strings. 
A word in one sentence is similar to a word in the other sentence if:
- They are the same string, or
- There is a direct or indirect chain of similarity relationships connecting them.

Given a list of pairs of similar words `similarPairs` where each pair `[word1, word2]` indicates that `word1` and `word2` are similar, 
return `True` if `sentence1` and `sentence2` are similar, or `False` otherwise.

Two sentences are similar if:
1. They have the same length.
2. Each word in one sentence is similar to the corresponding word in the other sentence.

Constraints:
- `1 <= len(sentence1), len(sentence2) <= 1000`
- `1 <= len(similarPairs) <= 2000`
- `1 <= len(word1), len(word2) <= 20`
- `sentence1[i]`, `sentence2[i]`, `word1`, and `word2` consist of lowercase English letters.

"""

from collections import defaultdict, deque

def areSentencesSimilarTwo(sentence1, sentence2, similarPairs):
    """
    Determines if two sentences are similar based on the given similar word pairs.

    :param sentence1: List[str] - The first sentence as a list of words.
    :param sentence2: List[str] - The second sentence as a list of words.
    :param similarPairs: List[List[str]] - List of pairs of similar words.
    :return: bool - True if the sentences are similar, False otherwise.
    """
    if len(sentence1) != len(sentence2):
        return False

    # Build a graph where each word is a node and edges represent similarity
    graph = defaultdict(list)
    for word1, word2 in similarPairs:
        graph[word1].append(word2)
        graph[word2].append(word1)

    # Helper function to perform BFS to check if two words are connected
    def are_words_similar(word1, word2):
        if word1 == word2:
            return True
        visited = set()
        queue = deque([word1])
        while queue:
            current = queue.popleft()
            if current == word2:
                return True
            if current not in visited:
                visited.add(current)
                queue.extend(graph[current])
        return False

    # Check each pair of words in the sentences
    for w1, w2 in zip(sentence1, sentence2):
        if not are_words_similar(w1, w2):
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]
    print(areSentencesSimilarTwo(sentence1, sentence2, similarPairs))  # Output: True

    # Test Case 2
    sentence1 = ["great"]
    sentence2 = ["great"]
    similarPairs = []
    print(areSentencesSimilarTwo(sentence1, sentence2, similarPairs))  # Output: True

    # Test Case 3
    sentence1 = ["great"]
    sentence2 = ["fine"]
    similarPairs = [["great", "good"], ["fine", "good"]]
    print(areSentencesSimilarTwo(sentence1, sentence2, similarPairs))  # Output: True

    # Test Case 4
    sentence1 = ["great", "skills"]
    sentence2 = ["fine", "talent"]
    similarPairs = [["great", "good"], ["fine", "good"]]
    print(areSentencesSimilarTwo(sentence1, sentence2, similarPairs))  # Output: False

"""
Time Complexity Analysis:
- Building the graph takes O(E), where E is the number of similarPairs.
- For each word pair in the sentences, we perform a BFS. In the worst case, BFS visits all nodes and edges, 
  which takes O(V + E), where V is the number of unique words in the graph.
- Let N be the length of the sentences. The total time complexity is O(N * (V + E)).

Space Complexity Analysis:
- The graph uses O(V + E) space.
- The BFS uses O(V) space for the visited set and queue.
- Overall space complexity is O(V + E).

Topic: Graph
"""