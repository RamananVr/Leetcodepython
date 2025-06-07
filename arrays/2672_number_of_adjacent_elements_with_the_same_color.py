"""
LeetCode Question #2672: Number of Adjacent Elements With the Same Color

Problem Statement:
There is a 0-indexed array nums of length n. Initially, all elements are uncolored (has a value of 0).

You are given a 2D integer array queries where queries[i] = [index, color] means:
- Change the color of index to color in the array nums.
- Answer how many adjacent elements have the same color after applying this query.

Note that adjacent elements refer to elements that are next to each other in the array.

Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

Examples:
Example 1:
Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
Output: [0,1,0,1,2]
Explanation:
Initially array = [0,0,0,0]
Query [0,2]: Change nums[0] to 2. Array = [2,0,0,0]. Adjacent pairs with same color: 0.
Query [1,2]: Change nums[1] to 2. Array = [2,2,0,0]. Adjacent pairs with same color: 1 (pair [0,1]).
Query [3,1]: Change nums[3] to 1. Array = [2,2,0,1]. Adjacent pairs with same color: 1.
Query [1,1]: Change nums[1] to 1. Array = [2,1,0,1]. Adjacent pairs with same color: 1.
Query [2,1]: Change nums[2] to 1. Array = [2,1,1,1]. Adjacent pairs with same color: 2 (pairs [1,2] and [2,3]).

Example 2:
Input: n = 1, queries = [[0,100000]]
Output: [0]
Explanation: Initially array = [0]
Query [0,100000]: Change nums[0] to 100000. Array = [100000]. Adjacent pairs with same color: 0.

Constraints:
- 1 <= n <= 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 0 <= index < n
- 1 <= color <= 10^5
"""

from typing import List

def colorTheArray(n: int, queries: List[List[int]]) -> List[int]:
    """
    Process queries and count adjacent elements with same color efficiently.
    
    Time: O(q) where q is the number of queries
    Space: O(n) for the array
    """
    nums = [0] * n
    adjacent_count = 0
    result = []
    
    for index, color in queries:
        old_color = nums[index]
        
        # Remove contribution of old color
        if index > 0 and nums[index - 1] != 0 and nums[index - 1] == old_color:
            adjacent_count -= 1
        if index < n - 1 and nums[index + 1] != 0 and nums[index + 1] == old_color:
            adjacent_count -= 1
        
        # Update the color
        nums[index] = color
        
        # Add contribution of new color
        if index > 0 and nums[index - 1] != 0 and nums[index - 1] == color:
            adjacent_count += 1
        if index < n - 1 and nums[index + 1] != 0 and nums[index + 1] == color:
            adjacent_count += 1
        
        result.append(adjacent_count)
    
    return result

def colorTheArrayBruteForce(n: int, queries: List[List[int]]) -> List[int]:
    """
    Brute force approach - recount adjacent pairs after each query.
    
    Time: O(q * n) where q is queries and n is array size
    Space: O(n)
    """
    nums = [0] * n
    result = []
    
    for index, color in queries:
        nums[index] = color
        
        # Count adjacent pairs with same color
        count = 0
        for i in range(n - 1):
            if nums[i] != 0 and nums[i + 1] != 0 and nums[i] == nums[i + 1]:
                count += 1
        
        result.append(count)
    
    return result

def colorTheArrayWithValidation(n: int, queries: List[List[int]]) -> List[int]:
    """
    Enhanced version with input validation and debugging.
    
    Time: O(q)
    Space: O(n)
    """
    if n <= 0:
        return []
    
    nums = [0] * n
    adjacent_count = 0
    result = []
    
    for query_idx, (index, color) in enumerate(queries):
        if not (0 <= index < n):
            continue  # Skip invalid indices
        if color <= 0:
            continue  # Skip invalid colors
        
        old_color = nums[index]
        
        # Calculate change in adjacent count
        change = 0
        
        # Check left neighbor
        if index > 0 and nums[index - 1] != 0:
            if nums[index - 1] == old_color:
                change -= 1  # Remove old matching pair
            if nums[index - 1] == color:
                change += 1  # Add new matching pair
        
        # Check right neighbor
        if index < n - 1 and nums[index + 1] != 0:
            if nums[index + 1] == old_color:
                change -= 1  # Remove old matching pair
            if nums[index + 1] == color:
                change += 1  # Add new matching pair
        
        # Update
        nums[index] = color
        adjacent_count += change
        result.append(adjacent_count)
    
    return result

def colorTheArrayDebug(n: int, queries: List[List[int]]) -> List[int]:
    """
    Debug version that shows step-by-step process.
    """
    nums = [0] * n
    adjacent_count = 0
    result = []
    
    print(f"Initial array: {nums}")
    
    for i, (index, color) in enumerate(queries):
        old_color = nums[index]
        print(f"\nQuery {i}: Change nums[{index}] from {old_color} to {color}")
        
        # Calculate change
        change = 0
        
        if index > 0 and nums[index - 1] != 0:
            if nums[index - 1] == old_color:
                change -= 1
                print(f"  Remove pair: nums[{index-1}]({nums[index-1]}) == nums[{index}]({old_color})")
            if nums[index - 1] == color:
                change += 1
                print(f"  Add pair: nums[{index-1}]({nums[index-1]}) == nums[{index}]({color})")
        
        if index < n - 1 and nums[index + 1] != 0:
            if nums[index + 1] == old_color:
                change -= 1
                print(f"  Remove pair: nums[{index}]({old_color}) == nums[{index+1}]({nums[index+1]})")
            if nums[index + 1] == color:
                change += 1
                print(f"  Add pair: nums[{index}]({color}) == nums[{index+1}]({nums[index+1]})")
        
        nums[index] = color
        adjacent_count += change
        result.append(adjacent_count)
        
        print(f"  Array after: {nums}")
        print(f"  Adjacent count: {adjacent_count}")
    
    return result

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (4, [[0,2],[1,2],[3,1],[1,1],[2,1]], [0,1,0,1,2]),
        (1, [[0,100000]], [0]),
        (3, [[0,1],[1,1],[2,1]], [0,1,2]),
        (5, [[2,3],[4,3],[1,2],[0,2]], [0,0,0,1]),
    ]
    
    print("Testing optimized approach:")
    for n, queries, expected in test_cases:
        result = colorTheArray(n, queries)
        print(f"n={n}, queries={queries}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing brute force approach:")
    for n, queries, expected in test_cases:
        result = colorTheArrayBruteForce(n, queries)
        print(f"n={n}, queries={queries}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    # Debug the first test case
    print("Debug trace for first test case:")
    colorTheArrayDebug(4, [[0,2],[1,2],[3,1],[1,1],[2,1]])

"""
Time and Space Complexity Analysis:

Optimized Approach:
Time Complexity: O(q) where q is the number of queries
Space Complexity: O(n) for the array storage

Brute Force Approach:
Time Complexity: O(q * n) - for each query, we scan the entire array
Space Complexity: O(n) for the array storage

Key Insights:
1. The key optimization is to track only the change in adjacent count
2. When changing a position, only its immediate neighbors matter
3. We need to remove old contributions and add new ones
4. Uncolored elements (value 0) don't form adjacent pairs
5. The problem reduces to efficiently maintaining a running count

Topic: Arrays, Simulation, Dynamic Updates
"""
