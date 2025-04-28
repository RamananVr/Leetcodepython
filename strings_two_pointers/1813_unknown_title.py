"""
LeetCode Problem #1813: Sentence Similarity III

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
For example, "Hello World", "Hello", "Alice and Bob", and "Alice" are all sentences. Words consist of 
only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence 
(possibly empty) inside one of these sentences such that the two sentences become equal. For example, 
sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting 
"my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. 
Otherwise, return false.

Example 1:
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned into sentence1 by inserting "name is" between "My" and "Haley".

Example 2:
Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make them equal.

Example 3:
Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned into sentence1 by inserting "right now" at the end of the sentence.

Constraints:
- 1 <= sentence1.length, sentence2.length <= 100
- sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
- The words in sentence1 and sentence2 are separated by a single space.
"""

def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    """
    Determines if two sentences are similar by checking if one can be made equal to the other
    by inserting an arbitrary sentence in one of them.
    """
    # Split the sentences into words
    words1 = sentence1.split()
    words2 = sentence2.split()
    
    # Ensure words1 is the longer sentence
    if len(words1) < len(words2):
        words1, words2 = words2, words1
    
    # Use two pointers to check prefix and suffix similarity
    i, j = 0, 0
    while i < len(words2) and words1[i] == words2[i]:
        i += 1
    while j < len(words2) and words1[-(j + 1)] == words2[-(j + 1)]:
        j += 1
    
    # Check if the entire shorter sentence is covered by prefix and suffix
    return i + j >= len(words2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "My name is Haley"
    sentence2 = "My Haley"
    print(areSentencesSimilar(sentence1, sentence2))  # Output: True

    # Test Case 2
    sentence1 = "of"
    sentence2 = "A lot of words"
    print(areSentencesSimilar(sentence1, sentence2))  # Output: False

    # Test Case 3
    sentence1 = "Eating right now"
    sentence2 = "Eating"
    print(areSentencesSimilar(sentence1, sentence2))  # Output: True

    # Test Case 4
    sentence1 = "Hello"
    sentence2 = "Hello"
    print(areSentencesSimilar(sentence1, sentence2))  # Output: True

    # Test Case 5
    sentence1 = "I love programming"
    sentence2 = "I programming"
    print(areSentencesSimilar(sentence1, sentence2))  # Output: True

"""
Time Complexity:
- Splitting the sentences into words takes O(n + m), where n and m are the lengths of sentence1 and sentence2.
- The prefix and suffix comparison takes O(min(n, m)).
- Overall time complexity: O(n + m).

Space Complexity:
- The space required to store the split words is O(n + m).
- Overall space complexity: O(n + m).

Topic: Strings, Two Pointers
"""