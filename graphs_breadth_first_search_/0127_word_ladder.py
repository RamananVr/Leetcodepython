"""
LeetCode Question #127: Word Ladder

Problem Statement:
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words 
`beginWord -> s1 -> s2 -> ... -> endWord` such that:

1. Every adjacent pair of words differs by a single letter.
2. Every `si` (except `beginWord`) must be in `wordList`. Note that `beginWord` does not need to be in `wordList`.
3. `endWord` must be in `wordList`.

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest 
transformation sequence from `beginWord` to `endWord`, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- `beginWord`, `endWord`, and `wordList[i]` consist of only lowercase English letters.
"""

from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord.
    """
    wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
    if endWord not in wordSet:
        return 0

    # Initialize BFS
    queue = deque([(beginWord, 1)])  # (current_word, current_depth)

    while queue:
        current_word, depth = queue.popleft()

        # Check if we've reached the endWord
        if current_word == endWord:
            return depth

        # Generate all possible transformations
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                transformed_word = current_word[:i] + char + current_word[i+1:]
                if transformed_word in wordSet:
                    wordSet.remove(transformed_word)  # Mark as visited
                    queue.append((transformed_word, depth + 1))

    return 0  # No transformation sequence exists

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladderLength(beginWord, endWord, wordList))  # Output: 5

    # Test Case 2
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(ladderLength(beginWord, endWord, wordList))  # Output: 0

    # Test Case 3
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    print(ladderLength(beginWord, endWord, wordList))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs a Breadth-First Search (BFS) over the word graph.
- For each word, we generate all possible transformations by changing one letter at a time.
- There are `L` positions in the word, and for each position, we can substitute one of 26 letters.
- Thus, the number of transformations for a word is `O(26 * L)`.
- If there are `N` words in the wordList, the total complexity is `O(N * 26 * L)`, which simplifies to `O(N * L)`.

Space Complexity:
- The space complexity is dominated by the `wordSet` and the BFS queue.
- The `wordSet` contains up to `N` words, and the queue can contain up to `N` words in the worst case.
- Thus, the space complexity is `O(N)`.

Topic: Graphs (Breadth-First Search)
"""