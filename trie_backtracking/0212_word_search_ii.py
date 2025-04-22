"""
LeetCode Question #212: Word Search II

Problem Statement:
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Constraints:
1. m == board.length
2. n == board[i].length
3. 1 <= m, n <= 12
4. board[i][j] is a lowercase English letter.
5. 1 <= words.length <= 3 * 10^4
6. 1 <= words[i].length <= 10
7. words[i] consists of lowercase English letters.
8. All the strings of words are unique.
"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie Node definition
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end_of_word = False

        # Build Trie from the list of words
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end_of_word = True
            return root

        # Backtracking function to search for words
        def backtrack(node, row, col, path):
            char = board[row][col]
            if char not in node.children:
                return
            next_node = node.children[char]
            path += char

            # Check if we found a word
            if next_node.is_end_of_word:
                result.add(path)
                next_node.is_end_of_word = False  # Avoid duplicate results

            # Mark the cell as visited
            board[row][col] = "#"

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != "#":
                    backtrack(next_node, nr, nc, path)

            # Restore the cell
            board[row][col] = char

        # Initialize variables
        trie_root = build_trie(words)
        result = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        # Start backtracking from each cell
        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(trie_root, r, c, "")

        return list(result)


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    board1 = [["o", "a", "a", "n"],
              ["e", "t", "a", "e"],
              ["i", "h", "k", "r"],
              ["i", "f", "l", "v"]]
    words1 = ["oath", "pea", "eat", "rain"]
    print(solution.findWords(board1, words1))  # Output: ["oath", "eat"]

    # Test Case 2
    board2 = [["a", "b"],
              ["c", "d"]]
    words2 = ["abcd"]
    print(solution.findWords(board2, words2))  # Output: []

    # Test Case 3
    board3 = [["a", "a"]]
    words3 = ["a"]
    print(solution.findWords(board3, words3))  # Output: ["a"]

"""
Time Complexity:
1. Building the Trie: O(W * L), where W is the number of words and L is the average length of the words.
2. Backtracking: O(M * N * 4^L), where M and N are the dimensions of the board, and L is the maximum length of a word.
   - Each cell can be visited at most once per word, and there are 4 possible directions to explore.

Overall Time Complexity: O(W * L + M * N * 4^L)

Space Complexity:
1. Trie Storage: O(W * L), for storing the words in the Trie.
2. Recursion Stack: O(L), where L is the maximum length of a word.

Overall Space Complexity: O(W * L + L)

Topic: Trie, Backtracking
"""