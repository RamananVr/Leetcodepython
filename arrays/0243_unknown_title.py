"""
LeetCode Problem #243: Shortest Word Distance

Problem Statement:
Given an array of strings `wordsDict` and two different strings `word1` and `word2`, 
return the shortest distance between these two words in the list.

The distance between two words is the absolute difference between their indices in the array.

Example:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Constraints:
1. 1 <= wordsDict.length <= 3 * 10^4
2. wordsDict[i] consists of lowercase English letters.
3. word1 and word2 are in `wordsDict`.
4. word1 != word2
"""

# Solution
def shortestDistance(wordsDict, word1, word2):
    """
    Finds the shortest distance between two words in a list.

    :param wordsDict: List[str] - List of words
    :param word1: str - First word
    :param word2: str - Second word
    :return: int - Shortest distance between word1 and word2
    """
    index1, index2 = -1, -1
    min_distance = float('inf')

    for i, word in enumerate(wordsDict):
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i
        
        if index1 != -1 and index2 != -1:
            min_distance = min(min_distance, abs(index1 - index2))
    
    return min_distance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(shortestDistance(wordsDict, word1, word2))  # Output: 3

    # Test Case 2
    wordsDict = ["a", "b", "c", "d", "e", "f", "g", "h"]
    word1 = "a"
    word2 = "h"
    print(shortestDistance(wordsDict, word1, word2))  # Output: 7

    # Test Case 3
    wordsDict = ["hello", "world", "leetcode", "hello", "world"]
    word1 = "hello"
    word2 = "world"
    print(shortestDistance(wordsDict, word1, word2))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the `wordsDict` list once, making the time complexity O(n), 
where n is the length of the list.

Space Complexity:
The function uses a constant amount of extra space (variables index1, index2, and min_distance), 
making the space complexity O(1).
"""

# Topic: Arrays