"""
LeetCode Problem #2323: Find Minimum Time to Finish All Jobs

Problem Statement:
You are given an integer array `jobs`, where `jobs[i]` is the amount of time it takes to complete the i-th job. 
There are `k` workers available to complete these jobs. Each job should be assigned to exactly one worker. 
The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. 
The goal is to distribute the jobs such that the maximum working time among all workers is minimized.

Return the minimum possible maximum working time of any assignment.

Constraints:
- 1 <= k <= jobs.length <= 12
- 1 <= jobs[i] <= 10^7
"""

from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def canDistribute(jobs, k, maxTime):
            # Helper function to check if we can distribute jobs within maxTime
            workers = [0] * k

            def backtrack(index):
                if index == len(jobs):
                    return True
                for i in range(k):
                    if workers[i] + jobs[index] <= maxTime:
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
    solution = Solution()

    # Test Case 1
    jobs1 = [3, 2, 3]
    k1 = 3
    print(solution.minimumTimeRequired(jobs1, k1))  # Output: 3

    # Test Case 2
    jobs2 = [1, 2, 4, 7, 8]
    k2 = 2
    print(solution.minimumTimeRequired(jobs2, k2))  # Output: 11

    # Test Case 3
    jobs3 = [5, 5, 4, 4, 4]
    k3 = 2
    print(solution.minimumTimeRequired(jobs3, k3))  # Output: 12


"""
Time Complexity:
- Sorting the jobs takes O(n log n), where n is the number of jobs.
- The binary search runs in O(log(sum(jobs) - max(jobs))).
- The backtracking function has a worst-case complexity of O(k^n), where n is the number of jobs and k is the number of workers.
- Overall, the complexity is approximately O(n log n + log(sum(jobs)) * k^n), but the constraints (n <= 12) make this feasible.

Space Complexity:
- The space complexity is O(k + n) due to the workers array and recursion stack.

Topic: Backtracking, Binary Search
"""