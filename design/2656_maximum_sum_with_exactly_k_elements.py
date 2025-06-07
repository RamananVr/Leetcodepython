"""
LeetCode Question #2656: Maximum Sum With Exactly K Elements

Problem Statement:
You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

1. Select an element m from nums.
2. Remove it from the array.
3. Add m + 1 to the array.
4. Increase your score by m.

Return the maximum score you can achieve after performing this operation exactly k times.

Examples:
Example 1:
Input: nums = [1,2,3,4,5], k = 3
Output: 18
Explanation: We need to choose from nums 3 times.
For the first iteration, we choose 5. Then, nums becomes [1,2,3,4,6] and our score is 5.
For the second iteration, we choose 6. Then, nums becomes [1,2,3,4,7] and our score is 5 + 6 = 11.
For the third iteration, we choose 7. Then, nums becomes [1,2,3,4,8] and our score is 5 + 6 + 7 = 18.

Example 2:
Input: nums = [5,5,5], k = 2
Output: 11
Explanation: We need to choose from nums 2 times.
For the first iteration, we choose 5. Then, nums becomes [5,5,6] and our score is 5.
For the second iteration, we choose 6. Then, nums becomes [5,5,7] and our score is 5 + 6 = 11.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100
"""

from typing import List
import heapq

def maximizeSum(nums: List[int], k: int) -> int:
    """
    Maximize sum by always picking the maximum element.
    
    Strategy: Always pick the maximum element, increment it, and repeat.
    This is optimal because we want to maximize each addition.
    """
    # Find the maximum element
    max_val = max(nums)
    
    # The optimal strategy is to keep picking the maximum element
    # and incrementing it k times
    total_score = 0
    
    for i in range(k):
        total_score += max_val + i
    
    return total_score

def maximizeSumHeap(nums: List[int], k: int) -> int:
    """
    Alternative implementation using max heap.
    """
    # Create max heap (negate values for min heap)
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    total_score = 0
    
    for _ in range(k):
        # Get maximum element
        max_val = -heapq.heappop(max_heap)
        total_score += max_val
        
        # Add incremented value back to heap
        heapq.heappush(max_heap, -(max_val + 1))
    
    return total_score

def maximizeSumSimulation(nums: List[int], k: int) -> int:
    """
    Simulation approach - actually modify the array.
    """
    nums = nums.copy()  # Don't modify original array
    total_score = 0
    
    for _ in range(k):
        # Find maximum element and its index
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        # Add to score
        total_score += max_val
        
        # Remove max element and add incremented value
        nums[max_idx] = max_val + 1
    
    return total_score

def maximizeSumMath(nums: List[int], k: int) -> int:
    """
    Mathematical approach using arithmetic sequence sum.
    """
    max_val = max(nums)
    
    # We'll pick max_val, max_val+1, max_val+2, ..., max_val+k-1
    # This is an arithmetic sequence with first term = max_val, n = k, d = 1
    # Sum = n/2 * (2*a + (n-1)*d) = k/2 * (2*max_val + k-1)
    
    return k * max_val + k * (k - 1) // 2

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 18),
        ([5, 5, 5], 2, 11),
        ([1], 5, 15),  # 1 + 2 + 3 + 4 + 5 = 15
        ([10], 1, 10),
        ([1, 2], 4, 14),  # 2 + 3 + 4 + 5 = 14
        ([100], 3, 303)  # 100 + 101 + 102 = 303
    ]
    
    print("Testing optimal approach:")
    for nums, k, expected in test_cases:
        result = maximizeSum(nums, k)
        print(f"maximizeSum({nums}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting heap approach:")
    for nums, k, expected in test_cases:
        result = maximizeSumHeap(nums, k)
        print(f"maximizeSumHeap({nums}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting simulation approach:")
    for nums, k, expected in test_cases:
        result = maximizeSumSimulation(nums, k)
        print(f"maximizeSumSimulation({nums}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting mathematical approach:")
    for nums, k, expected in test_cases:
        result = maximizeSumMath(nums, k)
        print(f"maximizeSumMath({nums}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Optimal Approach:
Time Complexity: O(n + k) where n is length of nums
- O(n) to find maximum element
- O(k) to calculate sum
Space Complexity: O(1) - only using constant extra space

Heap Approach:
Time Complexity: O(n + k log n)
- O(n) to heapify
- O(k log n) for k heap operations
Space Complexity: O(n) - heap storage

Simulation Approach:
Time Complexity: O(k * n)
- O(n) to find max in each of k iterations
Space Complexity: O(n) - copy of nums array

Mathematical Approach:
Time Complexity: O(n) - only to find maximum element
Space Complexity: O(1) - only using constant extra space

Key Insight:
The optimal strategy is always to pick the maximum element because:
1. We want to maximize each addition to the score
2. After picking max and incrementing it, it remains the maximum
3. This leads to an arithmetic sequence: max, max+1, max+2, ..., max+k-1

Topic: Greedy, Heap, Math, Arrays
"""
