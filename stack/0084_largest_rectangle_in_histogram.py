"""
LeetCode Question #84: Largest Rectangle in Histogram

Problem Statement:
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has an area of 10 units (formed by heights[2] and heights[3]).

Example 2:
Input: heights = [2,4]
Output: 4
Explanation: The largest rectangle has an area of 4 units (formed by heights[1]).

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

def largestRectangleArea(heights):
    """
    Calculate the largest rectangle area in a histogram.

    :param heights: List[int] - List of bar heights in the histogram
    :return: int - Maximum area of the rectangle
    """
    stack = []  # Stack to store indices of histogram bars
    max_area = 0  # Variable to store the maximum area
    n = len(heights)

    for i in range(n):
        # While the current bar is shorter than the bar at the stack's top index
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]  # Height of the rectangle
            width = i if not stack else i - stack[-1] - 1  # Width of the rectangle
            max_area = max(max_area, height * width)  # Update max_area

        stack.append(i)  # Push the current index onto the stack

    # Process remaining bars in the stack
    while stack:
        height = heights[stack.pop()]  # Height of the rectangle
        width = n if not stack else n - stack[-1] - 1  # Width of the rectangle
        max_area = max(max_area, height * width)  # Update max_area

    return max_area


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"Input: {heights1}, Output: {largestRectangleArea(heights1)}")  # Expected Output: 10

    # Test Case 2
    heights2 = [2, 4]
    print(f"Input: {heights2}, Output: {largestRectangleArea(heights2)}")  # Expected Output: 4

    # Test Case 3
    heights3 = [6, 2, 5, 4, 5, 1, 6]
    print(f"Input: {heights3}, Output: {largestRectangleArea(heights3)}")  # Expected Output: 12

    # Test Case 4
    heights4 = [1, 1, 1, 1, 1]
    print(f"Input: {heights4}, Output: {largestRectangleArea(heights4)}")  # Expected Output: 5

    # Test Case 5
    heights5 = [0, 0, 0, 0]
    print(f"Input: {heights5}, Output: {largestRectangleArea(heights5)}")  # Expected Output: 0


"""
Time Complexity:
- The algorithm processes each bar in the histogram exactly once, either by pushing it onto the stack or popping it off.
- Therefore, the time complexity is O(n), where n is the number of bars in the histogram.

Space Complexity:
- The space complexity is O(n) due to the stack used to store indices of histogram bars.

Topic: Stack
"""