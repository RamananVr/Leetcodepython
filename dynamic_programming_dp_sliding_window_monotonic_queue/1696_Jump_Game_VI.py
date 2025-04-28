"""
LeetCode Problem #1696: Jump Game VI

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump to any index `i` in the range `[1, min(n-1, index + k)]` inclusive. 
You cannot jump outside of the array. You want to reach the last index of the array (index `n-1`).

Your score is the sum of `nums` at each index you visit. Return the maximum score you can achieve.

Constraints:
- `1 <= nums.length, k <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
"""

from collections import deque

def maxResult(nums, k):
    """
    Function to calculate the maximum score to reach the last index of the array.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum jump distance.
    
    Returns:
    int: The maximum score achievable.
    """
    n = len(nums)
    # Deque to store indices of the array
    dq = deque()
    # Array to store the maximum score at each index
    dp = [0] * n
    dp[0] = nums[0]
    dq.append(0)
    
    for i in range(1, n):
        # Remove indices from the deque that are out of the current window
        while dq and dq[0] < i - k:
            dq.popleft()
        
        # Update dp[i] with the maximum score achievable at index i
        dp[i] = nums[i] + dp[dq[0]]
        
        # Maintain the deque in decreasing order of dp values
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, -1, -2, 4, -7, 3]
    k1 = 2
    print(maxResult(nums1, k1))  # Expected Output: 7

    # Test Case 2
    nums2 = [10, -5, -2, 4, 0, 3]
    k2 = 3
    print(maxResult(nums2, k2))  # Expected Output: 17

    # Test Case 3
    nums3 = [1, -5, -20, 4, -1, 3, -6, -3]
    k3 = 2
    print(maxResult(nums3, k3))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, making it O(n).
- For each index, we perform deque operations (append, pop, popleft), which are O(1) on average.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The `dp` array takes O(n) space.
- The deque can store up to k elements at any time, which is O(k) space.
- Therefore, the overall space complexity is O(n).

Topic: Dynamic Programming (DP) + Sliding Window / Monotonic Queue
"""