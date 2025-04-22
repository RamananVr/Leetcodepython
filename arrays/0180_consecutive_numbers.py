"""
LeetCode Question #180: Consecutive Numbers

Problem Statement:
Write an SQL query to find all numbers that appear at least three times consecutively in a table.

The table `Logs` contains the following columns:
- `Id`: The ID of the log entry (primary key).
- `Num`: The number logged.

Your query should return the result table in any order.

Example:
Input:
Logs table:
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 2   |
| 6  | 3   |
+----+-----+

Output:
+-----+
| Num |
+-----+
| 1   |
+-----+

Explanation:
The number 1 appears three times consecutively in the table.

Note:
The solution must be written in SQL, but for this exercise, we will simulate the problem in Python for educational purposes.
"""

# Python Solution
def find_consecutive_numbers(logs):
    """
    Function to find numbers that appear at least three times consecutively.

    Args:
    logs (List[Tuple[int, int]]): A list of tuples representing the logs table, where each tuple is (Id, Num).

    Returns:
    List[int]: A list of numbers that appear at least three times consecutively.
    """
    result = set()
    n = len(logs)

    for i in range(n - 2):
        # Check if the current number and the next two numbers are the same
        if logs[i][1] == logs[i + 1][1] == logs[i + 2][1]:
            result.add(logs[i][1])

    return list(result)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (6, 3),
    ]
    print(find_consecutive_numbers(logs))  # Output: [1]

    # Test Case 2
    logs = [
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 5),
        (5, 6),
        (6, 6),
        (7, 6),
    ]
    print(find_consecutive_numbers(logs))  # Output: [5, 6]

    # Test Case 3
    logs = [
        (1, 7),
        (2, 8),
        (3, 9),
        (4, 10),
    ]
    print(find_consecutive_numbers(logs))  # Output: []

    # Test Case 4
    logs = [
        (1, 3),
        (2, 3),
        (3, 3),
        (4, 3),
        (5, 3),
    ]
    print(find_consecutive_numbers(logs))  # Output: [3]


# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the logs list with a sliding window of size 3. 
This results in a time complexity of O(n), where n is the number of entries in the logs table.

Space Complexity:
The space complexity is O(k), where k is the number of unique numbers that appear at least three times consecutively.
In the worst case, k could be equal to n, but typically k is much smaller than n.
"""

# Topic: Arrays