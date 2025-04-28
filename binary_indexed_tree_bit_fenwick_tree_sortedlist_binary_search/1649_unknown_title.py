"""
LeetCode Problem #1649: Create Sorted Array through Instructions

Problem Statement:
Given an integer array `instructions`, you are asked to create a sorted array from the elements in `instructions`. 
You start with an empty array `nums`. For each element from left to right in `instructions`, insert it into `nums`. 
The cost of each insertion is the minimum of the following:
    - The number of elements currently in `nums` that are strictly less than the element being inserted.
    - The number of elements currently in `nums` that are strictly greater than the element being inserted.

You are to return the total cost of all insertions modulo 10^9 + 7.

Example:
Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = []. Insert 1 with cost min(0, 0) = 0, nums = [1].
Insert 5 with cost min(1, 0) = 0, nums = [1,5].
Insert 6 with cost min(2, 0) = 0, nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, nums = [1,2,5,6]. The total cost is 1.

Constraints:
- 1 <= instructions.length <= 10^5
- 1 <= instructions[i] <= 10^5
"""

# Solution
from sortedcontainers import SortedList

def createSortedArray(instructions):
    MOD = 10**9 + 7
    sorted_list = SortedList()
    cost = 0
    
    for num in instructions:
        left_cost = sorted_list.bisect_left(num)
        right_cost = len(sorted_list) - sorted_list.bisect_right(num)
        cost += min(left_cost, right_cost)
        sorted_list.add(num)
    
    return cost % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    instructions = [1, 5, 6, 2]
    print(createSortedArray(instructions))  # Output: 1

    # Test Case 2
    instructions = [1, 2, 3, 6, 5, 4]
    print(createSortedArray(instructions))  # Output: 3

    # Test Case 3
    instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]
    print(createSortedArray(instructions))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each insertion, we use `SortedList` operations:
  - `bisect_left` and `bisect_right` take O(log n) time.
  - `add` takes O(log n) time.
- Since there are `n` elements in `instructions`, the total time complexity is O(n log n).

Space Complexity:
- The `SortedList` data structure stores all elements in `instructions`, so it requires O(n) space.
"""

# Topic: Binary Indexed Tree (BIT) / Fenwick Tree, SortedList, Binary Search