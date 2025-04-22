"""
LeetCode Problem #42: Trapping Rain Water

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

def trap(height):
    """
    Calculate the amount of water that can be trapped after raining.

    :param height: List[int] - List of non-negative integers representing the elevation map.
    :return: int - Total amount of trapped water.
    """
    if not height or len(height) < 3:
        return 0

    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Test Case 1: {trap(height1)}")  # Expected Output: 6

    # Test Case 2
    height2 = [4,2,0,3,2,5]
    print(f"Test Case 2: {trap(height2)}")  # Expected Output: 9

    # Test Case 3
    height3 = [1,0,2]
    print(f"Test Case 3: {trap(height3)}")  # Expected Output: 1

    # Test Case 4
    height4 = [0,0,0,0]
    print(f"Test Case 4: {trap(height4)}")  # Expected Output: 0

    # Test Case 5
    height5 = [3,0,0,2,0,4]
    print(f"Test Case 5: {trap(height5)}")  # Expected Output: 10

# Topic: Arrays