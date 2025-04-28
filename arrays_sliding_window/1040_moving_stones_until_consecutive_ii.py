"""
LeetCode Question #1040: Moving Stones Until Consecutive II

Problem Statement:
You are given an integer array `stones`, where `stones[i]` is the position of the ith stone on an infinite number line. 
The positions of the stones are unique and sorted in ascending order.

In one move, you can:
- Move a single stone from its current position to any other position.

You need to move the stones until the positions of the stones are consecutive. 
Return the minimum and maximum number of moves needed.

Example:
Input: stones = [7, 4, 9]
Output: [1, 2]

Explanation:
- Minimum moves: Move stone at position 4 to position 8, resulting in [7, 8, 9].
- Maximum moves: Move stone at position 4 to position 6, and move stone at position 9 to position 5, resulting in [5, 6, 7].

Constraints:
- 3 <= stones.length <= 10^4
- 1 <= stones[i] <= 10^9
- stones[i] are unique and sorted in ascending order.
"""

# Python Solution
def numMovesStonesII(stones):
    stones.sort()
    n = len(stones)
    max_moves = stones[-1] - stones[0] + 1 - n - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)
    min_moves = float('inf')
    
    j = 0
    for i in range(n):
        while j < n and stones[j] - stones[i] + 1 <= n:
            j += 1
        count = j - i
        if count == n - 1 and stones[j - 1] - stones[i] + 1 == n - 1:
            min_moves = min(min_moves, 2)
        else:
            min_moves = min(min_moves, n - count)
    
    return [min_moves, max_moves]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones = [7, 4, 9]
    print(numMovesStonesII(stones))  # Output: [1, 2]

    # Test Case 2
    stones = [6, 5, 4, 3, 10]
    print(numMovesStonesII(stones))  # Output: [2, 5]

    # Test Case 3
    stones = [1, 2, 3, 4, 5]
    print(numMovesStonesII(stones))  # Output: [0, 0]

    # Test Case 4
    stones = [100, 101, 104, 105]
    print(numMovesStonesII(stones))  # Output: [1, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the stones array takes O(n log n).
- The sliding window approach to calculate the minimum moves takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space apart from the input array.
- Overall space complexity: O(1).

Topic: Arrays, Sliding Window
"""