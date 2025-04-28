"""
LeetCode Problem #1032: Stream of Characters

Problem Statement:
Design an algorithm that accepts a stream of characters and checks if a suffix of these characters matches any string in a given list of words.

Implement the StreamChecker class:
- StreamChecker(words): Initializes the object with the strings array words.
- query(letter): Returns true if any suffix of the stream matches a word in words, otherwise returns false.

Example:
Input:
["StreamChecker", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"]]
Output:
[null, false, false, false, true, false, true]

Explanation:
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the word list
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the word list

Constraints:
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 2000
- words[i] consists of lowercase English letters.
- letter is a lowercase English letter.
- At most 4 * 10^4 calls will be made to query.
"""

from collections import deque

class StreamChecker:
    def __init__(self, words):
        """
        Initialize the StreamChecker with a list of words.
        Use a Trie data structure to efficiently check suffix matches.
        """
        self.trie = {}
        self.stream = deque()
        
        # Build the Trie in reverse order of the words
        for word in words:
            node = self.trie
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True  # Mark the end of a word

    def query(self, letter):
        """
        Add the letter to the stream and check if any suffix matches a word in the Trie.
        """
        self.stream.appendleft(letter)  # Add the letter to the front of the stream
        node = self.trie
        
        for char in self.stream:
            if char in node:
                node = node[char]
                if '#' in node:  # Found a word
                    return True
            else:
                break
        
        return False


# Example Test Cases
if __name__ == "__main__":
    # Initialize StreamChecker with a list of words
    streamChecker = StreamChecker(["cd", "f", "kl"])
    
    # Test queries
    print(streamChecker.query("a"))  # Output: False
    print(streamChecker.query("b"))  # Output: False
    print(streamChecker.query("c"))  # Output: False
    print(streamChecker.query("d"))  # Output: True
    print(streamChecker.query("e"))  # Output: False
    print(streamChecker.query("f"))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- Initialization (__init__): Building the Trie takes O(sum(len(word) for word in words)), where len(word) is the length of each word in the list.
- Query (query): Each query checks the stream against the Trie. In the worst case, we traverse the Trie up to the length of the longest word, so the time complexity per query is O(L), where L is the length of the longest word.

Space Complexity:
- Trie: The Trie uses O(sum(len(word) for word in words)) space to store all the words.
- Stream: The stream stores up to L characters, where L is the length of the longest word. Thus, the space complexity for the stream is O(L).

Overall Space Complexity: O(sum(len(word) for word in words) + L)

Topic: Trie
"""