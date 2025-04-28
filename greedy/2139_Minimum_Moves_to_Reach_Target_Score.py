"""
LeetCode Problem #2139: Minimum Moves to Reach Target Score

Problem Statement:
You are playing a game with integers. You start with the integer `1` and you want to reach the integer `target`.

In one move, you can either:
1. Increment your current integer by `1` (i.e., `x = x + 1`).
2. If your current integer is divisible by `2`, you can multiply it by `2` (i.e., `x = x * 2`).

You can use the second operation at most `maxDoubles` times.

Given two integers `target` and `maxDoubles`, return the minimum number of moves needed to reach `target` starting with `1`.

Constraints:
- `1 <= target <= 10^9`
- `0 <= maxDoubles <= 100`
"""

def minMoves(target: int, maxDoubles: int) -> int:
    """
    Calculate the minimum number of moves to reach the target starting from 1.
    
    Args:
    target (int): The target integer to reach.
    maxDoubles (int): The maximum number of times the doubling operation can be used.
    
    Returns:
    int: The minimum number of moves required.
    """
    moves = 0
    while target > 1:
        if target % 2 == 0 and maxDoubles > 0:
            target //= 2
            maxDoubles -= 1
        elif maxDoubles == 0:
            # If no doubling operations are left, we can only increment.
            moves += target - 1
            break
        else:
            target -= 1
        moves += 1
    return moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = 10
    maxDoubles = 4
    print(minMoves(target, maxDoubles))  # Expected Output: 4

    # Test Case 2
    target = 19
    maxDoubles = 2
    print(minMoves(target, maxDoubles))  # Expected Output: 7

    # Test Case 3
    target = 5
    maxDoubles = 0
    print(minMoves(target, maxDoubles))  # Expected Output: 4

    # Test Case 4
    target = 1
    maxDoubles = 100
    print(minMoves(target, maxDoubles))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until `target` becomes 1. In the worst case, the loop runs O(log(target)) times 
  because each doubling operation halves the target. If no doubling is allowed, the loop runs O(target) times.
- Therefore, the time complexity is O(log(target)) when `maxDoubles > 0` and O(target) when `maxDoubles = 0`.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy
"""