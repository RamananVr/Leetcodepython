"""
LeetCode Problem #657: Robot Return to Origin

Problem Statement:
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a string `moves` that represents the sequence of its moves, where each character in the string represents a move, the robot can move as follows:
- 'U': Move up by 1 unit.
- 'D': Move down by 1 unit.
- 'L': Move left by 1 unit.
- 'R': Move right by 1 unit.

The robot performs the moves in the order given in the string `moves`. Return `True` if the robot returns to the origin after it finishes all of its moves, or `False` otherwise.

Note:
- The input string `moves` will only contain characters 'U', 'D', 'L', and 'R'.
- The length of `moves` will be in the range [1, 2 * 10^4].

Example 1:
Input: moves = "UD"
Output: True
Explanation: The robot moves up once, and then down once. All moves cancel out, and the robot returns to the origin.

Example 2:
Input: moves = "LL"
Output: False
Explanation: The robot moves left twice. It does not return to the origin.

Constraints:
- 1 <= moves.length <= 2 * 10^4
- moves consists only of characters 'U', 'D', 'L', 'R'.
"""

def judgeCircle(moves: str) -> bool:
    """
    Determines if the robot returns to the origin after performing the given moves.

    :param moves: A string representing the sequence of moves ('U', 'D', 'L', 'R').
    :return: True if the robot returns to the origin, False otherwise.
    """
    # Initialize counters for vertical and horizontal movements
    vertical = 0
    horizontal = 0

    # Iterate through each move and update the counters
    for move in moves:
        if move == 'U':
            vertical += 1
        elif move == 'D':
            vertical -= 1
        elif move == 'L':
            horizontal -= 1
        elif move == 'R':
            horizontal += 1

    # The robot returns to the origin if both counters are zero
    return vertical == 0 and horizontal == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Robot returns to origin
    moves1 = "UD"
    print(judgeCircle(moves1))  # Expected Output: True

    # Test Case 2: Robot does not return to origin
    moves2 = "LL"
    print(judgeCircle(moves2))  # Expected Output: False

    # Test Case 3: Robot returns to origin after multiple moves
    moves3 = "UDLR"
    print(judgeCircle(moves3))  # Expected Output: True

    # Test Case 4: Robot does not return to origin with unbalanced moves
    moves4 = "UUDDLR"
    print(judgeCircle(moves4))  # Expected Output: False

    # Test Case 5: Empty string (edge case)
    moves5 = ""
    print(judgeCircle(moves5))  # Expected Output: True

"""
Time Complexity:
- O(n), where n is the length of the input string `moves`. We iterate through the string once to count the moves.

Space Complexity:
- O(1), as we use only a constant amount of extra space for the counters `vertical` and `horizontal`.

Topic: String
"""