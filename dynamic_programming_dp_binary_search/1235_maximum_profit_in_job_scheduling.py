"""
LeetCode Question #1235: Maximum Profit in Job Scheduling

Problem Statement:
We have `n` jobs, where every job is represented by three arrays: `startTime`, `endTime`, and `profit`. 
The `i-th` job starts at `startTime[i]` and ends at `endTime[i]`, and if you choose this job, you will receive a profit of `profit[i]`.

You're tasked with finding the maximum profit you can achieve such that no two jobs overlap. You may schedule the jobs in any order.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset of jobs with maximum profit is [1,4] with profit = 50 + 70 = 120.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset of jobs with maximum profit is [1,4] with profit = 20 + 70 = 150.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:
- 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
- 1 <= startTime[i] < endTime[i] <= 10^9
- 1 <= profit[i] <= 10^4
"""

from typing import List
from bisect import bisect_left

def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # Combine the job details into a single list and sort by end time
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)
    
    # dp array to store the maximum profit at each step
    dp = [0] * (n + 1)
    end_times = [job[1] for job in jobs]  # Extract end times for binary search

    for i in range(1, n + 1):
        start, end, prof = jobs[i - 1]
        
        # Find the last job that doesn't overlap with the current job
        idx = bisect_left(end_times, start)
        
        # Max profit is either taking the current job or skipping it
        dp[i] = max(dp[i - 1], dp[idx] + prof)
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(jobScheduling(startTime, endTime, profit))  # Output: 120

    # Test Case 2
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    print(jobScheduling(startTime, endTime, profit))  # Output: 150

    # Test Case 3
    startTime = [1, 1, 1]
    endTime = [2, 3, 4]
    profit = [5, 6, 4]
    print(jobScheduling(startTime, endTime, profit))  # Output: 6

"""
Time Complexity:
- Sorting the jobs takes O(n log n).
- For each job, we perform a binary search to find the last non-overlapping job, which takes O(log n).
- Thus, the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) due to the `dp` array and the `end_times` list.

Topic: Dynamic Programming (DP), Binary Search
"""