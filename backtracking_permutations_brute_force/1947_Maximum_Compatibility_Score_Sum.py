"""
LeetCode Problem #1947: Maximum Compatibility Score Sum

Problem Statement:
There are `n` students and `n` mentors, each with a binary array representing their skills. 
The compatibility score between a student and a mentor is defined as the number of positions 
where their skills match. For example, if the student's skill array is [1, 0, 1] and the 
mentor's skill array is [0, 0, 1], the compatibility score is 2 because they match at the 
2nd and 3rd positions.

You are tasked to assign each student to one mentor such that the sum of their compatibility 
scores is maximized.

Return the maximum compatibility score sum that can be achieved.

Constraints:
- n == students.length == mentors.length
- m == students[i].length == mentors[j].length
- 1 <= n, m <= 8
- students[i][k] is either 0 or 1
- mentors[j][k] is either 0 or 1
"""

from itertools import permutations

def maxCompatibilitySum(students, mentors):
    """
    Calculate the maximum compatibility score sum by trying all possible assignments
    of students to mentors.

    :param students: List[List[int]] - Binary skill arrays of students
    :param mentors: List[List[int]] - Binary skill arrays of mentors
    :return: int - Maximum compatibility score sum
    """
    def compatibility_score(student, mentor):
        """Calculate the compatibility score between a student and a mentor."""
        return sum(s == m for s, m in zip(student, mentor))
    
    n = len(students)
    max_score = 0

    # Try all permutations of mentor assignments
    for perm in permutations(range(n)):
        current_score = 0
        for i, mentor_idx in enumerate(perm):
            current_score += compatibility_score(students[i], mentors[mentor_idx])
        max_score = max(max_score, current_score)
    
    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(maxCompatibilitySum(students, mentors))  # Output: 8

    # Test Case 2
    students = [[0, 0], [1, 1], [0, 1]]
    mentors = [[1, 1], [0, 0], [1, 0]]
    print(maxCompatibilitySum(students, mentors))  # Output: 4

    # Test Case 3
    students = [[1, 0, 1], [0, 1, 0]]
    mentors = [[0, 1, 0], [1, 0, 1]]
    print(maxCompatibilitySum(students, mentors))  # Output: 6

"""
Time Complexity:
- Calculating the compatibility score for a single student-mentor pair takes O(m), where m is the length of the skill array.
- There are n! permutations of mentor assignments, where n is the number of students/mentors.
- For each permutation, we calculate the compatibility score for n pairs.
- Overall time complexity: O(n! * n * m).

Space Complexity:
- The space complexity is O(n) for storing the current permutation during iteration.

Topic: Backtracking, Permutations, Brute Force
"""