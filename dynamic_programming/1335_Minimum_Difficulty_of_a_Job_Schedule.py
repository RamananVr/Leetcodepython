"""
LeetCode Problem #1335: Minimum Difficulty of a Job Schedule

Problem Statement:
You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e., to schedule a job, you have to finish all the jobs before it in the same day). You have to finish at least one job every day. The difficulty of a day is the maximum difficulty of a job done on that day. The difficulty of the schedule is the sum of difficulties of each day of the schedule.

You are given an integer array `jobDifficulty` and an integer `d`. The difficulty of the `i-th` job is `jobDifficulty[i]`.

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs, return -1.

Constraints:
- `1 <= jobDifficulty.length <= 300`
- `0 <= jobDifficulty[i] <= 1000`
- `1 <= d <= 10`
"""

# Solution
from functools import lru_cache

def minDifficulty(jobDifficulty, d):
    n = len(jobDifficulty)
    if n < d:
        return -1  # Not enough jobs to schedule in d days

    @lru_cache(None)
    def dp(day, i):
        # Base case: last day, schedule all remaining jobs
        if day == d:
            return max(jobDifficulty[i:])
        
        # Recursive case: try splitting jobs into current day and future days
        max_difficulty = 0
        min_total_difficulty = float('inf')
        for j in range(i, n - (d - day)):
            max_difficulty = max(max_difficulty, jobDifficulty[j])
            min_total_difficulty = min(min_total_difficulty, max_difficulty + dp(day + 1, j + 1))
        return min_total_difficulty

    return dp(1, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    print(minDifficulty(jobDifficulty, d))  # Expected Output: 7

    # Test Case 2
    jobDifficulty = [9, 9, 9]
    d = 4
    print(minDifficulty(jobDifficulty, d))  # Expected Output: -1

    # Test Case 3
    jobDifficulty = [1, 1, 1]
    d = 3
    print(minDifficulty(jobDifficulty, d))  # Expected Output: 3

    # Test Case 4
    jobDifficulty = [7, 1, 7, 1, 7, 1]
    d = 3
    print(minDifficulty(jobDifficulty, d))  # Expected Output: 15

    # Test Case 5
    jobDifficulty = [11, 111, 22, 222, 33, 333, 44, 444]
    d = 6
    print(minDifficulty(jobDifficulty, d))  # Expected Output: 843

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses memoization with `lru_cache`, and the state space is defined by `day` and `i`.
- There are `d` possible values for `day` and `n` possible values for `i`, resulting in a total of `O(d * n)` states.
- For each state, we iterate over the remaining jobs, which can take up to `O(n)` time.
- Therefore, the overall time complexity is `O(d * n^2)`.

Space Complexity:
- The memoization table stores `O(d * n)` states, each taking `O(1)` space.
- Additionally, the recursion stack can go up to `O(d)` depth.
- Therefore, the space complexity is `O(d * n)`.

Topic: Dynamic Programming
"""