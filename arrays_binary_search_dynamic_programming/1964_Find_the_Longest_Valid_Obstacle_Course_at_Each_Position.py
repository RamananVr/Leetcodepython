"""
LeetCode Problem #1964: Find the Longest Valid Obstacle Course at Each Position

Problem Statement:
You want to build some obstacle courses. You are given a 0-indexed integer array `obstacles` of length `n`, where `obstacles[i]` describes the height of the `i`th obstacle.

For every index `i` between `0` and `n - 1` (inclusive), find the length of the longest obstacle course in `obstacles` such that:
- You choose any number of obstacles between `0` and `i` inclusive.
- You must include the `i`th obstacle in the course.
- You must put the chosen obstacles in the same order as they appear in `obstacles`.
- Every obstacle in the course (except the first) must be greater than or equal to the obstacle immediately before it.

Return an array `ans` of length `n`, where `ans[i]` is the length of the longest obstacle course for index `i`.

Example 1:
Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,2], [1,2,2] has length 3.

Example 2:
Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [1], [1] has length 1.

Example 3:
Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [1], [1] has length 1.
- i = 2: [3,5], [3,5] has length 2.
- i = 3: [3,5,6], [3,5,6] has length 3.
- i = 4: [3,4], [3,4] has length 2.
- i = 5: [3,4,2], [3,4,2] has length 2.

Constraints:
- `n == obstacles.length`
- `1 <= n <= 10^5`
- `1 <= obstacles[i] <= 10^7`
"""

from bisect import bisect_right

def longestObstacleCourseAtEachPosition(obstacles):
    """
    Finds the length of the longest valid obstacle course at each position.

    :param obstacles: List[int] - The heights of the obstacles.
    :return: List[int] - The lengths of the longest valid obstacle courses at each position.
    """
    n = len(obstacles)
    ans = []
    lis = []  # This will store the smallest ending values of increasing subsequences of each length.

    for obstacle in obstacles:
        # Find the position to insert the current obstacle in the LIS array.
        pos = bisect_right(lis, obstacle)
        if pos == len(lis):
            lis.append(obstacle)  # Extend the LIS if the obstacle is greater than all elements in lis.
        else:
            lis[pos] = obstacle  # Replace the element at pos to maintain the smallest possible values.
        ans.append(pos + 1)  # Length of the LIS ending at this obstacle.

    return ans

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    obstacles1 = [1, 2, 3, 2]
    print(longestObstacleCourseAtEachPosition(obstacles1))  # Output: [1, 2, 3, 3]

    # Test Case 2
    obstacles2 = [2, 2, 1]
    print(longestObstacleCourseAtEachPosition(obstacles2))  # Output: [1, 2, 1]

    # Test Case 3
    obstacles3 = [3, 1, 5, 6, 4, 2]
    print(longestObstacleCourseAtEachPosition(obstacles3))  # Output: [1, 1, 2, 3, 2, 2]

    # Test Case 4
    obstacles4 = [5, 1, 5, 5, 1, 3, 4, 5]
    print(longestObstacleCourseAtEachPosition(obstacles4))  # Output: [1, 1, 2, 3, 1, 2, 3, 4]

# Time Complexity Analysis:
# - For each obstacle, we perform a binary search on the `lis` array, which takes O(log k), where k is the length of `lis`.
# - In the worst case, we process all `n` obstacles, so the total time complexity is O(n log n).

# Space Complexity Analysis:
# - The `lis` array stores at most `n` elements in the worst case, so the space complexity is O(n).
# - The `ans` array also takes O(n) space.
# - Overall space complexity is O(n).

# Topic: Arrays, Binary Search, Dynamic Programming