"""
LeetCode Problem #2756: Maximum Number of Groups Entering a Competition

Problem Statement:
You are given an integer array `grades` representing the grades of students in a competition. 
The competition organizer wants to divide the students into the maximum number of groups such that:
1. Each group has at least one student.
2. The total number of students in the i-th group is strictly greater than the total number of students in the (i-1)-th group.

Return the maximum number of groups that can be formed.

Constraints:
- 1 <= len(grades) <= 10^5
- 1 <= grades[i] <= 10^6
"""

def maximumGroups(grades):
    """
    Function to calculate the maximum number of groups that can be formed.

    Args:
    grades (List[int]): List of student grades.

    Returns:
    int: Maximum number of groups.
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
    print(maximumGroups(grades1))  # Expected Output: 3

    # Test Case 2
    grades2 = [8, 8]
    print(maximumGroups(grades2))  # Expected Output: 1

    # Test Case 3
    grades3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(maximumGroups(grades3))  # Expected Output: 4

    # Test Case 4
    grades4 = [1]
    print(maximumGroups(grades4))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until `n` becomes less than `current_group_size`. 
  In the worst case, the loop runs approximately sqrt(n) times because the sum of the first k natural numbers 
  (1 + 2 + 3 + ... + k) is k * (k + 1) / 2, which grows quadratically.
- Therefore, the time complexity is O(sqrt(n)).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy
"""