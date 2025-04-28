"""
LeetCode Problem #1762: Buildings With an Ocean View

Problem Statement:
There are `n` buildings in a line. You are given an integer array `heights` of size `n` where `heights[i]` is the height of the `i`th building.

A building has an ocean view if all the buildings to its right have a smaller height. Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:
Input: heights = [4, 2, 3, 1]
Output: [0, 2, 3]
Explanation:
Building 0 has an ocean view because all the buildings to its right (2, 3, 1) have smaller heights.
Building 2 has an ocean view because all the buildings to its right (1) have smaller heights.
Building 3 has an ocean view because there are no buildings to its right.
Building 1 does not have an ocean view because building 2 is taller.

Example 2:
Input: heights = [4, 3, 2, 1]
Output: [0, 1, 2, 3]
Explanation: All the buildings have an ocean view.

Example 3:
Input: heights = [1, 3, 2, 4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Constraints:
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9
"""

# Python Solution
def findBuildings(heights):
    """
    Finds the indices of buildings with an ocean view.

    :param heights: List[int] - List of building heights
    :return: List[int] - Indices of buildings with an ocean view
    """
    n = len(heights)
    result = []
    max_height = float('-inf')  # Initialize max_height to negative infinity

    # Traverse the buildings from right to left
    for i in range(n - 1, -1, -1):
        if heights[i] > max_height:
            result.append(i)  # Add the index to the result
            max_height = heights[i]  # Update max_height

    # Reverse the result to return indices in increasing order
    return result[::-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [4, 2, 3, 1]
    print(findBuildings(heights1))  # Output: [0, 2, 3]

    # Test Case 2
    heights2 = [4, 3, 2, 1]
    print(findBuildings(heights2))  # Output: [0, 1, 2, 3]

    # Test Case 3
    heights3 = [1, 3, 2, 4]
    print(findBuildings(heights3))  # Output: [3]

    # Test Case 4
    heights4 = [5, 5, 5, 5]
    print(findBuildings(heights4))  # Output: [3]

    # Test Case 5
    heights5 = [10]
    print(findBuildings(heights5))  # Output: [0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the `heights` array once from right to left.
- This results in a time complexity of O(n), where `n` is the length of the `heights` array.

Space Complexity:
- The algorithm uses a list `result` to store the indices of buildings with an ocean view.
- In the worst case, all buildings have an ocean view, so the space complexity for `result` is O(n).
- Other variables (e.g., `max_height`) use O(1) space.
- Overall space complexity: O(n).

Topic: Arrays
"""