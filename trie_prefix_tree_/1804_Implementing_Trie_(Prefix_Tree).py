"""
LeetCode Problem #1804: Implementing Trie (Prefix Tree)

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are two main operations in a trie:

1. insert: Inserts a string into the trie.
2. countWordsEqualTo: Returns the number of instances of a string in the trie.
3. countWordsStartingWith: Returns the number of strings in the trie that start with a given prefix.
4. erase: Removes a string from the trie.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
- int countWordsStartingWith(String prefix) Returns the number of strings in the trie that start with the prefix.
- void erase(String word) Removes the string word from the trie. It is guaranteed that word exists in the trie.

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        stack = []
        for char in word:
            stack.append((node, char))
            node = node.children[char]
            node.prefix_count -= 1
        node.word_count -= 1

        # Clean up nodes with no remaining prefixes or words
        while stack:
            parent, char = stack.pop()
            child = parent.children[char]
            if child.word_count == 0 and child.prefix_count == 0:
                del parent.children[char]
            else:
                break

# Example Test Cases
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    trie.insert("app")
    print(trie.countWordsEqualTo("apple"))  # Output: 2
    print(trie.countWordsStartingWith("app"))  # Output: 3
    trie.erase("apple")
    print(trie.countWordsEqualTo("apple"))  # Output: 1
    print(trie.countWordsStartingWith("app"))  # Output: 2

"""
Time and Space Complexity Analysis:

1. insert(word):
   - Time Complexity: O(L), where L is the length of the word.
   - Space Complexity: O(L), for storing new nodes in the trie.

2. countWordsEqualTo(word):
   - Time Complexity: O(L), where L is the length of the word.
   - Space Complexity: O(1), as no additional space is used.

3. countWordsStartingWith(prefix):
   - Time Complexity: O(P), where P is the length of the prefix.
   - Space Complexity: O(1), as no additional space is used.

4. erase(word):
   - Time Complexity: O(L), where L is the length of the word.
   - Space Complexity: O(1), as no additional space is used.

Overall Space Complexity:
The space complexity of the Trie depends on the total number of unique characters stored across all words. In the worst case, it is proportional to the sum of the lengths of all inserted words.

Topic: Trie (Prefix Tree)
"""