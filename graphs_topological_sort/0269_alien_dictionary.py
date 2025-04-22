"""
LeetCode Question #269: Alien Dictionary

Problem Statement:
There is a new alien language that uses the English alphabet. However, the order among letters is unknown to you. 
You are given a list of strings `words` from the alien language, sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

If the given words are invalid (i.e., they cannot possibly follow the rules of the alien language), return an empty string.
If there are multiple valid orderings, return any of them.
The input is guaranteed to be non-empty.

Example 1:
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Example 2:
Input: words = ["z", "x"]
Output: "zx"

Example 3:
Input: words = ["z", "x", "z"]
Output: ""

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- `words[i]` consists of only lowercase English letters.

"""

from collections import defaultdict, deque

def alienOrder(words):
    """
    Derives the order of letters in the alien language based on the given lexicographically sorted words.

    :param words: List[str] - List of words sorted lexicographically in the alien language.
    :return: str - A string representing the order of letters in the alien language, or an empty string if invalid.
    """
    # Step 1: Build the graph
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_length = min(len(word1), len(word2))
        
        # Check for invalid case: prefix conflict
        if word1[:min_length] == word2[:min_length] and len(word1) > len(word2):
            return ""

        for j in range(min_length):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break

    # Step 2: Topological Sort using Kahn's Algorithm
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the order contains all characters, return it; otherwise, return an empty string
    if len(order) == len(in_degree):
        return "".join(order)
    return ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    print(alienOrder(words1))  # Output: "wertf"

    # Test Case 2
    words2 = ["z", "x"]
    print(alienOrder(words2))  # Output: "zx"

    # Test Case 3
    words3 = ["z", "x", "z"]
    print(alienOrder(words3))  # Output: ""

    # Test Case 4
    words4 = ["abc", "ab"]
    print(alienOrder(words4))  # Output: "" (Invalid case due to prefix conflict)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph: O(C), where C is the total number of characters across all words.
- Topological sort: O(V + E), where V is the number of unique characters and E is the number of edges in the graph.
- Overall: O(C + V + E). Since V and E are bounded by C, the complexity simplifies to O(C).

Space Complexity:
- Graph storage: O(V + E), where V is the number of unique characters and E is the number of edges.
- In-degree dictionary: O(V).
- Queue and order list: O(V).
- Overall: O(V + E), which is bounded by O(C).

Topic: Graphs, Topological Sort
"""