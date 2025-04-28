"""
LeetCode Problem #68: Text Justification

Problem Statement:
Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the extra spaces go to the leftmost words on the line.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed `maxWidth`.
- The input array `words` will contain at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
   "What   must   be",
   "acknowledgment  ",
   "shall be        "
]

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain",
                "to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
   "Science  is  what we",
   "understand      well",
   "enough to explain to",
   "a  computer.  Art is",
   "everything  else  we",
   "do                  "
]

Constraints:
- 1 <= words.length <= 300
- 1 <= words[i].length <= 20
- words[i] consists of only English letters and symbols.
- 1 <= maxWidth <= 100
- words[i].length <= maxWidth
"""

def fullJustify(words, maxWidth):
    result = []
    line = []
    line_length = 0

    for word in words:
        # Check if adding the current word exceeds maxWidth
        if line_length + len(word) + len(line) > maxWidth:
            # Distribute spaces for the current line
            for i in range(maxWidth - line_length):
                line[i % (len(line) - 1 or 1)] += ' '
            result.append(''.join(line))
            line, line_length = [], 0
        line.append(word)
        line_length += len(word)

    # Handle the last line (left-justified)
    result.append(' '.join(line).ljust(maxWidth))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    print(fullJustify(words1, maxWidth1))
    # Expected Output:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]

    # Test Case 2
    words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth2 = 16
    print(fullJustify(words2, maxWidth2))
    # Expected Output:
    # [
    #    "What   must   be",
    #    "acknowledgment  ",
    #    "shall be        "
    # ]

    # Test Case 3
    words3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
              "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth3 = 20
    print(fullJustify(words3, maxWidth3))
    # Expected Output:
    # [
    #    "Science  is  what we",
    #    "understand      well",
    #    "enough to explain to",
    #    "a  computer.  Art is",
    #    "everything  else  we",
    #    "do                  "
    # ]

# Time Complexity Analysis:
# The algorithm processes each word exactly once, and for each line, it distributes spaces in O(maxWidth) time.
# Therefore, the overall time complexity is O(n + L), where n is the number of words and L is the total number of characters in all words.

# Space Complexity Analysis:
# The space complexity is O(n + maxWidth), where n is the number of words (for the result list) and maxWidth is for temporary storage of each line.

# Topic: Strings, Greedy Algorithm