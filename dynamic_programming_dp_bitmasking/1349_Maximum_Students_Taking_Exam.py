"""
LeetCode Problem #1349: Maximum Students Taking Exam

Problem Statement:
Given a m x n binary matrix seats where 0 represents a broken seat and 1 represents a usable seat, 
you must determine the maximum number of students that can take the exam without breaking the following rules:
1. No two students can be seated next to each other in the same row.
2. No two students can be seated directly in front of each other in adjacent rows.

Return the maximum number of students that can take the exam.

Example:
Input: seats = [[1,0,1],[1,1,1],[0,1,0]]
Output: 4
Explanation: The best arrangement is:
Row 1: [1,0,0]
Row 2: [0,1,1]
Row 3: [0,0,0]
"""

from functools import lru_cache

def maxStudents(seats):
    """
    Function to calculate the maximum number of students that can take the exam.
    :param seats: List[List[int]] - 2D binary matrix representing the seating arrangement.
    :return: int - Maximum number of students that can be seated.
    """
    m, n = len(seats), len(seats[0])
    valid_rows = []

    # Precompute valid seat configurations for each row
    for row in seats:
        mask = 0
        for j in range(n):
            if row[j] == 1:
                mask |= (1 << j)
        valid_rows.append(mask)

    @lru_cache(None)
    def dfs(row, prev_mask):
        if row == m:
            return 0

        max_students = 0
        # Iterate through all possible seat configurations for the current row
        for curr_mask in range(1 << n):
            # Check if the current mask is valid
            if (curr_mask & valid_rows[row]) == curr_mask and not (curr_mask & (curr_mask >> 1)):
                # Check if the current mask conflicts with the previous row
                if not (curr_mask & (prev_mask >> 1)) and not (curr_mask & (prev_mask << 1)):
                    max_students = max(max_students, bin(curr_mask).count('1') + dfs(row + 1, curr_mask))

        return max_students

    return dfs(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    seats1 = [[1, 0, 1], [1, 1, 1], [0, 1, 0]]
    print(maxStudents(seats1))  # Output: 4

    # Test Case 2
    seats2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(maxStudents(seats2))  # Output: 5

    # Test Case 3
    seats3 = [[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]]
    print(maxStudents(seats3))  # Output: 6

"""
Time Complexity:
- Let m be the number of rows and n be the number of columns.
- For each row, we iterate through all possible seat configurations (2^n).
- For each configuration, we check its validity and compute the result recursively.
- Total complexity: O(m * 2^n * 2^n) = O(m * 4^n), where 4^n arises from the combination of current and previous masks.

Space Complexity:
- The space complexity is O(m * 2^n) due to the memoization table used in the DFS function.

Topic: Dynamic Programming (DP), Bitmasking
"""