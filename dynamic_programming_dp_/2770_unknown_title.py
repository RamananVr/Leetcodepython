"""
LeetCode Problem #2770: Maximum Number of Jumps to Reach the Last Index

Problem Statement:
You are given a 0-indexed array `nums` of `n` integers and an integer `target`.

You are initially positioned at the first index of the array. In one jump, you can move from index `i` to index `j` (where `i < j`) if:
- `|nums[j] - nums[i]| <= target`

Return the maximum number of jumps you can make to reach the last index of the array. If it is not possible to reach the last index, return -1.

Constraints:
- `2 <= nums.length <= 1000`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= target <= 10^9`
"""

def maximumJumps(nums, target):
    """
    Function to calculate the maximum number of jumps to reach the last index.

    Args:
    nums (List[int]): The array of integers.
    target (int): The maximum allowed difference between nums[j] and nums[i].

    Returns:
    int: The maximum number of jumps to reach the last index, or -1 if not possible.
    """
    n = len(nums)
    dp = [-1] * n  # dp[i] stores the maximum number of jumps to reach index i
    dp[0] = 0  # Starting point, no jumps needed

    for i in range(n):
        if dp[i] == -1:  # If index i is not reachable, skip it
            continue
        for j in range(i + 1, n):
            if abs(nums[j] - nums[i]) <= target:
                dp[j] = max(dp[j], dp[i] + 1)

    return dp[-1]  # Return the maximum jumps to reach the last index


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 6, 4, 1, 2]
    target1 = 2
    print(maximumJumps(nums1, target1))  # Output: 3

    # Test Case 2
    nums2 = [1, 3, 6, 4, 1, 2]
    target2 = 0
    print(maximumJumps(nums2, target2))  # Output: -1

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    target3 = 10
    print(maximumJumps(nums3, target3))  # Output: 4

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    target4 = 15
    print(maximumJumps(nums4, target4))  # Output: 4

    # Test Case 5
    nums5 = [1, 100, 1, 100, 1]
    target5 = 99
    print(maximumJumps(nums5, target5))  # Output: 4


"""
Time Complexity:
- The outer loop iterates over all indices `i` (O(n)).
- The inner loop iterates over all indices `j` for each `i` (O(n)).
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n) due to the `dp` array.

Topic: Dynamic Programming (DP)
"""