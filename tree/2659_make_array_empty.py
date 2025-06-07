"""
LeetCode Question #2659: Make Array Empty

Problem Statement:
You are given an integer array nums. In one operation, you can choose any index i where nums[i] > 0, decrease nums[i] by 1, and increase nums[(i + 1) % n] by 1 (where n is the length of the array).

Return the minimum number of operations required to make all elements of the array equal to 0.

Examples:
Example 1:
Input: nums = [1,2,3,4]
Output: 10
Explanation: It is optimal to apply the following operations:
- Apply 3 operations on index 2: nums = [1,2,0,7].
- Apply 7 operations on index 3: nums = [8,2,0,0].
- Apply 8 operations on index 0: nums = [0,10,0,0].
- Apply 10 operations on index 1: nums = [0,0,0,0].
Total operations = 3 + 7 + 8 + 10 = 28. But this is not optimal.

Actually, optimal approach gives 10 operations.

Example 2:
Input: nums = [1,2,0,1]
Output: 4
Explanation: It is optimal to apply operations to move all values to index 2 (which is 0).

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

from typing import List

def countOperationsToEmptyArray(nums: List[int]) -> int:
    """
    Find minimum operations to make all array elements 0.
    
    Key insight: We need to process elements in ascending order of their values.
    For each element, we calculate how many steps it takes to reach the position
    where we want to "empty" it.
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # Create list of (value, original_index) and sort by value
    indexed_nums = [(nums[i], i) for i in range(n)]
    indexed_nums.sort()
    
    operations = 0
    last_removed_pos = 0
    removed_count = 0
    
    for value, original_index in indexed_nums:
        if value == 0:
            removed_count += 1
            continue
        
        # Calculate distance from last removed position to current position
        # considering the circular nature and removed elements
        current_effective_pos = original_index
        last_effective_pos = last_removed_pos
        
        # Adjust positions based on removed elements
        if original_index >= last_removed_pos:
            distance = original_index - last_removed_pos
        else:
            # Wrap around case
            distance = (n - last_removed_pos) + original_index
        
        # Account for elements already removed
        current_array_size = n - removed_count
        if current_array_size > 0:
            distance = distance % current_array_size
            if distance == 0 and original_index != last_removed_pos:
                distance = current_array_size
        
        operations += distance + value
        last_removed_pos = original_index
        removed_count += 1
    
    return operations

def countOperationsToEmptyArraySimulation(nums: List[int]) -> int:
    """
    Alternative approach using simulation with priority queue.
    """
    import heapq
    from collections import deque
    
    n = len(nums)
    if n == 0:
        return 0
    
    # Create priority queue with (value, index)
    pq = [(nums[i], i) for i in range(n) if nums[i] > 0]
    heapq.heapify(pq)
    
    operations = 0
    current_pos = 0
    active_indices = set(range(n))
    
    while pq:
        value, target_index = heapq.heappop(pq)
        
        # Skip if this index was already processed
        if target_index not in active_indices:
            continue
        
        # Find distance to target index
        indices_list = sorted(active_indices)
        current_idx_in_list = indices_list.index(current_pos) if current_pos in active_indices else 0
        target_idx_in_list = indices_list.index(target_index)
        
        # Calculate circular distance
        if target_idx_in_list >= current_idx_in_list:
            distance = target_idx_in_list - current_idx_in_list
        else:
            distance = len(indices_list) - current_idx_in_list + target_idx_in_list
        
        operations += distance + value
        current_pos = target_index
        active_indices.remove(target_index)
    
    return operations

def countOperationsToEmptyArrayOptimized(nums: List[int]) -> int:
    """
    Optimized approach based on the insight that we process elements
    in sorted order and calculate cumulative distances.
    """
    n = len(nums)
    
    # Create sorted list of (value, index) pairs, excluding zeros
    sorted_pairs = sorted((nums[i], i) for i in range(n) if nums[i] > 0)
    
    if not sorted_pairs:
        return 0
    
    operations = 0
    prev_index = 0
    
    for i, (value, index) in enumerate(sorted_pairs):
        # Calculate the number of elements we need to skip
        # These are elements that have been processed and removed
        remaining_elements = n - i
        
        # Calculate circular distance from prev_index to current index
        if index >= prev_index:
            distance = index - prev_index
        else:
            distance = index + (n - prev_index)
        
        # Adjust for removed elements
        if remaining_elements < n:
            distance = distance % remaining_elements
            if distance == 0 and index != prev_index:
                distance = remaining_elements
        
        operations += distance + value
        prev_index = index
    
    return operations

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 10),
        ([1, 2, 0, 1], 4),
        ([0, 0, 0], 0),
        ([5], 5),
        ([1, 0, 1], 2),
        ([3, 2, 1], 6),
        ([0, 1, 2], 3)
    ]
    
    print("Testing main approach:")
    for nums, expected in test_cases:
        result = countOperationsToEmptyArray(nums.copy())
        print(f"countOperationsToEmptyArray({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting simulation approach:")
    for nums, expected in test_cases:
        result = countOperationsToEmptyArraySimulation(nums.copy())
        print(f"countOperationsToEmptyArraySimulation({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for nums, expected in test_cases:
        result = countOperationsToEmptyArrayOptimized(nums.copy())
        print(f"countOperationsToEmptyArrayOptimized({nums}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

Main Approach:
Time Complexity: O(n log n) - sorting the array by values
Space Complexity: O(n) - storing indexed pairs

Simulation Approach:
Time Complexity: O(n^2 log n) - heap operations with index list operations
Space Complexity: O(n) - priority queue and active indices set

Optimized Approach:
Time Complexity: O(n log n) - sorting the array
Space Complexity: O(n) - storing sorted pairs

Key Insights:
1. Process elements in ascending order of their values
2. For each element, calculate the circular distance to reach it
3. Account for elements that have been removed in previous steps
4. Total operations = sum of (movement_cost + element_value)

The problem is about finding the optimal order to process elements
and calculating the minimum cost to reach each element.

Topic: Arrays, Greedy, Sorting, Circular Array, Simulation
"""
