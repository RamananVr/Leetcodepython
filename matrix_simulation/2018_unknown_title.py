"""
LeetCode Problem #2018: Check if Word Can Be Placed In Crossword

Problem Statement:
You are given an m x n matrix crossword, where crossword[i][j] is a character representing the cell in the crossword grid.

- ' ' (a blank space) indicates that the cell is empty.
- '#' indicates that the cell is blocked.

You are also given a string word. Return true if the word can be placed in the crossword grid either horizontally or vertically:
- The word must be placed in consecutive cells that are either all empty (' ') or match the corresponding character in the word.
- If the word is placed horizontally, it must not be blocked by a cell to its left or right (i.e., the cell immediately to the left and right of the word must either be out of bounds or contain '#').
- If the word is placed vertically, it must not be blocked by a cell above or below it.

Note:
- A word can be placed in the reverse order in the crossword grid.

Example 1:
Input: crossword = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: True

Example 2:
Input: crossword = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: False

Example 3:
Input: crossword = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: True

Constraints:
- m == crossword.length
- n == crossword[i].length
- 1 <= m, n <= 100
- crossword[i][j] is either ' ' or '#'.
- 1 <= word.length <= max(m, n)
- word consists of only lowercase English letters.
"""

def can_place_word_in_crossword(crossword, word):
    def can_place(row, col, dr, dc, word):
        for i, char in enumerate(word):
            r, c = row + i * dr, col + i * dc
            if not (0 <= r < len(crossword) and 0 <= c < len(crossword[0])):
                return False
            if crossword[r][c] != ' ' and crossword[r][c] != char:
                return False
        # Check boundaries
        before_r, before_c = row - dr, col - dc
        after_r, after_c = row + len(word) * dr, col + len(word) * dc
        if (0 <= before_r < len(crossword) and 0 <= before_c < len(crossword[0]) and crossword[before_r][before_c] != '#'):
            return False
        if (0 <= after_r < len(crossword) and 0 <= after_c < len(crossword[0]) and crossword[after_r][after_c] != '#'):
            return False
        return True

    def check_word(word):
        for row in range(len(crossword)):
            for col in range(len(crossword[0])):
                if can_place(row, col, 0, 1, word) or can_place(row, col, 1, 0, word):
                    return True
        return False

    return check_word(word) or check_word(word[::-1])

# Example Test Cases
if __name__ == "__main__":
    crossword1 = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
    word1 = "abc"
    print(can_place_word_in_crossword(crossword1, word1))  # Output: True

    crossword2 = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]]
    word2 = "ac"
    print(can_place_word_in_crossword(crossword2, word2))  # Output: False

    crossword3 = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]]
    word3 = "ca"
    print(can_place_word_in_crossword(crossword3, word3))  # Output: True

# Time and Space Complexity Analysis
# Time Complexity:
# - The function iterates over all cells in the crossword grid (m * n).
# - For each cell, it checks two directions (horizontal and vertical) for both the word and its reverse.
# - Each check involves iterating over the length of the word (O(word.length)).
# - Overall complexity: O(m * n * word.length).

# Space Complexity:
# - The function uses constant space for variables and does not use any additional data structures.
# - Overall complexity: O(1).

# Topic: Matrix, Simulation