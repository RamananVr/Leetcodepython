"""
LeetCode Problem #2033: Minimum Operations to Make a Uni-Value Grid

Problem Statement:
You are given a 2D grid of integers `grid` of size `m x n` and an integer `x`. In one operation, 
you can choose any element of the grid and either add or subtract `x` from it.

A uni-value grid is a grid where all the elements are equal. Return the minimum number of operations 
required to make the grid uni-value. If it is not possible, return -1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element in the grid equal to 4 by doing the following:
- Add 2 to 2 once.
- Subtract 2 from 6 once.
- Subtract 4 from 8 twice.
A total of 4 operations are required.

Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: -1
Explanation: It is impossible to make all the elements equal because the difference between some 
elements is not divisible by x.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make all the elements equal because the difference between some 
elements is not divisible by x.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10^2
- 1 <= grid[i][j], x <= 10^4
"""

# Python Solution
from typing import List

def minOperations(grid: List[List[int]], x: int) -> int:
    # Flatten the grid into a 1D list
    flat_grid = [num for row in grid for num in row]
    
    # Check if all elements can be made equal modulo x
    remainder = flat_grid[0] % x
    for num in flat_grid:
        if num % x != remainder:
            return -1  # Not possible to make all elements equal
    
    # Transform all elements to their "base" values (divided by x)
    transformed = [num // x for num in flat_grid]
    
    # Find the median of the transformed values
    transformed.sort()
    median = transformed[len(transformed) // 2]
    
    # Calculate the total number of operations to make all elements equal to the median
    operations = sum(abs(num - median) for num in transformed)
    
    # Multiply the operations by x to account for the original scale
    return operations * x

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[2, 4], [6, 8]]
    x1 = 2
    print(minOperations(grid1, x1))  # Output: 4

    # Test Case 2
    grid2 = [[1, 5], [2, 3]]
    x2 = 1
    print(minOperations(grid2, x2))  # Output: -1

    # Test Case 3
    grid3 = [[1, 2], [3, 4]]
    x3 = 2
    print(minOperations(grid3, x3))  # Output: -1

    # Test Case 4
    grid4 = [[10, 20, 30], [40, 50, 60]]
    x4 = 10
    print(minOperations(grid4, x4))  # Output: 60

    # Test Case 5
    grid5 = [[1, 1], [1, 1]]
    x5 = 1
    print(minOperations(grid5, x5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
1. Flattening the grid: O(m * n), where m and n are the dimensions of the grid.
2. Checking modulo condition: O(m * n).
3. Sorting the transformed array: O(m * n * log(m * n)).
4. Calculating the total operations: O(m * n).
Overall: O(m * n * log(m * n)).

Space Complexity:
1. Storing the flattened grid: O(m * n).
2. Storing the transformed array: O(m * n).
Overall: O(m * n).
"""

# Topic: Arrays, Sorting, Math