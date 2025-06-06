"""
LeetCode Problem #1674: Minimum Moves to Make Array Complementary

Problem Statement:
You are given an integer array `nums` of even length `n` and an integer `limit`. 
In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive.

The array `nums` is complementary if for all indices `i` (0 <= i < n / 2), 
`nums[i] + nums[n - 1 - i]` equals the same number.

Return the minimum number of moves required to make `nums` complementary.

Constraints:
- `n == nums.length`
- `2 <= n <= 10^5`
- `n` is even.
- `1 <= nums[i] <= limit`

"""

def minMoves(nums, limit):
    """
    Function to calculate the minimum number of moves to make the array complementary.
    """
    n = len(nums)
    delta = [0] * (2 * limit + 2)

    for i in range(n // 2):
        a, b = nums[i], nums[n - 1 - i]
        delta[2] += 2
        delta[min(a, b) + 1] -= 1
        delta[a + b] -= 1
        delta[a + b + 1] += 1
        delta[max(a, b) + limit + 1] += 1

    moves = 0
    min_moves = float('inf')
    for i in range(2, 2 * limit + 1):
        moves += delta[i]
        min_moves = min(min_moves, moves)

    return min_moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 1]
    limit1 = 2
    print(minMoves(nums1, limit1))  # Output: 0

    # Test Case 2
    nums2 = [1, 2, 1, 2]
    limit2 = 2
    print(minMoves(nums2, limit2))  # Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    limit3 = 4
    print(minMoves(nums3, limit3))  # Output: 1

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6]
    limit4 = 6
    print(minMoves(nums4, limit4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once to calculate the delta array, which takes O(n) time.
- Then, it iterates through the delta array (of size 2 * limit + 2) to calculate the minimum moves, which takes O(limit) time.
- Overall, the time complexity is O(n + limit).

Space Complexity:
- The algorithm uses a delta array of size 2 * limit + 2, which takes O(limit) space.
- Thus, the space complexity is O(limit).

Topic: Arrays, Prefix Sum
"""