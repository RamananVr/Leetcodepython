"""
LeetCode Problem #1691: Maximum Height by Stacking Cuboids

Problem Statement:
Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [width, depth, height], 
you can place cuboid i on cuboid j if and only if width[i] <= width[j], depth[i] <= depth[j], 
and height[i] <= height[j]. You can rearrange any cuboid's dimensions by rotating it to put 
any side facing up. Return the maximum height of the stacked cuboids.

Constraints:
1. 1 <= cuboids.length <= 100
2. 1 <= width[i], depth[i], height[i] <= 100
"""

def maxHeight(cuboids):
    """
    Function to calculate the maximum height by stacking cuboids.
    """
    # Step 1: Normalize each cuboid by sorting its dimensions
    for cuboid in cuboids:
        cuboid.sort()
    
    # Step 2: Sort all cuboids based on their dimensions
    cuboids.sort()
    
    # Step 3: Initialize DP array
    n = len(cuboids)
    dp = [0] * n
    
    # Step 4: Compute the maximum height using DP
    for i in range(n):
        dp[i] = cuboids[i][2]  # Base height is the height of the current cuboid
        for j in range(i):
            if (cuboids[j][0] <= cuboids[i][0] and
                cuboids[j][1] <= cuboids[i][1] and
                cuboids[j][2] <= cuboids[i][2]):
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])
    
    # Step 5: Return the maximum height
    return max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cuboids1 = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
    print(maxHeight(cuboids1))  # Expected Output: 190

    # Test Case 2
    cuboids2 = [[38, 25, 45], [76, 35, 3]]
    print(maxHeight(cuboids2))  # Expected Output: 76

    # Test Case 3
    cuboids3 = [[7, 11, 17], [7, 17, 11], [11, 7, 17]]
    print(maxHeight(cuboids3))  # Expected Output: 34

"""
Time Complexity:
1. Sorting the dimensions of each cuboid: O(n * 3 * log(3)) = O(n), since each cuboid has 3 dimensions.
2. Sorting the cuboids: O(n * log(n)).
3. Nested loops for DP computation: O(n^2).
Overall: O(n^2).

Space Complexity:
1. DP array: O(n).
Overall: O(n).

Topic: Dynamic Programming (DP)
"""