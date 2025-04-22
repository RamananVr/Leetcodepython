"""
LeetCode Question #244: Shortest Word Distance II

Problem Statement:
Design a class that receives a list of words and can return the shortest distance between two given words in the list.

Implement the WordDistance class:
- WordDistance(wordsDict) Initializes the object with the words dictionary wordsDict.
- shortest(word1, word2) Returns the shortest distance between word1 and word2 in the list.

Example:
Input:
["practice", "makes", "perfect", "coding", "makes"]
WordDistance.shortest("coding", "practice") -> 3
WordDistance.shortest("makes", "coding") -> 1

Constraints:
- 1 <= wordsDict.length <= 3 * 10^4
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.
- word1 != word2
"""

# Solution
class WordDistance:
    def __init__(self, wordsDict):
        """
        Initialize the WordDistance object with the words dictionary.
        Precompute the indices of each word for efficient distance calculation.
        """
        self.word_indices = {}
        for i, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(i)

    def shortest(self, word1, word2):
        """
        Returns the shortest distance between word1 and word2 in the list.
        """
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        i, j = 0, 0
        min_distance = float('inf')

        # Use two pointers to find the minimum distance
        while i < len(indices1) and j < len(indices2):
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        return min_distance


# Example Test Cases
if __name__ == "__main__":
    # Initialize the WordDistance object
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word_distance = WordDistance(wordsDict)

    # Test cases
    print(word_distance.shortest("coding", "practice"))  # Output: 3
    print(word_distance.shortest("makes", "coding"))     # Output: 1
    print(word_distance.shortest("perfect", "makes"))    # Output: 2


"""
Time and Space Complexity Analysis:

1. Initialization (__init__):
   - Time Complexity: O(n), where n is the length of wordsDict. We iterate through the list once to build the word_indices dictionary.
   - Space Complexity: O(n), as we store the indices of each word in the dictionary.

2. Shortest Method:
   - Time Complexity: O(m + k), where m and k are the lengths of the lists of indices for word1 and word2, respectively. The two-pointer approach iterates through both lists.
   - Space Complexity: O(1), as we only use a few variables for computation.

Overall:
- Initialization: O(n) time and space.
- Query: O(m + k) time and O(1) space.

Topic: Hash Table, Two Pointers
"""