"""
LeetCode Problem 2770: Maximum Number of Jumps to Reach the Last Index

You are given a 0-indexed array nums of n integers and an integer target.

You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:
- 0 <= i < j < n
- -target <= nums[j] - nums[i] <= target

Return the maximum number of jumps you can make to reach the last index. If there is no way to reach the last index, return -1.

Constraints:
- 2 <= nums.length <= 1000
- -10^9 <= nums[i] <= 10^9
- 0 <= target <= 2 * 10^9

Example 1:
Input: nums = [1,3,6,4,1,2], target = 2
Output: 3
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.

Example 2:
Input: nums = [1,3,6,4,1,2], target = 3
Output: 5
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.

Example 3:
Input: nums = [1,3,6,4,1,2], target = 0
Output: -1
Explanation: You can only jump to indexes that have the same value as the current index.

Topics: Array, Dynamic Programming
"""

class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        """
        Approach 1: Dynamic Programming
        
        Use DP where dp[i] represents the maximum number of jumps to reach index i.
        For each position, try to jump to all valid future positions.
        
        Time: O(n^2) - for each position, check all future positions
        Space: O(n) - DP array
        """
        n = len(nums)
        # dp[i] = maximum jumps to reach index i, -1 if impossible
        dp = [-1] * n
        dp[0] = 0  # Starting position requires 0 jumps
        
        for i in range(n):
            if dp[i] == -1:  # Cannot reach this position
                continue
            
            # Try jumping to all valid future positions
            for j in range(i + 1, n):
                diff = abs(nums[j] - nums[i])
                if diff <= target:
                    # Can jump from i to j
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n - 1]
    
    def maximumJumps_bfs(self, nums: list[int], target: int) -> int:
        """
        Approach 2: BFS to find maximum path
        
        Use BFS to explore all possible paths and track maximum jumps.
        
        Time: O(n^2) in worst case
        Space: O(n) for queue and visited tracking
        """
        from collections import deque
        
        n = len(nums)
        # (index, jumps_count)
        queue = deque([(0, 0)])
        max_jumps = [-1] * n
        max_jumps[0] = 0
        
        while queue:
            curr_idx, jumps = queue.popleft()
            
            # Skip if we've found a better path to this position
            if jumps < max_jumps[curr_idx]:
                continue
            
            # Try jumping to all valid next positions
            for next_idx in range(curr_idx + 1, n):
                diff = abs(nums[next_idx] - nums[curr_idx])
                if diff <= target:
                    new_jumps = jumps + 1
                    if new_jumps > max_jumps[next_idx]:
                        max_jumps[next_idx] = new_jumps
                        queue.append((next_idx, new_jumps))
        
        return max_jumps[n - 1]
    
    def maximumJumps_dfs_memo(self, nums: list[int], target: int) -> int:
        """
        Approach 3: DFS with memoization
        
        Use DFS to explore paths from each position with memoization.
        
        Time: O(n^2)
        Space: O(n) for memoization and recursion stack
        """
        n = len(nums)
        memo = {}
        
        def dfs(index):
            """Return maximum jumps from index to last index."""
            if index == n - 1:
                return 0
            
            if index in memo:
                return memo[index]
            
            max_jumps = -1
            
            # Try jumping to all valid future positions
            for next_idx in range(index + 1, n):
                diff = abs(nums[next_idx] - nums[index])
                if diff <= target:
                    jumps_from_next = dfs(next_idx)
                    if jumps_from_next != -1:
                        max_jumps = max(max_jumps, 1 + jumps_from_next)
            
            memo[index] = max_jumps
            return max_jumps
        
        return dfs(0)
    
    def maximumJumps_greedy_wrong(self, nums: list[int], target: int) -> int:
        """
        Approach 4: Greedy approach (INCORRECT - for comparison)
        
        This greedy approach is wrong because it doesn't guarantee maximum jumps.
        Always jumping to the nearest valid position might miss better paths.
        
        Time: O(n^2)
        Space: O(1)
        """
        n = len(nums)
        current_idx = 0
        jumps = 0
        
        while current_idx < n - 1:
            next_idx = -1
            
            # Find the nearest valid position to jump to
            for j in range(current_idx + 1, n):
                diff = abs(nums[j] - nums[current_idx])
                if diff <= target:
                    next_idx = j
                    break
            
            if next_idx == -1:
                return -1  # Cannot make progress
            
            current_idx = next_idx
            jumps += 1
        
        return jumps

def test_maximum_jumps():
    """Test the maximum jumps solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.maximumJumps([1, 3, 6, 4, 1, 2], 2) == 3
    
    # Test case 2: Larger target
    assert solution.maximumJumps([1, 3, 6, 4, 1, 2], 3) == 5
    
    # Test case 3: Impossible case
    assert solution.maximumJumps([1, 3, 6, 4, 1, 2], 0) == -1
    
    # Test case 4: Two elements
    assert solution.maximumJumps([1, 2], 1) == 1
    
    # Test case 5: Two elements, impossible
    assert solution.maximumJumps([1, 5], 3) == -1
    
    # Test case 6: All same values
    assert solution.maximumJumps([3, 3, 3, 3], 0) == 3
    
    # Test case 7: Strictly increasing with large target
    assert solution.maximumJumps([1, 2, 3, 4, 5], 10) == 4
    
    # Test case 8: Complex case
    assert solution.maximumJumps([1, 0, 2, 3, 0, 4], 2) == 4
    
    # Compare different approaches
    test_cases = [
        ([1, 3, 6, 4, 1, 2], 2),
        ([1, 3, 6, 4, 1, 2], 3),
        ([1, 3, 6, 4, 1, 2], 0),
        ([1, 2], 1),
        ([1, 5], 3),
        ([3, 3, 3, 3], 0),
        ([1, 2, 3, 4, 5], 10),
        ([1, 0, 2, 3, 0, 4], 2)
    ]
    
    for nums, target in test_cases:
        result1 = solution.maximumJumps(nums, target)
        result2 = solution.maximumJumps_bfs(nums, target)
        result3 = solution.maximumJumps_dfs_memo(nums, target)
        assert result1 == result2 == result3, f"Mismatch for {nums}, {target}: {result1}, {result2}, {result3}"
    
    print("All maximum jumps tests passed!")

if __name__ == "__main__":
    test_maximum_jumps()
