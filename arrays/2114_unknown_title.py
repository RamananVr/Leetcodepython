"""
LeetCode Problem #2114: Maximum Number of Words Found in Sentences

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
You are given an array of strings `sentences`, where each `sentences[i]` represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Example:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence has 5 words: "alice", "and", "bob", "love", "leetcode".
- The second sentence has 4 words: "i", "think", "so", "too".
- The third sentence has 6 words: "this", "is", "great", "thanks", "very", "much".
Thus, the maximum number of words in a single sentence is 6.

Constraints:
- 1 <= sentences.length <= 100
- 1 <= sentences[i].length <= 100
- sentences[i] consists only of lowercase English letters and spaces.
- sentences[i] does not have leading or trailing spaces.
- All the words in sentences[i] are separated by a single space.
"""

# Python Solution
def mostWordsFound(sentences):
    """
    Function to find the maximum number of words in a single sentence.

    :param sentences: List[str] - List of sentences
    :return: int - Maximum number of words in a single sentence
    """
    return max(len(sentence.split()) for sentence in sentences)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    print(mostWordsFound(sentences1))  # Output: 6

    # Test Case 2
    sentences2 = ["hello world", "a b c d e f g", "singleword"]
    print(mostWordsFound(sentences2))  # Output: 7

    # Test Case 3
    sentences3 = ["one two three", "four five", "six seven eight nine"]
    print(mostWordsFound(sentences3))  # Output: 4

    # Test Case 4
    sentences4 = ["a", "b c", "d e f g h"]
    print(mostWordsFound(sentences4))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting each sentence into words using `split()` takes O(n), where n is the length of the sentence.
- We iterate over all sentences in the list, so the overall complexity is O(m * n), where m is the number of sentences and n is the average length of a sentence.

Space Complexity:
- The space complexity is O(1) for the function itself, as we are not using any additional data structures.
- However, the `split()` method creates a temporary list of words for each sentence, which has a space complexity of O(n) for each sentence. This is temporary and does not persist beyond the function call.
"""

# Topic: Arrays