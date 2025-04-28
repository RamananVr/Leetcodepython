"""
LeetCode Question #2158: Amount of New Area Painted Each Day

Problem Statement:
You are given an array of `paint` of length `n`, where `paint[i] = [start_i, end_i]` represents that on the i-th day you are painting the area between `start_i` and `end_i` (inclusive). Each day, any overlapping area with previous days is ignored, i.e., only the unpainted area is painted.

Return an array `result` of length `n` where `result[i]` is the amount of new area painted on the i-th day.

Example:
Input: paint = [[1, 4], [4, 7], [5, 8]]
Output: [3, 3, 1]
Explanation:
Day 1: Paint from 1 to 4, new area is 3.
Day 2: Paint from 4 to 7, new area is 3.
Day 3: Paint from 5 to 8, new area is 1.

Constraints:
- 1 <= paint.length <= 10^5
- paint[i].length == 2
- 0 <= start_i < end_i <= 10^5
"""

# Solution
def amountPainted(paint):
    """
    Calculate the amount of new area painted each day.

    :param paint: List[List[int]] - List of intervals representing painting days.
    :return: List[int] - Amount of new area painted each day.
    """
    max_end = max(end for _, end in paint)
    painted = [0] * (max_end + 1)
    result = [0] * len(paint)

    for i, (start, end) in enumerate(paint):
        while start < end:
            if painted[start] == 0:
                painted[start] = 1
                result[i] += 1
            start += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    paint = [[1, 4], [4, 7], [5, 8]]
    print(amountPainted(paint))  # Output: [3, 3, 1]

    # Test Case 2
    paint = [[1, 5], [2, 6], [3, 7]]
    print(amountPainted(paint))  # Output: [4, 1, 1]

    # Test Case 3
    paint = [[0, 2], [2, 4], [1, 3]]
    print(amountPainted(paint))  # Output: [2, 2, 0]

    # Test Case 4
    paint = [[0, 10], [5, 15], [10, 20]]
    print(amountPainted(paint))  # Output: [10, 5, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through each interval in `paint` and processes each unit of the interval.
- In the worst case, where intervals are disjoint, the total number of iterations is proportional to the sum of the lengths of all intervals.
- Let `L` be the sum of the lengths of all intervals. The time complexity is O(L).

Space Complexity:
- The `painted` array is used to track painted areas, and its size is proportional to the maximum endpoint in `paint`.
- Let `M` be the maximum endpoint in `paint`. The space complexity is O(M).
"""

# Topic: Arrays