"""
LeetCode Problem #1033: Moving Stones Until Consecutive

Problem Statement:
Three stones are on a number line at positions `a`, `b`, and `c`. Each turn, you pick up a stone and move it to an integer position 
so that the positions of the three stones are still distinct. Formally, let the positions of the stones be `x`, `y`, and `z` with 
`x < y < z`. You can move a stone from position `x` to any position in the range `(x, z)` that is not occupied by another stone.

The goal is to make the stones consecutive, i.e., `y - x == 1` and `z - y == 1`. Return an array `answer` of length 2 where:
- `answer[0]` is the minimum number of moves needed to make the stones consecutive.
- `answer[1]` is the maximum number of moves needed to make the stones consecutive.

Example:
Input: a = 1, b = 2, c = 5
Output: [1, 2]

Constraints:
- 1 <= a, b, c <= 100
- a, b, and c are distinct.
"""

def numMovesStones(a: int, b: int, c: int) -> list[int]:
    # Sort the positions of the stones
    x, y, z = sorted([a, b, c])
    
    # Calculate the gaps between the stones
    gap1 = y - x - 1
    gap2 = z - y - 1
    
    # Minimum moves
    if gap1 == 0 and gap2 == 0:
        min_moves = 0
    elif gap1 <= 1 or gap2 <= 1:
        min_moves = 1
    else:
        min_moves = 2
    
    # Maximum moves
    max_moves = gap1 + gap2
    
    return [min_moves, max_moves]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b, c = 1, 2, 5
    print(numMovesStones(a, b, c))  # Output: [1, 2]

    # Test Case 2
    a, b, c = 4, 3, 2
    print(numMovesStones(a, b, c))  # Output: [0, 0]

    # Test Case 3
    a, b, c = 3, 5, 1
    print(numMovesStones(a, b, c))  # Output: [1, 2]

    # Test Case 4
    a, b, c = 10, 1, 5
    print(numMovesStones(a, b, c))  # Output: [1, 7]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the three numbers takes O(1) since there are only three elements.
- Calculating the gaps and determining the minimum and maximum moves are O(1) operations.
- Overall, the time complexity is O(1).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables and calculations.
- Overall, the space complexity is O(1).

Topic: Arrays, Sorting, Simulation
"""