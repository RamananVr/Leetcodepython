"""
LeetCode Problem #1222: Queens That Can Attack the King

Problem Statement:
On an 8x8 chessboard, there can be multiple Black Queens and one White King.
You are given an array of integer coordinates `queens` that represents the positions of the Black Queens, 
and a pair of coordinates `king` that represents the position of the White King.

Return the coordinates of all the queens (in any order) that can directly attack the King. 
A queen can attack the King if they are in the same row, column, or diagonal, and there are no other pieces 
blocking the path between the queen and the king.

Constraints:
- `1 <= queens.length <= 63`
- `queens[i].length == 2`
- `0 <= queens[i][j] < 8`
- `king.length == 2`
- `0 <= king[j] < 8`
- All the given positions are unique.

Example:
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]

Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]
"""

def queensAttacktheKing(queens, king):
    """
    Finds all queens that can attack the king.

    :param queens: List[List[int]] - List of queen positions on the chessboard.
    :param king: List[int] - Position of the king on the chessboard.
    :return: List[List[int]] - List of queen positions that can attack the king.
    """
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Vertical and horizontal directions
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal directions
    ]
    queens_set = set(map(tuple, queens))  # Convert queens list to a set for O(1) lookups
    result = []

    for dx, dy in directions:
        x, y = king
        while 0 <= x < 8 and 0 <= y < 8:  # Stay within the board boundaries
            x += dx
            y += dy
            if (x, y) in queens_set:  # If a queen is found in this direction
                result.append([x, y])
                break  # Stop searching further in this direction

    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
    king = [0,0]
    print(queensAttacktheKing(queens, king))  # Output: [[0,1],[1,0],[3,3]]

    # Test Case 2
    queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
    king = [3,3]
    print(queensAttacktheKing(queens, king))  # Output: [[2,2],[3,4],[4,4]]

    # Test Case 3
    queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3]]
    king = [3,4]
    print(queensAttacktheKing(queens, king))  # Output: [[2,1],[5,6],[1,6],[4,0]]

"""
Time Complexity:
- Converting the queens list to a set takes O(Q), where Q is the number of queens.
- For each of the 8 directions, we traverse the board until we find a queen or go out of bounds. 
  In the worst case, this takes O(8 * 8) = O(64), which is constant.
- Overall time complexity: O(Q).

Space Complexity:
- The queens set takes O(Q) space.
- The result list takes O(min(Q, 8)) space, as at most 8 queens can attack the king.
- Overall space complexity: O(Q).

Topic: Arrays, Simulation
"""