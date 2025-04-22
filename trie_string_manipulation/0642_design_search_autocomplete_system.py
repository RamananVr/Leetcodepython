"""
LeetCode Question #642: Design Search Autocomplete System

Problem Statement:
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word) and the system returns the top 3 historical sentences that start with the same prefix as the input sentence. Here are the specific requirements:

1. The system has a history of sentences and their corresponding times they have been typed.
2. The sentences are sorted by their frequency (descending order). If two sentences have the same frequency, they are sorted lexicographically (ascending order).
3. When the user types a character, the system returns the top 3 sentences that match the current prefix.
4. If there are fewer than 3 matches, return all matches.
5. If no matches exist, return an empty list.
6. The system should allow the user to add new sentences to the history.

Implement the `AutocompleteSystem` class:
- `AutocompleteSystem(String[] sentences, int[] times)` Initializes the object with the sentences and their corresponding times.
- `List<String> input(char c)` This method is called when the user types a character. Returns the top 3 historical sentences that match the current prefix. If `c == '#'`, the user finishes typing the current sentence and it should be added to the history.

Constraints:
- The length of `sentences` and `times` will not exceed 1000.
- The length of each sentence will not exceed 100.
- The total number of characters typed will not exceed 5000.
- Times will be in the range [1, 1000].
- Each sentence will have at least one word.

"""

from collections import defaultdict
import heapq

class AutocompleteSystem:
    def __init__(self, sentences, times):
        """
        Initializes the AutocompleteSystem with historical sentences and their frequencies.
        """
        self.trie = defaultdict(dict)  # Trie structure to store sentences and their frequencies
        self.history = defaultdict(int)  # Dictionary to store sentence frequencies
        self.current_prefix = ""  # Current prefix being typed by the user

        # Populate the trie and history with the given sentences and times
        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence, time):
        """
        Adds a sentence to the history and trie with the given frequency.
        """
        self.history[sentence] += time
        node = self.trie
        for char in sentence:
            if char not in node:
                node[char] = defaultdict(dict)
            node = node[char]
        node["#"] = sentence  # Mark the end of the sentence

    def search(self, prefix):
        """
        Searches for all sentences that match the given prefix.
        """
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]

        # Perform DFS to collect all sentences under the current prefix
        results = []

        def dfs(node):
            for key, value in node.items():
                if key == "#":
                    results.append(value)
                else:
                    dfs(value)

        dfs(node)
        return results

    def input(self, c):
        """
        Handles user input character by character.
        """
        if c == "#":
            # Add the current prefix to the history and reset the prefix
            self.add_sentence(self.current_prefix, 1)
            self.current_prefix = ""
            return []

        self.current_prefix += c
        matched_sentences = self.search(self.current_prefix)

        # Sort sentences by frequency (descending) and lexicographically (ascending)
        matched_sentences.sort(key=lambda x: (-self.history[x], x))
        return matched_sentences[:3]


# Example Test Cases
if __name__ == "__main__":
    # Initialize the autocomplete system
    sentences = ["i love you", "island", "ironman", "i love leetcode"]
    times = [5, 3, 2, 2]
    autocompleteSystem = AutocompleteSystem(sentences, times)

    # Test case 1: Typing 'i'
    print(autocompleteSystem.input('i'))  # Output: ["i love you", "i love leetcode", "island"]

    # Test case 2: Typing ' '
    print(autocompleteSystem.input(' '))  # Output: ["i love you", "i love leetcode"]

    # Test case 3: Typing 'a'
    print(autocompleteSystem.input('a'))  # Output: []

    # Test case 4: Typing '#'
    print(autocompleteSystem.input('#'))  # Output: []

    # Test case 5: Typing 'i' again
    print(autocompleteSystem.input('i'))  # Output: ["i love you", "i love leetcode", "island"]

"""
Time and Space Complexity Analysis:

1. `add_sentence`:
   - Time Complexity: O(L), where L is the length of the sentence being added.
   - Space Complexity: O(L), for storing the sentence in the trie.

2. `search`:
   - Time Complexity: O(P + S), where P is the length of the prefix and S is the number of sentences matching the prefix.
   - Space Complexity: O(S), for storing the matching sentences.

3. `input`:
   - Time Complexity: O(P + S log S), where P is the length of the prefix and S is the number of matching sentences (due to sorting).
   - Space Complexity: O(S), for storing the matching sentences.

Overall:
- Time Complexity: O(P + S log S) per input character.
- Space Complexity: O(N * L), where N is the number of sentences and L is the average length of a sentence.

Topic: Trie, String Manipulation
"""