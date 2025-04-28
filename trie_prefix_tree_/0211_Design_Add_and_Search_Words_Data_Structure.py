"""
LeetCode Problem #211: Design Add and Search Words Data Structure

Problem Statement:
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure. It can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

Example:
    Input:
    ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
    [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    Output:
    [null, null, null, null, false, true, true, true]

Constraints:
- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consists of `'.'` or lowercase English letters.
- There will be at most `3 * 10^4` calls in total to `addWord` and `search`.
"""

# Solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end_of_word

            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)

# Example Test Cases
if __name__ == "__main__":
    # Initialize WordDictionary
    word_dict = WordDictionary()

    # Add words
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")

    # Search for words
    print(word_dict.search("pad"))  # Output: False
    print(word_dict.search("bad"))  # Output: True
    print(word_dict.search(".ad"))  # Output: True
    print(word_dict.search("b.."))  # Output: True

"""
Time Complexity:
- `addWord`: O(L), where L is the length of the word being added. Each character is processed once.
- `search`: O(N * 26^M), where N is the length of the word being searched, and M is the number of '.' characters in the word. In the worst case, each '.' can branch into 26 possibilities.

Space Complexity:
- The space complexity is O(T), where T is the total number of characters in all added words. Each character is stored in a TrieNode.

Topic: Trie (Prefix Tree)
"""