"""
LeetCode Problem #2358: Maximum Number of Groups Entering a Competition

Problem Statement:
You are given a positive integer array `grades` representing the grades of students in a class. 
You want to form as many groups as possible such that each group contains at least one student, 
and the total number of students in each group is strictly greater than the total number of students in the previous group.

Return the maximum number of groups that can be formed.

Example:
Input: grades = [10, 6, 12, 7, 3, 5]
Output: 3
Explanation: The groups can be formed as follows:
- Group 1: [3]
- Group 2: [5, 6]
- Group 3: [7, 10, 12]
You can form 3 groups, but not more.

Constraints:
- 1 <= grades.length <= 10^5
- 1 <= grades[i] <= 10^6
"""

def maximumGroups(grades):
    """
    Function to calculate the maximum number of groups that can be formed
    such that the total number of students in each group is strictly greater
    than the total number of students in the previous group.

    :param grades: List[int] - List of grades of students
    :return: int - Maximum number of groups
    """
    n = len(grades)
    groups = 0
    current_group_size = 1

    while n >= current_group_size:
        groups += 1
        n -= current_group_size
        current_group_size += 1

    return groups

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grades1 = [10, 6, 12, 7, 3, 5]
    print(maximumGroups(grades1))  # Output: 3

    # Test Case 2
    grades2 = [8, 8, 8, 8]
    print(maximumGroups(grades2))  # Output: 2

    # Test Case 3
    grades3 = [1]
    print(maximumGroups(grades3))  # Output: 1

    # Test Case 4
    grades4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(maximumGroups(grades4))  # Output: 4

    # Test Case 5
    grades5 = [1000000] * 100000
    print(maximumGroups(grades5))  # Output: 447

"""
Time Complexity Analysis:
- The while loop runs until the sum of the first `k` natural numbers (1 + 2 + ... + k) exceeds `n`.
  This means the loop runs approximately O(sqrt(n)) iterations, where `n` is the length of the grades array.
- Therefore, the time complexity is O(sqrt(n)).

Space Complexity Analysis:
- The algorithm uses only a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy Algorithm
"""