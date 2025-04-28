"""
LeetCode Problem #1859: Sorting the Sentence

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending a positive integer `i` to the end of each word, where `i` represents 
the position of the word in the sentence. For example, the sentence "This is a sentence" can be shuffled as 
"sentence4 a2 is3 This1".

Given a shuffled sentence `s` containing no more than 9 words, reconstruct and return the original sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"

Example 2:
Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"

Constraints:
- 1 <= s.length <= 100
- `s` contains only lowercase and uppercase English letters, spaces, and digits.
- The number of words in `s` is between 1 and 9.
- The words in `s` are separated by a single space.
- `s` contains no leading or trailing spaces.

"""

# Solution
def sortSentence(s: str) -> str:
    """
    Reconstructs the original sentence from a shuffled sentence.

    Args:
    s (str): A shuffled sentence where each word has a number indicating its position.

    Returns:
    str: The original sentence in the correct order.
    """
    # Split the sentence into words
    words = s.split()
    
    # Create a list to store the words in their correct positions
    sorted_words = [None] * len(words)
    
    # Iterate through each word and place it in the correct position
    for word in words:
        # Extract the position from the word (last character)
        position = int(word[-1]) - 1
        # Extract the actual word (excluding the position)
        sorted_words[position] = word[:-1]
    
    # Join the sorted words into a single sentence
    return " ".join(sorted_words)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "is2 sentence4 This1 a3"
    print(sortSentence(s1))  # Output: "This is a sentence"

    # Test Case 2
    s2 = "Myself2 Me1 I4 and3"
    print(sortSentence(s2))  # Output: "Me Myself and I"

    # Test Case 3
    s3 = "word3 another2 first1"
    print(sortSentence(s3))  # Output: "first another word"

    # Test Case 4
    s4 = "one1"
    print(sortSentence(s4))  # Output: "one"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the sentence into words takes O(n), where n is the length of the string `s`.
- Iterating through the words and placing them in the correct position takes O(k), where k is the number of words (at most 9).
- Joining the sorted words into a single sentence takes O(n).
- Overall, the time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The `words` list and `sorted_words` list both take O(k) space, where k is the number of words (at most 9).
- The space complexity is O(k), which is constant since the number of words is bounded by 9.
"""

# Topic: Strings