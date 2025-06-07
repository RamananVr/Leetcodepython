"""
LeetCode Question #2679: Sum in a Matrix

Problem Statement:
You are given a 0-indexed 2D integer array nums. Initially, your score is 0. Perform the following operations until the matrix becomes empty:

1. From each row in the matrix, select the largest number and remove it. In the case of a tie, it does not matter which one you remove.
2. Add the largest of the selected numbers to your score.

Return the final score.

Examples:
Example 1:
Input: nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
Output: 15
Explanation: In the first operation, we select the largest value from each row: [7, 6, 6, 3]. The largest among these is 7.
In the second operation, we select [2, 4, 5, 2]. The largest is 5.
In the third operation, we select [1, 2, 3, 1]. The largest is 3.
The final score is 7 + 5 + 3 = 15.

Example 2:
Input: nums = [[1]]
Output: 1
Explanation: We select 1 and the score becomes 1.

Constraints:
- 1 <= nums.length <= 300
- 1 <= nums[i].length <= 500
- 0 <= nums[i][j] <= 10^3
"""

from typing import List
import heapq

def matrixSum(nums: List[List[int]]) -> int:
    """
    Calculate matrix sum by selecting largest from each row in each round.
    
    Time: O(m * n * log n) where m is rows, n is max columns
    Space: O(1) if we can modify input, O(m * n) for sorting
    """
    # Sort each row in descending order for efficient largest element removal
    for row in nums:
        row.sort(reverse=True)
    
    total_score = 0
    num_cols = len(nums[0]) if nums else 0
    
    # Process each column (round)
    for col in range(num_cols):
        round_max = 0
        
        # Find maximum element among all rows at current column position
        for row in range(len(nums)):
            if col < len(nums[row]):
                round_max = max(round_max, nums[row][col])
        
        total_score += round_max
    
    return total_score

def matrixSumHeap(nums: List[List[int]]) -> int:
    """
    Using max heaps for each row to efficiently get largest elements.
    
    Time: O(m * n * log n) for heap operations
    Space: O(m * n) for heap storage
    """
    if not nums or not nums[0]:
        return 0
    
    # Convert each row to a max heap (negate values for min heap)
    heaps = []
    for row in nums:
        heap = [-val for val in row]  # Negate for max heap using min heap
        heapq.heapify(heap)
        heaps.append(heap)
    
    total_score = 0
    
    # Continue until all heaps are empty
    while any(heaps):
        round_max = 0
        
        # Get largest element from each non-empty heap
        for i, heap in enumerate(heaps):
            if heap:
                largest = -heapq.heappop(heap)  # Negate back to get original value
                round_max = max(round_max, largest)
        
        total_score += round_max
    
    return total_score

def matrixSumSimulation(nums: List[List[int]]) -> int:
    """
    Direct simulation approach - actually remove elements.
    
    Time: O(m * n^2) due to element removal
    Space: O(m * n) for copying the matrix
    """
    # Create a copy to avoid modifying the original
    matrix = [row[:] for row in nums]
    total_score = 0
    
    while any(row for row in matrix if row):  # While any row is non-empty
        round_selections = []
        
        # Select largest from each non-empty row
        for row in matrix:
            if row:
                max_val = max(row)
                row.remove(max_val)  # Remove first occurrence
                round_selections.append(max_val)
        
        # Add the largest selection to score
        if round_selections:
            total_score += max(round_selections)
    
    return total_score

def matrixSumOptimized(nums: List[List[int]]) -> int:
    """
    Optimized approach using column-wise processing after sorting.
    
    Time: O(m * n * log n) for sorting
    Space: O(1) if modifying input is allowed
    """
    if not nums:
        return 0
    
    # Sort each row in descending order
    for row in nums:
        row.sort(reverse=True)
    
    total_score = 0
    max_cols = max(len(row) for row in nums)
    
    # Process each column position
    for col in range(max_cols):
        column_max = 0
        
        for row in nums:
            if col < len(row):
                column_max = max(column_max, row[col])
        
        total_score += column_max
    
    return total_score

def matrixSumWithTracking(nums: List[List[int]]) -> List[int]:
    """
    Return the score along with round-by-round breakdown.
    
    Time: O(m * n * log n)
    Space: O(m * n)
    """
    # Sort each row in descending order
    sorted_matrix = [sorted(row, reverse=True) for row in nums]
    
    round_scores = []
    max_cols = max(len(row) for row in sorted_matrix) if sorted_matrix else 0
    
    for col in range(max_cols):
        round_max = 0
        round_selections = []
        
        for row in sorted_matrix:
            if col < len(row):
                round_selections.append(row[col])
                round_max = max(round_max, row[col])
        
        round_scores.append({
            'round': col + 1,
            'selections': round_selections,
            'max': round_max
        })
    
    total_score = sum(round_info['max'] for round_info in round_scores)
    return total_score, round_scores

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]], 15),
        ([[1]], 1),
        ([[1, 2, 3], [4, 5, 6]], 11),  # Max selections: [3,6] -> 6, [2,5] -> 5, [1,4] -> 4. Total: 15
        ([[5, 1], [3, 4], [2, 6]], 11), # Round 1: [5,4,6] -> 6, Round 2: [1,3,2] -> 3. Total: 9
        ([], 0),
        ([[0, 0], [0, 0]], 0),
    ]
    
    print("Testing main approach:")
    for nums, expected in test_cases:
        result = matrixSum([row[:] for row in nums])  # Copy to avoid modification
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing heap approach:")
    for nums, expected in test_cases:
        result = matrixSumHeap([row[:] for row in nums])
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing simulation approach:")
    for nums, expected in test_cases:
        result = matrixSumSimulation([row[:] for row in nums])
        print(f"nums = {nums}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    # Detailed breakdown for first test case
    print("Detailed breakdown for [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]:")
    nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
    total, rounds = matrixSumWithTracking(nums)
    print(f"Total score: {total}")
    for round_info in rounds:
        print(f"Round {round_info['round']}: selections {round_info['selections']}, max = {round_info['max']}")

"""
Time and Space Complexity Analysis:

Main Approach (Sorting):
Time Complexity: O(m * n * log n) where m is rows, n is max columns per row
Space Complexity: O(1) if input modification allowed, O(m * n) for sorting

Heap Approach:
Time Complexity: O(m * n * log n) for heap operations
Space Complexity: O(m * n) for storing heaps

Simulation Approach:
Time Complexity: O(m * n^2) due to element removal from lists
Space Complexity: O(m * n) for matrix copy

Optimized Approach:
Time Complexity: O(m * n * log n) for sorting rows
Space Complexity: O(1) additional space

Key Insights:
1. The problem can be solved efficiently by sorting each row first
2. After sorting, we can process column by column to find round maximums
3. Heap approach provides an alternative but has similar complexity
4. The key insight is that order of selection within each row doesn't matter
5. We only need the largest available element from each row in each round

Algorithm Steps:
1. Sort each row in descending order
2. For each column position (round):
   - Find maximum element across all rows at that position
   - Add to total score
3. Return total score

Topic: Arrays, Matrix, Sorting, Heap, Greedy
"""
