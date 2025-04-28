"""
LeetCode Problem #1280: Students and Examinations

Problem Statement:
There are n students and m exams. You are given a 2D integer array `logs` where each `logs[i] = [IDi, examIdi]` indicates that the student with ID `IDi` attended the exam with ID `examIdi`. The array `logs` does not necessarily have all the students and exams, and the IDs are not guaranteed to be in order.

Return a 2D integer array `result` where `result[i] = [studentIdi, counti]` indicates that the student with ID `studentIdi` attended `counti` exams. The result array should be sorted by `studentIdi` in ascending order.

Constraints:
- 1 <= n, m <= 100
- 1 <= logs.length <= 10^4
- 1 <= IDi <= n
- 1 <= examIdi <= m
- All the values in `logs[i]` are unique.

Example:
Input: n = 4, logs = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: [[1, 2], [2, 1], [3, 1], [4, 0]]

Explanation:
- Student 1 attended exams 2 and 3.
- Student 2 attended exam 3.
- Student 3 attended exam 4.
- Student 4 did not attend any exams.
"""

from collections import defaultdict

def count_exams(n, logs):
    """
    Function to count the number of exams attended by each student.

    :param n: int - Number of students
    :param logs: List[List[int]] - Logs of student exam attendance
    :return: List[List[int]] - List of [studentId, count] sorted by studentId
    """
    # Dictionary to store the count of exams attended by each student
    attendance = defaultdict(int)
    
    # Count the number of exams attended by each student
    for student_id, _ in logs:
        attendance[student_id] += 1
    
    # Prepare the result array
    result = []
    for student_id in range(1, n + 1):
        result.append([student_id, attendance[student_id]])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    logs = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(count_exams(n, logs))  # Expected Output: [[1, 2], [2, 1], [3, 1], [4, 0]]

    # Test Case 2
    n = 3
    logs = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3]]
    print(count_exams(n, logs))  # Expected Output: [[1, 2], [2, 2], [3, 1]]

    # Test Case 3
    n = 5
    logs = []
    print(count_exams(n, logs))  # Expected Output: [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]

# Time Complexity Analysis:
# - Iterating through the `logs` array takes O(len(logs)).
# - Constructing the result array for `n` students takes O(n).
# - Overall time complexity: O(len(logs) + n).

# Space Complexity Analysis:
# - The `attendance` dictionary stores at most `n` keys, so it takes O(n) space.
# - The result array also takes O(n) space.
# - Overall space complexity: O(n).

# Topic: Hash Table