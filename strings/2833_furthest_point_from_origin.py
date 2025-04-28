"""
LeetCode Question #2833: Furthest Point From Origin

Problem Statement:
You are given a string `moves` of length `n` consisting of characters 'L', 'R', and '_'. 
The string represents the moves a robot can make on a number line starting at the origin (0). 
- 'L' means the robot moves one unit to the left.
- 'R' means the robot moves one unit to the right.
- '_' means the robot stays in its current position.

Return the maximum distance the robot can be from the origin after performing all the moves.

Constraints:
- 1 <= moves.length <= 1000
- moves consists of characters 'L', 'R', and '_'.
"""

def furthestDistanceFromOrigin(moves: str) -> int:
    """
    Calculate the maximum distance the robot can be from the origin after performing all moves.

    :param moves: A string consisting of 'L', 'R', and '_'.
    :return: The maximum distance from the origin.
    """
    left_moves = moves.count('L')
    right_moves = moves.count('R')
    stationary_moves = moves.count('_')
    
    # The maximum distance is achieved by treating all stationary moves as either 'L' or 'R'.
    return abs(left_moves - right_moves) + stationary_moves


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    moves = "L_RL__R"
    print(furthestDistanceFromOrigin(moves))  # Expected Output: 5

    # Test Case 2: All moves are stationary
    moves = "_____"
    print(furthestDistanceFromOrigin(moves))  # Expected Output: 5

    # Test Case 3: Equal number of 'L' and 'R'
    moves = "LRLRLR"
    print(furthestDistanceFromOrigin(moves))  # Expected Output: 0

    # Test Case 4: Only 'L' moves
    moves = "LLLLL"
    print(furthestDistanceFromOrigin(moves))  # Expected Output: 5

    # Test Case 5: Only 'R' moves
    moves = "RRRRR"
    print(furthestDistanceFromOrigin(moves))  # Expected Output: 5

    # Test Case 6: Mixed moves with no stationary
    moves = "LLRRR"
    print(furthestDistanceFromOrigin(moves))  # Expected Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the occurrences of 'L', 'R', and '_' in the string takes O(n), where n is the length of the string `moves`.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space to store the counts of 'L', 'R', and '_'.
- Therefore, the space complexity is O(1).

Topic: Strings
"""