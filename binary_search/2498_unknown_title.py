"""
LeetCode Problem #2498: Frog Jump II

Problem Statement:
You are given a 0-indexed integer array `stones` of size `n` where `stones[i]` represents the position of the ith stone along a river. A frog is initially on the first stone and wants to cross the river to the last stone. However, it can only jump in the following way:

1. The frog can jump to the next stone or skip one stone and jump to the stone after that.
2. The cost of a jump between stones i and j is the absolute difference between their positions, i.e., |stones[i] - stones[j]|.

The frog wants to minimize the maximum cost of a jump across the river. Return the minimum possible value of this maximum cost.

Constraints:
- `2 <= stones.length <= 10^5`
- `0 <= stones[i] <= 10^9`
- `stones` is sorted in strictly increasing order.
"""

# Solution
def minMaxJump(stones):
    """
    Function to calculate the minimum possible value of the maximum cost of a jump.

    :param stones: List[int] - A sorted list of stone positions.
    :return: int - The minimum possible value of the maximum cost of a jump.
    """
    n = len(stones)
    left, right = 0, stones[-1] - stones[0]

    def canCross(max_jump):
        """
        Helper function to check if the frog can cross the river with the given max_jump.
        """
        last_position = 0
        for i in range(1, n):
            if stones[i] - stones[last_position] > max_jump:
                if i - last_position == 1:
                    return False
                last_position = i - 1
        return True

    while left < right:
        mid = (left + right) // 2
        if canCross(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones1 = [0, 2, 5, 6, 7]
    print(minMaxJump(stones1))  # Expected Output: 3

    # Test Case 2
    stones2 = [0, 3, 9]
    print(minMaxJump(stones2))  # Expected Output: 6

    # Test Case 3
    stones3 = [0, 1, 3, 6, 10]
    print(minMaxJump(stones3))  # Expected Output: 4

    # Test Case 4
    stones4 = [0, 4, 8, 12]
    print(minMaxJump(stones4))  # Expected Output: 4

    # Test Case 5
    stones5 = [0, 1, 2, 3, 4, 5]
    print(minMaxJump(stones5))  # Expected Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max_jump)), where max_jump is the difference between the first and last stone.
- The `canCross` function iterates through the stones array, which takes O(n).
- Therefore, the overall time complexity is O(n * log(max_jump)).

Space Complexity:
- The algorithm uses O(1) additional space, as it only uses a few variables for computation.

Topic: Binary Search
"""