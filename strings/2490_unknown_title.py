"""
LeetCode Problem #2490: Circular Sentence

Problem Statement:
A sentence is circular if:
- The last character of a word is the same as the first character of the next word.
- The last character of the last word is the same as the first character of the first word.

You are given a string `sentence` containing words separated by spaces. Determine if the sentence is circular.

Return `True` if the sentence is circular. Otherwise, return `False`.

Constraints:
- 1 <= sentence.length <= 500
- The sentence consists of lowercase English letters and spaces.
- There is no leading or trailing space in the sentence.
- All words are separated by a single space.
"""

def isCircularSentence(sentence: str) -> bool:
    """
    Determines if a sentence is circular.

    Args:
    sentence (str): The input sentence.

    Returns:
    bool: True if the sentence is circular, False otherwise.
    """
    words = sentence.split()
    n = len(words)
    
    # Check circular condition for all adjacent words
    for i in range(n):
        current_word = words[i]
        next_word = words[(i + 1) % n]  # Wrap around to the first word for the last word
        if current_word[-1] != next_word[0]:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Circular sentence
    sentence1 = "leetcode exercises sound delightful"
    print(isCircularSentence(sentence1))  # Expected output: True

    # Test Case 2: Not circular
    sentence2 = "hello world"
    print(isCircularSentence(sentence2))  # Expected output: False

    # Test Case 3: Single word (always circular)
    sentence3 = "a"
    print(isCircularSentence(sentence3))  # Expected output: True

    # Test Case 4: Circular with wrap-around
    sentence4 = "abc cde efg gab"
    print(isCircularSentence(sentence4))  # Expected output: True

    # Test Case 5: Not circular due to mismatch
    sentence5 = "abc cde efg xyz"
    print(isCircularSentence(sentence5))  # Expected output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the sentence into words takes O(n), where n is the length of the sentence.
- Checking the circular condition involves iterating through all words, which takes O(k), where k is the number of words.
- Overall time complexity: O(n + k). Since k <= n (number of words is bounded by the length of the sentence), the complexity simplifies to O(n).

Space Complexity:
- The `words` list stores all the words in the sentence, which takes O(k) space.
- Other variables use constant space.
- Overall space complexity: O(k), which is at most O(n).

Topic: Strings
"""