"""
LeetCode Question #42: Trapping Rain Water

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map (height) is represented as [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

def trap(height):
    """
    Calculate the amount of trapped rainwater given an elevation map.

    :param height: List[int] - List of non-negative integers representing the elevation map.
    :return: int - Total amount of trapped rainwater.
    """
    if not height or len(height) < 3:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Fill right_max array
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Calculate trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height1))  # Output: 6

    # Test Case 2
    height2 = [4,2,0,3,2,5]
    print(trap(height2))  # Output: 9

    # Test Case 3
    height3 = [0,0,0,0]
    print(trap(height3))  # Output: 0

    # Test Case 4
    height4 = [1,2,3,4,5]
    print(trap(height4))  # Output: 0

    # Test Case 5
    height5 = [5,4,3,2,1]
    print(trap(height5))  # Output: 0

"""
Topic: Arrays
"""