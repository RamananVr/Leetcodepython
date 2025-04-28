"""
LeetCode Problem #1986: Minimum Number of Work Sessions to Finish the Tasks

Problem Statement:
You are given `n` tasks labeled from 0 to n - 1 represented by a 0-indexed integer array `tasks`, where `tasks[i]` is the duration of the ith task. You are also given an integer `sessionTime` which represents the maximum duration of a single work session.

You need to find the minimum number of work sessions needed to finish all the tasks such that:
1. Each task is assigned to exactly one work session.
2. The sum of the task durations in a single work session is at most `sessionTime`.

Return the minimum number of work sessions required to finish all the tasks.

Constraints:
- `n == tasks.length`
- `1 <= n <= 14`
- `1 <= tasks[i] <= 10`
- `1 <= sessionTime <= 15`
"""

from functools import lru_cache
from typing import List

def minSessions(tasks: List[int], sessionTime: int) -> int:
    """
    Finds the minimum number of work sessions required to complete all tasks.
    """
    n = len(tasks)

    # Use bitmasking to represent subsets of tasks
    @lru_cache(None)
    def dfs(mask, remaining_time):
        if mask == 0:  # All tasks are completed
            return 0

        # Start a new session
        min_sessions = float('inf')
        for i in range(n):
            if mask & (1 << i):  # If task i is not yet completed
                if tasks[i] <= remaining_time:
                    # Add task i to the current session
                    min_sessions = min(min_sessions, dfs(mask ^ (1 << i), remaining_time - tasks[i]))
                else:
                    # Start a new session for task i
                    min_sessions = min(min_sessions, 1 + dfs(mask ^ (1 << i), sessionTime - tasks[i]))

        return min_sessions

    # Start with all tasks uncompleted (mask = (1 << n) - 1) and no remaining time in the current session
    return 1 + dfs((1 << n) - 1, 0)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks = [1, 2, 3]
    sessionTime = 3
    print(minSessions(tasks, sessionTime))  # Output: 2

    # Test Case 2
    tasks = [3, 1, 3, 1, 1]
    sessionTime = 8
    print(minSessions(tasks, sessionTime))  # Output: 2

    # Test Case 3
    tasks = [1, 2, 3, 4, 5]
    sessionTime = 15
    print(minSessions(tasks, sessionTime))  # Output: 1

    # Test Case 4
    tasks = [5, 5, 5, 5]
    sessionTime = 5
    print(minSessions(tasks, sessionTime))  # Output: 4


"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the `dfs` function is O(2^n * sessionTime), where `2^n` represents all subsets of tasks (bitmasking) and `sessionTime` represents the possible remaining time in a session.
- For each state, we iterate over `n` tasks, leading to a total complexity of O(n * 2^n * sessionTime).

Space Complexity:
- The space complexity is O(2^n * sessionTime) for the memoization table and O(n) for the recursion stack.
- Total space complexity: O(2^n * sessionTime).

Primary Topic: Dynamic Programming (Bitmasking)
"""