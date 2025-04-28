"""
LeetCode Question #2766: Relocate Marbles

Problem Statement:
You are given two integer arrays `nums` and `moveFrom` and `moveTo` of length `n`.

- `nums` represents the positions of marbles on a number line.
- `moveFrom[i]` and `moveTo[i]` represent that you want to move the marble from position `moveFrom[i]` to position `moveTo[i]`.

After performing all the moves, return a sorted list of the final positions of the marbles.

Notes:
- It is guaranteed that there are no duplicate positions in `nums`.
- It is guaranteed that no two marbles will end up in the same position after all moves.

Constraints:
- `1 <= nums.length, moveFrom.length, moveTo.length <= 10^5`
- `-10^9 <= nums[i], moveFrom[i], moveTo[i] <= 10^9`
"""

# Solution
def relocateMarbles(nums, moveFrom, moveTo):
    # Use a set to track the positions of marbles
    marble_positions = set(nums)
    
    # Process each move
    for from_pos, to_pos in zip(moveFrom, moveTo):
        # Remove the marble from the old position
        marble_positions.remove(from_pos)
        # Add the marble to the new position
        marble_positions.add(to_pos)
    
    # Return the sorted list of final positions
    return sorted(marble_positions)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 6, 7, 8]
    moveFrom = [1, 7, 2]
    moveTo = [2, 9, 5]
    print(relocateMarbles(nums, moveFrom, moveTo))  # Output: [2, 5, 6, 8, 9]

    # Test Case 2
    nums = [3, 4, 5]
    moveFrom = [3, 4]
    moveTo = [6, 7]
    print(relocateMarbles(nums, moveFrom, moveTo))  # Output: [5, 6, 7]

    # Test Case 3
    nums = [10, 20, 30]
    moveFrom = [10, 20]
    moveTo = [40, 50]
    print(relocateMarbles(nums, moveFrom, moveTo))  # Output: [30, 40, 50]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `remove` and `add` operations on a set are O(1) on average.
- Sorting the final positions takes O(k log k), where k is the number of unique positions.
- Overall complexity: O(n + k log k), where n is the length of `moveFrom` and `moveTo`.

Space Complexity:
- The space used by the set `marble_positions` is O(k), where k is the number of unique positions.
- Overall space complexity: O(k).
"""

# Topic: Arrays, HashSet