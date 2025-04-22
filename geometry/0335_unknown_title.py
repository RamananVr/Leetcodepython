"""
LeetCode Problem #335: Self Crossing

Problem Statement:
You are given an array of integers `distance` representing the distance of a sequence of moves. 
The moves are always performed in the following order:
  - Move north by `distance[0]`.
  - Move west by `distance[1]`.
  - Move south by `distance[2]`.
  - Move east by `distance[3]`.
  - Repeat the same cycle of directions.

Return `True` if the path crosses itself at any point, and `False` otherwise.

Example 1:
Input: distance = [2, 1, 1, 2]
Output: True

Example 2:
Input: distance = [1, 2, 3, 4]
Output: False

Example 3:
Input: distance = [1, 1, 1, 1]
Output: True

Constraints:
- 1 <= distance.length <= 10^4
- 1 <= distance[i] <= 10^4
"""

def isSelfCrossing(distance):
    """
    Determines if the path crosses itself.

    :param distance: List[int] - distances of moves in the sequence
    :return: bool - True if the path crosses itself, False otherwise
    """
    n = len(distance)
    for i in range(3, n):
        # Case 1: Current line crosses the line 3 steps ahead
        if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
            return True
        # Case 2: Current line crosses the line 4 steps ahead
        if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
            return True
        # Case 3: Current line crosses the line 5 steps ahead
        if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 1] <= distance[i - 3] and distance[i - 1] + distance[i - 5] >= distance[i - 3]:
            return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Path crosses itself
    distance1 = [2, 1, 1, 2]
    print(isSelfCrossing(distance1))  # Output: True

    # Test Case 2: Path does not cross itself
    distance2 = [1, 2, 3, 4]
    print(isSelfCrossing(distance2))  # Output: False

    # Test Case 3: Path crosses itself
    distance3 = [1, 1, 1, 1]
    print(isSelfCrossing(distance3))  # Output: True

    # Test Case 4: Longer path that does not cross itself
    distance4 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(isSelfCrossing(distance4))  # Output: False

    # Test Case 5: Longer path that crosses itself
    distance5 = [1, 1, 2, 1, 1]
    print(isSelfCrossing(distance5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `distance` array once, checking conditions for each index.
- Therefore, the time complexity is O(n), where n is the length of the `distance` array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables and comparisons.
- Therefore, the space complexity is O(1).

Topic: Geometry
"""