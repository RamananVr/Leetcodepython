"""
LeetCode Question #245: Shortest Word Distance III

Problem Statement:
Given an array of strings `wordsDict` and two strings `word1` and `word2`, 
return the shortest distance between these two words in the list.

Note that `word1` and `word2` may be the same. If they are the same, 
find the shortest distance between two occurrences of it in the list.

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3

Constraints:
- 1 <= wordsDict.length <= 10^5
- 1 <= wordsDict[i].length <= 10
- `wordsDict[i]` consists of lowercase English letters.
- `word1` and `word2` are in `wordsDict`.
"""

def shortestWordDistance(wordsDict, word1, word2):
    """
    Finds the shortest distance between two words in a list.
    If the words are the same, finds the shortest distance between two occurrences of the word.

    :param wordsDict: List[str] - The list of words.
    :param word1: str - The first word.
    :param word2: str - The second word.
    :return: int - The shortest distance between the two words.
    """
    index1, index2 = -1, -1
    min_distance = float('inf')
    same_word = (word1 == word2)

    for i, word in enumerate(wordsDict):
        if word == word1:
            if same_word:
                # If word1 == word2, update index2 to the previous index1
                index2 = index1
            index1 = i
        elif word == word2:
            index2 = i

        if index1 != -1 and index2 != -1:
            min_distance = min(min_distance, abs(index1 - index2))

    return min_distance


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    wordsDict1 = ["practice", "makes", "perfect", "coding", "makes"]
    word1_1, word2_1 = "makes", "coding"
    print(shortestWordDistance(wordsDict1, word1_1, word2_1))  # Output: 1

    # Test Case 2
    wordsDict2 = ["practice", "makes", "perfect", "coding", "makes"]
    word1_2, word2_2 = "makes", "makes"
    print(shortestWordDistance(wordsDict2, word1_2, word2_2))  # Output: 3

    # Test Case 3
    wordsDict3 = ["a", "b", "a", "a", "b", "a"]
    word1_3, word2_3 = "a", "b"
    print(shortestWordDistance(wordsDict3, word1_3, word2_3))  # Output: 1

    # Test Case 4
    wordsDict4 = ["a", "b", "c", "a", "b", "c"]
    word1_4, word2_4 = "a", "a"
    print(shortestWordDistance(wordsDict4, word1_4, word2_4))  # Output: 3


"""
Time Complexity:
- The algorithm iterates through the `wordsDict` list once, making it O(n), 
  where n is the length of the list.

Space Complexity:
- The algorithm uses a constant amount of extra space, making it O(1).

Topic: Arrays
"""