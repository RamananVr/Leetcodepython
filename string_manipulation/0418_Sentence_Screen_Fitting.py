"""
LeetCode Problem #418: Sentence Screen Fitting

Problem Statement:
Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The sentence can be fitted on the screen following these rules:
1. A word cannot be split into two lines.
2. The order of words in the sentence must remain unchanged.
3. Two consecutive words in a line must be separated by a single space.
4. Each word in the sentence is at least one character long.

Example 1:
Input: sentence = ["hello", "world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Example 2:
Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-

Example 3:
Input: sentence = ["i", "had", "apple", "pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--

Constraints:
- 1 <= sentence.length <= 100
- 1 <= sentence[i].length <= 10
- sentence[i] consists of only lowercase English letters.
- 1 <= rows, cols <= 2 * 10^4
"""

def wordsTyping(sentence, rows, cols):
    """
    Function to calculate how many times the sentence can fit on the screen.

    :param sentence: List[str] - The sentence to fit on the screen.
    :param rows: int - Number of rows on the screen.
    :param cols: int - Number of columns on the screen.
    :return: int - Number of times the sentence can fit on the screen.
    """
    # Join the sentence into a single string with spaces
    sentence_str = " ".join(sentence) + " "
    n = len(sentence_str)
    
    # Initialize the pointer to track the position in the sentence string
    pointer = 0
    
    # Iterate through each row
    for _ in range(rows):
        # Move the pointer forward by the number of columns
        pointer += cols
        
        # If the pointer lands on a space, move to the next character
        if sentence_str[pointer % n] == " ":
            pointer += 1
        # If the pointer lands in the middle of a word, move it back to the start of the word
        else:
            while pointer > 0 and sentence_str[(pointer - 1) % n] != " ":
                pointer -= 1
    
    # The number of times the sentence fits is the number of full cycles of the sentence string
    return pointer // n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = ["hello", "world"]
    rows1, cols1 = 2, 8
    print(wordsTyping(sentence1, rows1, cols1))  # Output: 1

    # Test Case 2
    sentence2 = ["a", "bcd", "e"]
    rows2, cols2 = 3, 6
    print(wordsTyping(sentence2, rows2, cols2))  # Output: 2

    # Test Case 3
    sentence3 = ["i", "had", "apple", "pie"]
    rows3, cols3 = 4, 5
    print(wordsTyping(sentence3, rows3, cols3))  # Output: 1

# Time Complexity Analysis:
# - Constructing the sentence string takes O(S), where S is the total length of all words in the sentence.
# - Iterating through the rows takes O(rows).
# - Adjusting the pointer for each row takes O(cols) in the worst case, but since the pointer adjustment is bounded by the sentence length, it is effectively O(S).
# - Overall time complexity: O(rows + S).
#
# Space Complexity Analysis:
# - The only additional space used is for the sentence string, which is O(S).
# - Overall space complexity: O(S).

# Topic: String Manipulation