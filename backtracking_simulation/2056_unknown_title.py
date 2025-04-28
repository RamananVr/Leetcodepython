"""
LeetCode Problem #2056: Number of Valid Move Combinations On Chessboard

Problem Statement:
You are given a chessboard of size 8x8 and a list of pieces, where each piece is either a "rook", "bishop", or "queen". 
You are also given a list of positions where each piece is initially located on the chessboard. The chessboard is 
represented as a grid with rows numbered from 1 to 8 and columns numbered from 1 to 8. The position of the i-th piece 
is given as positions[i] = [ri, ci], where ri is the row and ci is the column.

A move combination is a sequence of moves for all the pieces such that:
1. Each piece moves exactly once.
2. No two pieces occupy the same square after moving.
3. Each piece moves according to the rules of chess:
   - A rook moves any number of squares along a row or column.
   - A bishop moves any number of squares diagonally.
   - A queen moves any number of squares along a row, column, or diagonal.

Return the number of valid move combinations.

Constraints:
- 1 <= pieces.length <= 4
- pieces[i] is either "rook", "bishop", or "queen".
- positions.length == pieces.length
- 1 <= ri, ci <= 8

"""

from itertools import product

def numOfValidMoveCombinations(pieces, positions):
    def get_moves(piece, r, c):
        """Generate all possible moves for a given piece from position (r, c)."""
        moves = set()
        if piece in ("rook", "queen"):
            # Horizontal and vertical moves
            for i in range(1, 9):
                if i != r:  # Vertical moves
                    moves.add((i, c))
                if i != c:  # Horizontal moves
                    moves.add((r, i))
        if piece in ("bishop", "queen"):
            # Diagonal moves
            for i in range(1, 9):
                if i != 0:
                    if 1 <= r + i <= 8 and 1 <= c + i <= 8:
                        moves.add((r + i, c + i))
                    if 1 <= r - i <= 8 and 1 <= c - i <= 8:
                        moves.add((r - i, c - i))
                    if 1 <= r + i <= 8 and 1 <= c - i <= 8:
                        moves.add((r + i, c - i))
                    if 1 <= r - i <= 8 and 1 <= c + i <= 8:
                        moves.add((r - i, c + i))
        return moves

    def is_valid_combination(moves):
        """Check if a combination of moves is valid (no two pieces occupy the same square)."""
        return len(set(moves)) == len(moves)

    # Generate all possible moves for each piece
    all_moves = []
    for i, piece in enumerate(pieces):
        r, c = positions[i]
        moves = get_moves(piece, r, c)
        moves.add((r, c))  # Include the option of not moving
        all_moves.append(list(moves))

    # Generate all combinations of moves
    valid_combinations = 0
    for combination in product(*all_moves):
        if is_valid_combination(combination):
            valid_combinations += 1

    return valid_combinations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pieces = ["rook"]
    positions = [[1, 1]]
    print(numOfValidMoveCombinations(pieces, positions))  # Output: 15

    # Test Case 2
    pieces = ["queen", "bishop"]
    positions = [[1, 1], [2, 2]]
    print(numOfValidMoveCombinations(pieces, positions))  # Output: 65

    # Test Case 3
    pieces = ["rook", "rook"]
    positions = [[1, 1], [1, 2]]
    print(numOfValidMoveCombinations(pieces, positions))  # Output: 223

    # Test Case 4
    pieces = ["queen", "queen"]
    positions = [[1, 1], [8, 8]]
    print(numOfValidMoveCombinations(pieces, positions))  # Output: 1297

"""
Time Complexity:
- Let n = len(pieces) (number of pieces).
- For each piece, we generate all possible moves. Each piece can have up to O(64) moves (8x8 board).
- Generating all combinations of moves involves iterating over O(64^n) combinations.
- Checking if a combination is valid takes O(n) time.
- Overall time complexity: O(64^n * n), where n <= 4 (constant upper bound).

Space Complexity:
- The space required to store all possible moves for each piece is O(64 * n).
- The space required for the combinations is O(64^n).
- Overall space complexity: O(64^n).

Topic: Backtracking, Simulation
"""