"""
LeetCode Problem #497: Random Point in Non-overlapping Rectangles

Problem Statement:
You are given an array of non-overlapping axis-aligned rectangles `rects` where `rects[i] = [ai, bi, xi, yi]` 
indicates that the bottom-left corner of the rectangle is `(ai, bi)` and the top-right corner is `(xi, yi)`.

Design a class `Solution` which supports the following two methods:
1. `__init__(rects: List[List[int]])`: Initializes the object with the given rectangles.
2. `pick(): List[int]`: Returns a random integer point `[u, v]` inside one of the given rectangles. 
   A point `(u, v)` is considered inside a rectangle if `ai <= u <= xi` and `bi <= v <= yi`. 
   The probability of picking a point from a rectangle is proportional to its area.

Constraints:
- 1 <= rects.length <= 100
- rects[i].length == 4
- -10^9 <= ai < xi <= 10^9
- -10^9 <= bi < yi <= 10^9
- All rectangles are non-overlapping.
- At most 10^4 calls will be made to `pick`.

"""

import random
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        self.total_area = 0
        
        # Calculate the area of each rectangle and store cumulative weights
        for rect in rects:
            x1, y1, x2, y2 = rect
            area = (x2 - x1 + 1) * (y2 - y1 + 1)  # Area of the rectangle
            self.total_area += area
            self.weights.append(self.total_area)  # Cumulative sum of areas

    def pick(self) -> List[int]:
        # Randomly select a rectangle based on weights
        target = random.randint(1, self.total_area)
        rect_index = self._binary_search(target)
        
        # Pick a random point within the selected rectangle
        x1, y1, x2, y2 = self.rects[rect_index]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]

    def _binary_search(self, target: int) -> int:
        # Binary search to find the rectangle corresponding to the target weight
        left, right = 0, len(self.weights) - 1
        while left < right:
            mid = (left + right) // 2
            if self.weights[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


# Example Test Cases
if __name__ == "__main__":
    # Initialize the solution with rectangles
    rects = [[1, 1, 5, 5], [10, 10, 13, 13], [20, 20, 25, 25]]
    solution = Solution(rects)
    
    # Test the pick method
    print(solution.pick())  # Random point from one of the rectangles
    print(solution.pick())  # Random point from one of the rectangles
    print(solution.pick())  # Random point from one of the rectangles

"""
Time Complexity Analysis:
- Initialization (__init__):
  - Calculating the area of each rectangle and cumulative weights takes O(n), where n is the number of rectangles.
- Picking a point (pick):
  - Binary search to find the rectangle index takes O(log n).
  - Randomly selecting a point within the rectangle takes O(1).
  - Overall complexity for pick is O(log n).

Space Complexity Analysis:
- The space complexity is O(n) for storing the cumulative weights.

Topic: Randomization, Binary Search
"""