"""
LeetCode Question #1723: Find Minimum Time to Finish All Jobs

Problem Statement:
You are given an integer array `jobs`, where `jobs[i]` is the amount of time it takes to complete the i-th job. 
There are `k` workers that you can assign jobs to. Each job should be assigned to exactly one worker. 
The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. 
Your goal is to distribute the jobs such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

Constraints:
- 1 <= k <= jobs.length <= 12
- 1 <= jobs[i] <= 10^7
"""

from typing import List

def minimumTimeRequired(jobs: List[int], k: int) -> int:
    """
    Finds the minimum possible maximum working time of any assignment.
    """
    def canDistribute(jobs, k, max_time):
        # Helper function to check if we can distribute jobs within max_time
        workers = [0] * k

        def backtrack(index):
            if index == len(jobs):
                return True
            for i in range(k):
                if workers[i] + jobs[index] <= max_time:
                    workers[i] += jobs[index]
                    if backtrack(index + 1):
                        return True
                    workers[i] -= jobs[index]
                # If a worker has no jobs assigned, break to avoid redundant checks
                if workers[i] == 0:
                    break
            return False

        return backtrack(0)

    jobs.sort(reverse=True)  # Sort jobs in descending order for optimization
    left, right = max(jobs), sum(jobs)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if canDistribute(jobs, k, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    jobs = [3, 2, 3]
    k = 3
    print(minimumTimeRequired(jobs, k))  # Output: 3

    # Test Case 2
    jobs = [1, 2, 4, 7, 8]
    k = 2
    print(minimumTimeRequired(jobs, k))  # Output: 11

    # Test Case 3
    jobs = [5, 5, 4, 4, 4]
    k = 2
    print(minimumTimeRequired(jobs, k))  # Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the jobs array takes O(n log n), where n is the number of jobs.
- The binary search runs in O(log(sum(jobs) - max(jobs))).
- The backtracking function has a worst-case complexity of O(k^n), where n is the number of jobs and k is the number of workers.
- Overall, the time complexity is approximately O(n log n + log(sum(jobs)) * k^n).

Space Complexity:
- The space complexity is O(k + n), where k is the number of workers (for the workers array) and n is the recursion depth.

Primary Topic: Backtracking
"""