"""
LeetCode Question #79: Word Search

Problem Statement:
Given an `m x n` board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Return `True` if the word exists in the grid, otherwise return `False`.

Constraints:
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of only lowercase and uppercase English letters.
"""

# Solution
def exist(board, word):
    def dfs(x, y, index):
        # Base case: if the entire word is matched
        if index == len(word):
            return True
        
        # Check boundaries and if the current cell matches the word[index]
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]:
            return False
        
        # Temporarily mark the cell as visited
        temp = board[x][y]
        board[x][y] = '#'
        
        # Explore all four directions
        found = (dfs(x + 1, y, index + 1) or
                 dfs(x - 1, y, index + 1) or
                 dfs(x, y + 1, index + 1) or
                 dfs(x, y - 1, index + 1))
        
        # Restore the cell's original value
        board[x][y] = temp
        
        return found
    
    # Iterate through each cell in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Start DFS if the first letter matches
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    print(exist(board1, word1))  # Output: True

    # Test Case 2
    board2 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word2 = "SEE"
    print(exist(board2, word2))  # Output: True

    # Test Case 3
    board3 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word3 = "ABCB"
    print(exist(board3, word3))  # Output: False

    # Test Case 4
    board4 = [
        ['A']
    ]
    word4 = "A"
    print(exist(board4, word4))  # Output: True

    # Test Case 5
    board5 = [
        ['A', 'B'],
        ['C', 'D']
    ]
    word5 = "ACDB"
    print(exist(board5, word5))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The DFS function is called for each cell in the board, and in the worst case, it explores all possible paths.
- For a board of size `m x n` and a word of length `k`, the time complexity is O(m * n * 4^k), where 4^k accounts for the branching factor (4 directions).

Space Complexity:
- The space complexity is O(k), where `k` is the length of the word. This is due to the recursion stack used in DFS.

Overall:
- Time Complexity: O(m * n * 4^k)
- Space Complexity: O(k)
"""

# Topic: Backtracking