"""
LeetCode Problem #956: Tallest Billboard

Problem Statement:
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, 
and you can choose which steel rods to use or not use. The rods have different lengths, and the billboard must be 
supported by two rods of the same total height.

You are given an array `rods` where `rods[i]` is the length of the i-th rod. You can use the rods in any order. 
You want to maximize the height of the billboard that can be supported by the two rods of the same height. 
If you cannot support the billboard, return 0.

Example 1:
Input: rods = [1,2,3,6]
Output: 6
Explanation: We use the rods of lengths 6 and 1+2+3 to make two supports of height 6.

Example 2:
Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We use the rods of lengths 1+2+5 and 3+4+6 to make two supports of height 10.

Example 3:
Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported since the two supports cannot be of the same height.

Constraints:
- 1 <= rods.length <= 20
- 1 <= rods[i] <= 1000
- The sum of rods is at most 5000.
"""

# Solution
from collections import defaultdict

def tallestBillboard(rods):
    """
    Function to find the maximum height of the billboard that can be supported by two rods of the same height.
    
    Args:
    rods (List[int]): List of rod lengths.
    
    Returns:
    int: Maximum height of the billboard that can be supported, or 0 if not possible.
    """
    dp = {0: 0}  # Dictionary to store the difference and the maximum height for that difference.

    for rod in rods:
        current_dp = dp.copy()
        for diff, height in current_dp.items():
            # Case 1: Add the rod to one side
            dp[diff + rod] = max(dp.get(diff + rod, 0), height)
            # Case 2: Add the rod to the other side
            dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), height + min(diff, rod))
    
    return dp[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rods1 = [1, 2, 3, 6]
    print("Test Case 1 Output:", tallestBillboard(rods1))  # Expected Output: 6

    # Test Case 2
    rods2 = [1, 2, 3, 4, 5, 6]
    print("Test Case 2 Output:", tallestBillboard(rods2))  # Expected Output: 10

    # Test Case 3
    rods3 = [1, 2]
    print("Test Case 3 Output:", tallestBillboard(rods3))  # Expected Output: 0

    # Test Case 4
    rods4 = [1, 2, 3, 4, 5, 10]
    print("Test Case 4 Output:", tallestBillboard(rods4))  # Expected Output: 10

    # Test Case 5
    rods5 = [1, 1, 2, 3, 6]
    print("Test Case 5 Output:", tallestBillboard(rods5))  # Expected Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of rods is at most 20, and the sum of rods is at most 5000.
- For each rod, we iterate over the current state of the `dp` dictionary, which can have at most O(sum(rods)) keys.
- Thus, the time complexity is O(n * sum(rods)), where n is the number of rods.

Space Complexity:
- The `dp` dictionary can have at most O(sum(rods)) keys, where each key-value pair takes O(1) space.
- Thus, the space complexity is O(sum(rods)).
"""

# Topic: Dynamic Programming (DP)