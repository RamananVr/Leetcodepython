"""
LeetCode Question #422: Valid Word Square

Problem Statement:
Given an array of strings `words`, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the k-th row and k-th column read the same string, 
where 0 ≤ k < max(numRows, numColumns).

In other words, the character at position (i, j) in the 2D structure should match the character at position (j, i).

Example 1:
Input: words = ["abcd", "bnrt", "crmy", "dtye"]
Output: true
Explanation:
The 2D grid looks like this:
a b c d
b n r t
c r m y
d t y e
As you can see, the characters match at (i, j) and (j, i).

Example 2:
Input: words = ["abcd", "bnrt", "crm", "dt"]
Output: true
Explanation:
The 2D grid looks like this:
a b c d
b n r t
c r m
d t
As you can see, the characters match at (i, j) and (j, i).

Example 3:
Input: words = ["ball", "area", "read", "lady"]
Output: false
Explanation:
The 2D grid looks like this:
b a l l
a r e a
r e a d
l a d y
The third row and third column do not match.

Constraints:
- 1 <= words.length <= 200
- 1 <= words[i].length <= 200
- words[i] consists of only lowercase English letters.
"""

def validWordSquare(words):
    """
    Function to check if the given list of words forms a valid word square.

    :param words: List[str] - List of strings representing the word square.
    :return: bool - True if the input forms a valid word square, False otherwise.
    """
    for i in range(len(words)):
        for j in range(len(words[i])):
            # Check if the corresponding column exists and matches the character
            if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                return False
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abcd", "bnrt", "crmy", "dtye"]
    print(validWordSquare(words1))  # Output: True

    # Test Case 2
    words2 = ["abcd", "bnrt", "crm", "dt"]
    print(validWordSquare(words2))  # Output: True

    # Test Case 3
    words3 = ["ball", "area", "read", "lady"]
    print(validWordSquare(words3))  # Output: False

    # Test Case 4 (Edge Case: Single word)
    words4 = ["a"]
    print(validWordSquare(words4))  # Output: True

    # Test Case 5 (Edge Case: Empty word square)
    words5 = []
    print(validWordSquare(words5))  # Output: True

"""
Time Complexity Analysis:
- Let n be the number of rows in the input `words` and m be the maximum length of a word.
- The outer loop runs for n iterations, and the inner loop runs for up to m iterations.
- In the worst case, we check each character in the grid once, resulting in O(n * m) time complexity.

Space Complexity Analysis:
- The algorithm uses only a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""