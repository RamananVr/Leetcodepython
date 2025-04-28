"""
LeetCode Problem #1051: Height Checker

Problem Statement:
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by an integer array `expected` where `expected[i]` is the expected height of the ith student in line.

You are given an integer array `heights` representing the current order that the students are standing in. Each `heights[i]` is the height of the ith student in line. Return the number of indices where `heights[i] != expected[i]`.

Example:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
    heights:  [1,1,4,2,1,3]
    expected: [1,1,1,2,3,4]
    Indices 2, 4, and 5 do not match.

Constraints:
- 1 <= heights.length <= 100
- 1 <= heights[i] <= 100
"""

# Python Solution
def heightChecker(heights):
    """
    Function to count the number of indices where the heights array does not match the expected sorted order.

    :param heights: List[int] - List of student heights
    :return: int - Number of indices where heights[i] != expected[i]
    """
    expected = sorted(heights)
    return sum(1 for i in range(len(heights)) if heights[i] != expected[i])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights = [1, 1, 4, 2, 1, 3]
    print(heightChecker(heights))  # Output: 3

    # Test Case 2
    heights = [5, 1, 2, 3, 4]
    print(heightChecker(heights))  # Output: 5

    # Test Case 3
    heights = [1, 2, 3, 4, 5]
    print(heightChecker(heights))  # Output: 0

    # Test Case 4
    heights = [10, 6, 6, 10, 10]
    print(heightChecker(heights))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the `heights` array takes O(n log n), where n is the length of the array.
- Comparing the `heights` and `expected` arrays takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `expected` array is a copy of the `heights` array, so it takes O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays