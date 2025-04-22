"""
LeetCode Question #546: Remove Boxes

Problem Statement:
You are given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), 
remove them and get k * k points.

Return the maximum points you can get.

Example 1:
Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (Remove 3 '2's, get 3 * 3 = 9 points)
----> [1, 3, 4, 3, 1] (Remove 1 '3', get 1 * 1 = 1 point)
----> [1, 3, 4, 1] (Remove 1 '3', get 1 * 1 = 1 point)
----> [1, 4, 1] (Remove 1 '4', get 1 * 1 = 1 point)
----> [1, 1] (Remove 2 '1's, get 2 * 2 = 4 points)
Total = 9 + 1 + 1 + 1 + 4 = 23

Constraints:
- 1 <= boxes.length <= 100
- 1 <= boxes[i] <= 100
"""

# Python Solution
from functools import lru_cache

def removeBoxes(boxes):
    @lru_cache(None)
    def dp(l, r, k):
        """
        l: left index of the current subarray
        r: right index of the current subarray
        k: number of boxes of the same color as boxes[r] contiguous to the right of r
        """
        if l > r:
            return 0
        
        # Extend the sequence of the same color to the left
        while l < r and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1
        
        # Option 1: Remove the boxes[r] group directly
        result = dp(l, r - 1, 0) + (k + 1) ** 2
        
        # Option 2: Try merging boxes[r] with another group of the same color
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                result = max(result, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
        
        return result
    
    return dp(0, len(boxes) - 1, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    print(removeBoxes(boxes))  # Output: 23

    # Test Case 2
    boxes = [1, 1, 1]
    print(removeBoxes(boxes))  # Output: 9

    # Test Case 3
    boxes = [1]
    print(removeBoxes(boxes))  # Output: 1

    # Test Case 4
    boxes = [1, 2, 1, 2, 1]
    print(removeBoxes(boxes))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
The function uses memoization to store results for subproblems defined by (l, r, k). 
There are O(n^3) possible states since l and r can each take O(n) values, and k can also take O(n) values in the worst case.
Each state requires O(n) work due to the loop over i, so the overall time complexity is O(n^4).

Space Complexity:
The space complexity is O(n^3) due to the memoization table storing results for O(n^3) states.
Additionally, the recursion stack can go up to O(n) depth, so the total space complexity is O(n^3).
"""

# Topic: Dynamic Programming (DP)