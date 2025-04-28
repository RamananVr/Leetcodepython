"""
LeetCode Question #2545: Sort the Students by Their Kth Score

Problem Statement:
You are given a 2D integer array `score` where `score[i]` is an array that represents the scores of the ith student in multiple subjects. 
You are also given an integer `k`.

Sort the students (i.e., the rows of the array) by their scores in the kth (0-indexed) column in descending order.

Return the array after sorting it.

Constraints:
- `1 <= score.length, score[i].length <= 250`
- `0 <= score[i][j] <= 10^5`
- `0 <= k < score[i].length`
"""

# Python Solution
from typing import List

def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
    # Sort the rows of the score array based on the kth column in descending order
    return sorted(score, key=lambda x: x[k], reverse=True)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    score1 = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    k1 = 2
    print(sortTheStudents(score1, k1))  # Expected Output: [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]

    # Test Case 2
    score2 = [[3, 4], [5, 6]]
    k2 = 0
    print(sortTheStudents(score2, k2))  # Expected Output: [[5, 6], [3, 4]]

    # Test Case 3
    score3 = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
    k3 = 1
    print(sortTheStudents(score3, k3))  # Expected Output: [[2, 3, 1], [1, 2, 3], [3, 2, 1]]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Sorting the array involves a time complexity of O(n * log(n)), where n is the number of rows in the `score` array.
   - The key function (lambda x: x[k]) is called once for each row, which is O(1) per row.
   - Overall time complexity: O(n * log(n)).

2. Space Complexity:
   - The sorting operation may require additional space for the sorted output, which is O(n).
   - No additional data structures are used apart from the input and output.
   - Overall space complexity: O(n).

Topic: Arrays
"""