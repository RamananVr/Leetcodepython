"""
LeetCode Problem #1725: Number Of Rectangles That Can Form The Largest Square

Problem Statement:
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Find the number of rectangles that can make the largest square.

Example 1:
Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest square you can get from each rectangle is of side length 5. 
- From the first rectangle, you can get a square with a side length of 5.
- From the second rectangle, you can get a square with a side length of 3.
- From the third rectangle, you can get a square with a side length of 5.
- From the fourth rectangle, you can get a square with a side length of 5.
The largest square side length is 5, and you can get it out of 3 rectangles.

Example 2:
Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3

Constraints:
- 1 <= rectangles.length <= 1000
- 1 <= li, wi <= 10^9
- li != wi

"""

# Python Solution
from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # Step 1: Find the maximum square side length for each rectangle
        max_squares = [min(l, w) for l, w in rectangles]
        
        # Step 2: Find the largest square side length
        largest_square = max(max_squares)
        
        # Step 3: Count how many rectangles can form the largest square
        return max_squares.count(largest_square)

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    rectangles1 = [[5,8],[3,9],[5,12],[16,5]]
    print(solution.countGoodRectangles(rectangles1))  # Output: 3
    
    # Test Case 2
    rectangles2 = [[2,3],[3,7],[4,3],[3,7]]
    print(solution.countGoodRectangles(rectangles2))  # Output: 3
    
    # Test Case 3
    rectangles3 = [[1,2],[2,3],[3,4],[4,5]]
    print(solution.countGoodRectangles(rectangles3))  # Output: 1
    
    # Test Case 4
    rectangles4 = [[10,20],[15,15],[20,10],[5,5]]
    print(solution.countGoodRectangles(rectangles4))  # Output: 1

"""
Time Complexity Analysis:
- Calculating the minimum side for each rectangle takes O(n), where n is the number of rectangles.
- Finding the maximum square side length takes O(n).
- Counting the occurrences of the largest square side length also takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `max_squares` list stores the minimum side lengths for all rectangles, which takes O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""