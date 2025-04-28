"""
LeetCode Problem #2377: Sort the Students by Their Kth Score

Problem Statement:
You are given a 2D integer array `score` where `score[i]` is an array that contains the scores of the ith student in multiple subjects. 
You are also given an integer `k`. Sort the students based on their scores in the kth (0-indexed) column in descending order.

Return the 2D array `score` after sorting it.

Constraints:
- `1 <= score.length, score[i].length <= 250`
- `0 <= score[i][j] <= 10^5`
- `0 <= k < score[i].length`
"""

from typing import List

def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
    """
    Sorts the students based on their scores in the kth column in descending order.

    Args:
    score (List[List[int]]): A 2D list where each sublist represents a student's scores.
    k (int): The index of the column to sort by.

    Returns:
    List[List[int]]: The sorted 2D list.
    """
    # Sort the rows of the score matrix based on the kth column in descending order
    return sorted(score, key=lambda x: x[k], reverse=True)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    score1 = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    k1 = 2
    print(sortTheStudents(score1, k1))  # Expected: [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]

    # Test Case 2
    score2 = [[3, 4], [5, 6]]
    k2 = 0
    print(sortTheStudents(score2, k2))  # Expected: [[5, 6], [3, 4]]

    # Test Case 3
    score3 = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
    k3 = 1
    print(sortTheStudents(score3, k3))  # Expected: [[2, 3, 1], [1, 2, 3], [3, 2, 1]]

"""
Time Complexity Analysis:
- Sorting the list of students involves a time complexity of O(n * log(n)), where n is the number of students (rows in the `score` array).
- The key function (lambda) runs in O(1) for each comparison since it accesses a single element in the row.

Overall Time Complexity: O(n * log(n))

Space Complexity Analysis:
- The sorting operation is performed in-place (if using Timsort, which is Python's default sorting algorithm), so the space complexity is O(1) for the input list.
- However, the sorting algorithm may use O(n) additional space for temporary storage during the sort.

Overall Space Complexity: O(n)

Topic: Sorting
"""