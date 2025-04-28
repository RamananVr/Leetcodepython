"""
LeetCode Problem #676: Implement Magic Dictionary

Problem Statement:
Design a data structure that is initialized with a list of words, and provides a method to search a word. 
A search word matches if it can be obtained by modifying exactly one character of any word in the data structure.

Implement the MagicDictionary class:
- MagicDictionary() Initializes the object.
- void buildDict(List<String> dictionary) Sets the data structure with an array of distinct strings dictionary.
- bool search(String searchWord) Returns true if there is any word in the data structure that can be obtained by modifying exactly one character in searchWord, otherwise returns false.

Example:
Input:
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output:
[null, null, false, true, false, false]

Explanation:
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False

Constraints:
- 1 <= dictionary.length <= 100
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lowercase English letters.
- All the strings in dictionary are distinct.
- 1 <= searchWord.length <= 100
- searchWord consists of only lowercase English letters.
"""

# Python Solution
class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()

    def buildDict(self, dictionary: list[str]) -> None:
        """
        Build a dictionary through a list of words.
        """
        self.words = set(dictionary)

    def search(self, searchWord: str) -> bool:
        """
        Returns true if there is any word in the dictionary that can be obtained by modifying exactly one character in searchWord.
        """
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            # Count the number of differing characters
            diff_count = sum(1 for a, b in zip(word, searchWord) if a != b)
            if diff_count == 1:
                return True
        return False


# Example Test Cases
if __name__ == "__main__":
    # Initialize the MagicDictionary
    magicDictionary = MagicDictionary()
    
    # Build the dictionary
    magicDictionary.buildDict(["hello", "leetcode"])
    
    # Test cases
    print(magicDictionary.search("hello"))      # Output: False
    print(magicDictionary.search("hhllo"))      # Output: True
    print(magicDictionary.search("hell"))       # Output: False
    print(magicDictionary.search("leetcoded"))  # Output: False


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `buildDict`: O(n), where n is the number of words in the dictionary. We simply store the words in a set.
   - `search`: O(m * k), where m is the number of words in the dictionary and k is the average length of the words. 
     For each word in the dictionary, we compare it character by character with the searchWord.

2. Space Complexity:
   - The space complexity is O(n * k), where n is the number of words in the dictionary and k is the average length of the words. 
     This is because we store all the words in a set.

Topic: Hashing / String Manipulation
"""