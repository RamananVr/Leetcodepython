"""
LeetCode Problem #1376: Time Needed to Inform All Employees

Problem Statement:
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has the ID headID.

Each employee has one direct manager given in the `manager` array where `manager[i]` is the direct manager of the `i-th` employee, `manager[headID] = -1`. Also, it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know the news.

The `informTime` array is such that `informTime[i]` is the time it takes for the `i-th` employee to inform all their direct subordinates. Return the total time it takes to inform all the employees.

Constraints:
- 1 <= n <= 10^5
- 0 <= headID < n
- manager.length == n
- 0 <= manager[i] < n (for all i != headID)
- manager[headID] == -1
- informTime.length == n
- 0 <= informTime[i] <= 1000
- All the values of `informTime[i]` are non-negative.
- It is guaranteed that all employees can be informed.

Example:
Input: n = 6, headID = 2, manager = [2, 2, -1, 2, 2, 2], informTime = [0, 0, 1, 0, 0, 0]
Output: 1
Explanation: The head of the company with ID = 2 is the only one who can inform all employees. The time it takes to inform all employees is 1.

"""

from collections import defaultdict, deque

def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
    # Build an adjacency list to represent the tree structure
    tree = defaultdict(list)
    for employee, mgr in enumerate(manager):
        if mgr != -1:
            tree[mgr].append(employee)
    
    # Perform BFS to calculate the total time to inform all employees
    queue = deque([(headID, 0)])  # (current_employee, time_taken_to_reach)
    max_time = 0
    
    while queue:
        current, time_taken = queue.popleft()
        max_time = max(max_time, time_taken)
        for subordinate in tree[current]:
            queue.append((subordinate, time_taken + informTime[current]))
    
    return max_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    headID1 = 2
    manager1 = [2, 2, -1, 2, 2, 2]
    informTime1 = [0, 0, 1, 0, 0, 0]
    print(numOfMinutes(n1, headID1, manager1, informTime1))  # Output: 1

    # Test Case 2
    n2 = 7
    headID2 = 6
    manager2 = [1, 2, 3, 4, 5, 6, -1]
    informTime2 = [0, 6, 5, 4, 3, 2, 1]
    print(numOfMinutes(n2, headID2, manager2, informTime2))  # Output: 21

    # Test Case 3
    n3 = 4
    headID3 = 0
    manager3 = [-1, 0, 0, 1]
    informTime3 = [1, 2, 3, 4]
    print(numOfMinutes(n3, headID3, manager3, informTime3))  # Output: 7

    # Test Case 4
    n4 = 1
    headID4 = 0
    manager4 = [-1]
    informTime4 = [0]
    print(numOfMinutes(n4, headID4, manager4, informTime4))  # Output: 0

"""
Time Complexity:
- Building the adjacency list takes O(n).
- BFS traversal visits each employee once, so it takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list (tree) takes O(n) space.
- The queue used in BFS takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Graphs, BFS, Tree
"""