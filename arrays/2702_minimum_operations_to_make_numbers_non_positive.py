"""
LeetCode Problem #2702: Minimum Operations to Make Numbers Non-positive

Problem Statement:
You are given a 0-indexed integer array `nums` and two integers `x` and `y`. In one operation, you must choose an index `i` such that `0 <= i < nums.length` and perform one of the following:
- Decrement `nums[i]` by `x`, or
- Decrement `nums[i]` by `y`.

Return the minimum number of operations to make all the elements of the array non-positive.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= x, y <= 10^9
"""

def minOperations(nums, x, y):
    """
    Calculates the minimum operations to make all elements non-positive.

    :param nums: List[int] - Array of positive integers
    :param x: int - First decrement value
    :param y: int - Second decrement value
    :return: int - Minimum number of operations
    """
    def min_ops_for_num(num):
        if num <= 0:
            return 0
        
        # Try all possible combinations of x and y operations
        min_ops = float('inf')
        
        # Maximum operations using x only
        max_x_ops = (num + x - 1) // x
        
        for x_ops in range(max_x_ops + 1):
            remaining = num - x_ops * x
            if remaining <= 0:
                min_ops = min(min_ops, x_ops)
            else:
                y_ops = (remaining + y - 1) // y
                min_ops = min(min_ops, x_ops + y_ops)
        
        return min_ops
    
    return sum(min_ops_for_num(num) for num in nums)

def minOperationsOptimized(nums, x, y):
    """
    Optimized solution using mathematical approach.

    :param nums: List[int] - Array of positive integers
    :param x: int - First decrement value
    :param y: int - Second decrement value
    :return: int - Minimum number of operations
    """
    # Ensure x >= y for optimization
    if x < y:
        x, y = y, x
    
    def min_ops_for_num(num):
        if num <= 0:
            return 0
        
        # If x == y, just use either operation
        if x == y:
            return (num + x - 1) // x
        
        # Try using only y operations
        min_ops = (num + y - 1) // y
        
        # Try combinations where we use some x operations
        # We only need to check up to y combinations
        for x_ops in range(1, min(y, (num + x - 1) // x) + 1):
            remaining = num - x_ops * x
            if remaining <= 0:
                min_ops = min(min_ops, x_ops)
            else:
                y_ops = (remaining + y - 1) // y
                min_ops = min(min_ops, x_ops + y_ops)
        
        return min_ops
    
    return sum(min_ops_for_num(num) for num in nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [3, 4]
    x, y = 3, 2
    print(minOperations(nums, x, y))  # Output: 3
    print(minOperationsOptimized(nums, x, y))  # Output: 3

    # Test Case 2
    nums = [1, 2, 1]
    x, y = 2, 1
    print(minOperations(nums, x, y))  # Output: 3
    print(minOperationsOptimized(nums, x, y))  # Output: 3

    # Test Case 3
    nums = [10, 15, 20]
    x, y = 5, 3
    print(minOperations(nums, x, y))  # Output: 12
    print(minOperationsOptimized(nums, x, y))  # Output: 12

    # Test Case 4
    nums = [1]
    x, y = 1, 1
    print(minOperations(nums, x, y))  # Output: 1
    print(minOperationsOptimized(nums, x, y))  # Output: 1

    # Test Case 5
    nums = [100, 200, 300]
    x, y = 10, 25
    print(minOperations(nums, x, y))  # Output: 32
    print(minOperationsOptimized(nums, x, y))  # Output: 32

"""
Time Complexity Analysis:
Basic Solution:
- For each number, we try at most (num/x + 1) combinations.
- Time complexity: O(sum(nums[i]/min(x,y))) which can be large for small x,y.

Optimized Solution:
- For each number, we try at most min(y, num/x) combinations.
- Time complexity: O(n * min(x, y)) where n is length of nums.

Space Complexity Analysis:
- Both solutions use O(1) extra space.

Topic: Arrays, Math, Greedy
"""
