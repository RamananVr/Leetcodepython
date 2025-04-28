"""
LeetCode Problem #1465: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Problem Statement:
You are given a rectangular cake of size `h x w` and two arrays of integers `horizontalCuts` and `verticalCuts` 
where:
- `horizontalCuts[i]` is the distance from the top of the rectangular cake to the ith horizontal cut.
- `verticalCuts[j]` is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays. 
Since the answer can be a large number, return it modulo `10^9 + 7`.

Constraints:
- 2 <= h, w <= 10^9
- 1 <= horizontalCuts.length <= min(h - 1, 10^5)
- 1 <= verticalCuts.length <= min(w - 1, 10^5)
- 1 <= horizontalCuts[i] < h
- 1 <= verticalCuts[j] < w
- All the elements in `horizontalCuts` are distinct.
- All the elements in `verticalCuts` are distinct.
"""

# Python Solution
from typing import List

def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    MOD = 10**9 + 7

    # Sort the cuts
    horizontalCuts.sort()
    verticalCuts.sort()

    # Calculate the maximum gap between consecutive horizontal cuts
    max_h_gap = max(horizontalCuts[0], h - horizontalCuts[-1])  # Edge gaps
    for i in range(1, len(horizontalCuts)):
        max_h_gap = max(max_h_gap, horizontalCuts[i] - horizontalCuts[i - 1])

    # Calculate the maximum gap between consecutive vertical cuts
    max_v_gap = max(verticalCuts[0], w - verticalCuts[-1])  # Edge gaps
    for i in range(1, len(verticalCuts)):
        max_v_gap = max(max_v_gap, verticalCuts[i] - verticalCuts[i - 1])

    # Calculate the maximum area
    return (max_h_gap * max_v_gap) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    h1, w1 = 5, 4
    horizontalCuts1 = [1, 2, 4]
    verticalCuts1 = [1, 3]
    print(maxArea(h1, w1, horizontalCuts1, verticalCuts1))  # Expected Output: 4

    # Test Case 2
    h2, w2 = 5, 4
    horizontalCuts2 = [3, 1]
    verticalCuts2 = [1]
    print(maxArea(h2, w2, horizontalCuts2, verticalCuts2))  # Expected Output: 6

    # Test Case 3
    h3, w3 = 1000000000, 1000000000
    horizontalCuts3 = [2]
    verticalCuts3 = [2]
    print(maxArea(h3, w3, horizontalCuts3, verticalCuts3))  # Expected Output: 999999996

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting `horizontalCuts` and `verticalCuts` takes O(n log n) and O(m log m), where n is the length of `horizontalCuts` 
  and m is the length of `verticalCuts`.
- Calculating the maximum gaps takes O(n) and O(m).
- Overall time complexity: O(n log n + m log m).

Space Complexity:
- The sorting operations use O(n) and O(m) space for the sorted arrays.
- Overall space complexity: O(n + m).

Topic: Arrays, Sorting
"""