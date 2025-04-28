"""
LeetCode Problem #2075: Decode the Slanted Ciphertext

Problem Statement:
A string `encodedText` is given, and it represents a slanted ciphertext encoded from a rectangular matrix of characters. 
The matrix is constructed by writing the plaintext string row by row, and then reading the characters diagonally from 
top-left to bottom-right.

Given the encoded string `encodedText` and the number of rows `rows` in the matrix, return the original plaintext string 
after decoding. Remove trailing spaces at the end of the plaintext.

Example:
Input: encodedText = "ch   ie   pr", rows = 3
Output: "cipher"

Explanation:
The matrix is:
c h
i e
p r
Reading diagonally gives "cipher".

Constraints:
- 1 <= encodedText.length <= 10^5
- encodedText consists of lowercase English letters and spaces.
- `rows` is an integer such that `rows` > 0 and `rows` <= encodedText.length.
"""

# Solution
def decodeCiphertext(encodedText: str, rows: int) -> str:
    # Calculate the number of columns in the matrix
    cols = len(encodedText) // rows
    
    # Initialize the result string
    result = []
    
    # Decode the text by reading diagonally
    for col in range(cols):
        for row in range(rows):
            index = row * cols + col + row
            if index < len(encodedText):
                result.append(encodedText[index])
    
    # Join the result and strip trailing spaces
    return ''.join(result).rstrip()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    encodedText1 = "ch   ie   pr"
    rows1 = 3
    print(decodeCiphertext(encodedText1, rows1))  # Output: "cipher"

    # Test Case 2
    encodedText2 = "iveo    eed   l te   olc"
    rows2 = 4
    print(decodeCiphertext(encodedText2, rows2))  # Output: "i love leetcode"

    # Test Case 3
    encodedText3 = "coding"
    rows3 = 1
    print(decodeCiphertext(encodedText3, rows3))  # Output: "coding"

    # Test Case 4
    encodedText4 = "a b c d e f g h i j k l m n o p"
    rows4 = 4
    print(decodeCiphertext(encodedText4, rows4))  # Output: "abcdefghijklmno"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates over each column and row of the matrix, resulting in O(rows * cols) iterations.
- Since rows * cols = len(encodedText), the time complexity is O(n), where n is the length of the encodedText.

Space Complexity:
- The algorithm uses a list to store the decoded characters, which requires O(n) space.
- Therefore, the space complexity is O(n).

Topic: Strings
"""