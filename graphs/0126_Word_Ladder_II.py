"""
LeetCode Problem #126: Word Ladder II

Problem Statement:
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words 
`beginWord -> s1 -> s2 -> ... -> sk` such that:
1. Every adjacent pair of words differs by a single letter.
2. Every `si` (for 1 <= i <= k) is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
3. `sk == endWord`.

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return all the shortest transformation sequences 
from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of 
the words `[beginWord, s1, s2, ..., sk]`.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord` != `endWord`
- All the words in `wordList` are unique.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []

Topic: Graphs
"""

from collections import defaultdict, deque
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    # Step 1: Build the graph using BFS
    layer = {}
    layer[beginWord] = [[beginWord]]
    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == endWord:
                return layer[word]
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]
        wordSet -= set(new_layer.keys())
        layer = new_layer

    return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(findLadders(beginWord1, endWord1, wordList1))
    # Expected Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

    # Test Case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print(findLadders(beginWord2, endWord2, wordList2))
    # Expected Output: []

    # Test Case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    print(findLadders(beginWord3, endWord3, wordList3))
    # Expected Output: [["a", "c"]]

"""
Time Complexity:
- Let N be the length of each word and M be the size of the wordList.
- Generating all possible transformations for a word takes O(26 * N) = O(N) time.
- BFS explores each word in the wordList at most once, so the total time complexity is O(M * N).

Space Complexity:
- The space complexity is O(M * N) due to the storage of the graph and the layers in BFS.

Topic: Graphs
"""