"""
LeetCode Question #208: Implement Trie (Prefix Tree)

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize the Trie object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie, and false otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is any word in the trie that starts with the given prefix, and false otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example Test Cases
if __name__ == "__main__":
    trie = Trie()
    
    # Test case 1: Insert and search
    trie.insert("apple")
    assert trie.search("apple") == True  # "apple" is in the trie
    assert trie.search("app") == False  # "app" is not in the trie
    assert trie.startsWith("app") == True  # "app" is a prefix of "apple"
    
    # Test case 2: Insert and check prefix
    trie.insert("app")
    assert trie.search("app") == True  # "app" is now in the trie
    
    # Test case 3: Check non-existent word
    assert trie.search("banana") == False  # "banana" is not in the trie
    assert trie.startsWith("ban") == False  # No word starts with "ban"
    
    print("All test cases passed!")

"""
Time Complexity:
- insert(word): O(m), where m is the length of the word. Each character is processed once.
- search(word): O(m), where m is the length of the word. Each character is checked once.
- startsWith(prefix): O(p), where p is the length of the prefix. Each character is checked once.

Space Complexity:
- The space complexity is O(N * M), where N is the number of words inserted into the trie, and M is the average length of the words. 
  This accounts for the storage of all characters in the trie.

Topic: Trie (Prefix Tree)
"""