"""
LeetCode Question #745: Prefix and Suffix Search

Problem Statement:
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the `WordFilter` class:
- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
- `int f(string prefix, string suffix)` Returns the index of the word in the dictionary which has the prefix `prefix` and the suffix `suffix`. 
  If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Example:
Input:
["WordFilter", "f", "f"]
[[["apple"]], ["a", "e"], ["b", ""]]
Output:
[null, 0, -1]

Explanation:
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
wordFilter.f("b", ""); // return -1, because there is no word that has prefix = "b" and suffix = "".

Constraints:
- 1 <= words.length <= 15000
- 1 <= words[i].length <= 10
- 1 <= prefix.length, suffix.length <= 10
- words[i], prefix and suffix consist of lowercase English letters only.
- At most 15000 calls will be made to the function.
"""

# Solution
class WordFilter:
    def __init__(self, words: list[str]):
        # Store a mapping of (prefix, suffix) -> index
        self.prefix_suffix_map = {}
        for index, word in enumerate(words):
            n = len(word)
            # Generate all possible prefix and suffix combinations
            for i in range(n + 1):  # Prefixes
                for j in range(n + 1):  # Suffixes
                    prefix = word[:i]
                    suffix = word[j:]
                    self.prefix_suffix_map[(prefix, suffix)] = index

    def f(self, prefix: str, suffix: str) -> int:
        # Return the index for the given prefix and suffix, or -1 if not found
        return self.prefix_suffix_map.get((prefix, suffix), -1)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the WordFilter object
    wordFilter = WordFilter(["apple", "banana", "grape", "apricot", "orange"])

    # Test cases
    print(wordFilter.f("a", "e"))  # Output: 0 (word "apple" at index 0)
    print(wordFilter.f("b", "a"))  # Output: 1 (word "banana" at index 1)
    print(wordFilter.f("g", "e"))  # Output: 2 (word "grape" at index 2)
    print(wordFilter.f("ap", "ot"))  # Output: 3 (word "apricot" at index 3)
    print(wordFilter.f("o", "e"))  # Output: 4 (word "orange" at index 4)
    print(wordFilter.f("x", "y"))  # Output: -1 (no matching word)

# Time and Space Complexity Analysis
"""
Time Complexity:
- Initialization (__init__): O(N * L^2), where N is the number of words and L is the maximum length of a word.
  For each word, we generate all possible prefix and suffix combinations, which is O(L^2) for each word.
- Query (f): O(1), as we are performing a dictionary lookup.

Space Complexity:
- O(N * L^2), where N is the number of words and L is the maximum length of a word.
  We store all possible prefix and suffix combinations in the dictionary.

Overall, this solution is efficient for the given constraints.
"""

# Topic: Trie, Hash Map, String Matching