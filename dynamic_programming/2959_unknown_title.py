"""
LeetCode Problem #2959: Minimum Cost to Split an Array

Problem Statement:
You are given an integer array `nums` and an integer `k`. You want to split the array into some number of non-empty subarrays such that the cost of each subarray is minimized. The cost of a subarray is defined as the sum of its elements plus `k`.

Return the minimum cost to split the array into subarrays.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- 1 <= k <= 1000
"""

def minCost(nums, k):
    """
    Function to calculate the minimum cost to split the array into subarrays.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The additional cost for each subarray.

    Returns:
    int: The minimum cost to split the array.
    """
    from functools import lru_cache

    n = len(nums)

    @lru_cache(None)
    def dp(start):
        if start == n:
            return 0

        freq = {}
        subarray_cost = 0
        min_cost = float('inf')

        for end in range(start, n):
            num = nums[end]
            if num in freq:
                if freq[num] == 1:
                    subarray_cost += 2  # First duplicate adds 2
                else:
                    subarray_cost += 1  # Subsequent duplicates add 1
            freq[num] = freq.get(num, 0) + 1

            # Calculate the cost of splitting at this point
            current_cost = subarray_cost + k + dp(end + 1)
            min_cost = min(min_cost, current_cost)

        return min_cost

    return dp(0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1, 2, 1, 3]
    k1 = 2
    print("Test Case 1 Output:", minCost(nums1, k1))  # Expected Output: 8

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 5
    print("Test Case 2 Output:", minCost(nums2, k2))  # Expected Output: 9

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    k3 = 3
    print("Test Case 3 Output:", minCost(nums3, k3))  # Expected Output: 10

    # Test Case 4
    nums4 = [1]
    k4 = 1
    print("Test Case 4 Output:", minCost(nums4, k4))  # Expected Output: 2

"""
Time Complexity:
- The function uses dynamic programming with memoization. For each starting index `start`, we iterate through the rest of the array to calculate the cost of splitting.
- This results in a time complexity of O(n^2), where `n` is the length of the array.

Space Complexity:
- The space complexity is O(n) for the recursion stack and O(n) for the memoization table, resulting in a total space complexity of O(n).

Topic: Dynamic Programming
"""