"""
LeetCode Problem #2664: Minimum Moves to Make Array Complementary

Problem Statement:
You are given an integer array `nums` of even length `n` and an integer `limit`. 
In one move, you can replace any integer in `nums` with another integer between `1` and `limit`, inclusive.

The array `nums` is complementary if for all indices `i` (0 <= i < n / 2), 
`nums[i] + nums[n - i - 1]` is the same. Return the minimum number of moves required to make `nums` complementary.

Constraints:
- `n == nums.length`
- `2 <= n <= 10^5`
- `n` is even.
- `1 <= nums[i] <= limit`

"""

# Solution
def minMoves(nums, limit):
    """
    Calculate the minimum number of moves to make the array complementary.

    :param nums: List[int] - The input array of integers.
    :param limit: int - The maximum value that any integer in nums can take.
    :return: int - The minimum number of moves required.
    """
    n = len(nums)
    delta = [0] * (2 * limit + 2)

    for i in range(n // 2):
        a, b = nums[i], nums[n - i - 1]
        delta[2] += 2
        delta[min(a, b) + 1] -= 1
        delta[a + b] -= 1
        delta[a + b + 1] += 1
        delta[max(a, b) + limit + 1] += 1

    moves = 2 * n
    current_moves = 0
    for x in range(2, 2 * limit + 1):
        current_moves += delta[x]
        moves = min(moves, current_moves)

    return moves


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 1]
    limit1 = 2
    print(minMoves(nums1, limit1))  # Expected Output: 0

    # Test Case 2
    nums2 = [1, 2, 1, 2]
    limit2 = 2
    print(minMoves(nums2, limit2))  # Expected Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    limit3 = 4
    print(minMoves(nums3, limit3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    limit4 = 10
    print(minMoves(nums4, limit4))  # Expected Output: 0


# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once to calculate the delta array, which takes O(n) time.
- Then, it iterates through the range [2, 2 * limit + 1] to calculate the minimum moves, which takes O(limit) time.
- Overall, the time complexity is O(n + limit).

Space Complexity:
- The delta array has a size of O(2 * limit + 2), which is the dominant space usage.
- Therefore, the space complexity is O(limit).
"""

# Topic: Arrays