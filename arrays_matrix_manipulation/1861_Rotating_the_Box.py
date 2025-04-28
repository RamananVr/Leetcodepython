"""
LeetCode Problem #1861: Rotating the Box

Problem Statement:
You are given an m x n matrix `box` of characters representing a box. The box is rotated 90 degrees clockwise, and then the stones fall due to gravity. Each cell in the box contains one of the following:

- A stone ('#')
- An obstacle ('*')
- Empty ('.')

The gravity causes the stones to fall down until they meet an obstacle or the bottom of the box. Once the box is rotated, return the box as a 2D list.

Example:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Constraints:
- m == box.length
- n == box[i].length
- 1 <= m, n <= 100
- box[i][j] is either '#', '*', or '.'.
"""

def rotateTheBox(box):
    """
    Rotates the box 90 degrees clockwise and simulates gravity for the stones.

    :param box: List[List[str]] - 2D list representing the box
    :return: List[List[str]] - Rotated and gravity-adjusted box
    """
    m, n = len(box), len(box[0])

    # Simulate gravity for each row
    for row in box:
        empty = n - 1  # Start from the rightmost column
        for col in range(n - 1, -1, -1):
            if row[col] == '#':  # Stone
                row[col], row[empty] = row[empty], row[col]
                empty -= 1
            elif row[col] == '*':  # Obstacle
                empty = col - 1

    # Rotate the box 90 degrees clockwise
    rotated_box = [[box[m - 1 - row][col] for row in range(m)] for col in range(n)]
    return rotated_box


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    box1 = [["#",".","#"]]
    print(rotateTheBox(box1))
    # Expected Output: [["."], ["#"], ["#"]]

    # Test Case 2
    box2 = [["#",".","*","."],
            ["#","#","*","."]]
    print(rotateTheBox(box2))
    # Expected Output: [["#","."],
    #                   ["#","#"],
    #                   ["*","*"],
    #                   [".","."]]

    # Test Case 3
    box3 = [["#","#","*",".","."],
            ["#",".",".","#","*"]]
    print(rotateTheBox(box3))
    # Expected Output: [[".","#"],
    #                   ["#","."],
    #                   ["*","."],
    #                   [".","#"],
    #                   [".","*"]]


"""
Time Complexity Analysis:
1. Gravity Simulation: For each row, we iterate through all columns once, which takes O(n) time per row. For m rows, this is O(m * n).
2. Rotation: To rotate the box, we iterate through all m * n elements once, which takes O(m * n) time.
Overall Time Complexity: O(m * n)

Space Complexity Analysis:
1. The rotated box requires additional space of size O(m * n) to store the result.
Overall Space Complexity: O(m * n)

Topic: Arrays, Matrix Manipulation
"""