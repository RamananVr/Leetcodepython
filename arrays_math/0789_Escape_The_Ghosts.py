"""
LeetCode Problem #789: Escape The Ghosts

Problem Statement:
You are playing a simplified Pacman game. You start at the point (0, 0), and your destination is at point (target[0], target[1]). 
There are several ghosts on the map, represented as an array `ghosts`, where `ghosts[i]` is the position of the i-th ghost.

Each turn, you and all the ghosts can move one step in one of the four cardinal directions: north, east, west, or south. 
You can move closer to the destination, but the ghosts can also move closer to you.

Return `true` if you can escape the ghosts and reach the destination. Otherwise, return `false`.

If the ghosts reach you before you reach the destination (or at the same time), you lose. If you reach the destination first, you win.

Constraints:
- `target.length == 2`
- `1 <= target[0], target[1] <= 10^4`
- `1 <= ghosts.length <= 100`
- `ghosts[i].length == 2`
- `-10^4 <= ghosts[i][0], ghosts[i][1] <= 10^4`

"""

def escapeGhosts(ghosts, target):
    """
    Determines if you can escape the ghosts and reach the target.

    :param ghosts: List[List[int]] - Positions of the ghosts
    :param target: List[int] - Target position
    :return: bool - True if you can escape the ghosts, False otherwise
    """
    # Calculate the Manhattan distance from the starting point (0, 0) to the target
    player_distance = abs(target[0]) + abs(target[1])
    
    # Check if any ghost can reach the target faster or at the same time as the player
    for ghost in ghosts:
        ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
        if ghost_distance <= player_distance:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Ghosts are far away
    ghosts = [[1, 0], [0, 3]]
    target = [0, 1]
    print(escapeGhosts(ghosts, target))  # Expected Output: True

    # Test Case 2: Ghost reaches the target at the same time
    ghosts = [[1, 0]]
    target = [2, 0]
    print(escapeGhosts(ghosts, target))  # Expected Output: False

    # Test Case 3: Ghosts are closer to the target than the player
    ghosts = [[2, 0], [1, 1]]
    target = [3, 3]
    print(escapeGhosts(ghosts, target))  # Expected Output: False

    # Test Case 4: No ghosts
    ghosts = []
    target = [5, 5]
    print(escapeGhosts(ghosts, target))  # Expected Output: True

    # Test Case 5: Ghosts are far away and cannot reach the target in time
    ghosts = [[-10, -10], [10, 10]]
    target = [1, 1]
    print(escapeGhosts(ghosts, target))  # Expected Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the Manhattan distance for the player is O(1).
- Calculating the Manhattan distance for each ghost is O(ghosts.length).
- Overall, the time complexity is O(n), where n is the number of ghosts.

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to store distances and do not use any additional data structures.

Topic: Arrays, Math
"""